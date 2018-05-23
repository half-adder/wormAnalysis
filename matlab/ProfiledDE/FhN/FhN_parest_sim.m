%% Simulation of Parameter Estimation for Perturbed FitzHugh-Nagumo Systems

odefn       = @fhnfunode;   % Function for ODE solver (exact)

fn.fn       = @fhnfun;       % RHS function

fn.dfdx     = @fhndfdx;      % Derivative wrt inputs (Jacobian)
fn.dfdp     = @fhndfdp;      % Derviative wrt parameters

fn.d2fdx2   = @fhnd2fdx2;    % Hessian wrt inputs
fn.d2fdxdp  = @fhnd2fdxdp;   % Hessian wrt inputs and parameters
fn.d2fdp2   = @fhnd2fdp2;    % Hessian wrt parameters.    

fn.d3fdx3   = @fhnd3fdx3;    % Third derivative wrt inputs.
fn.d3fdx2dp = @fhnd3fdx2dp;  % Third derivative wrt intputs, inputs and pars.
fn.d3fdxdp2 = @fhnd3fdxdp2;  % Third derivative wrt inputs, pars and pars. 
                             % dimensions = time, component, input,
                             % parameters
                         
                          
%% Various Parameters


y0 = [-1,1];                      
pars = [0.2; 0.2; 3];          

sigma = 0.5;                    

jitter = 0.2;                   
nrep = 50;

%% Observation times

tspan = 0:0.1:20;  
tfine = 0:0.05:20;
obs_pts{1} = 1:length(tspan);       
obs_pts{2} = 1:length(tspan);      
%obs_pts{2} = [];

%% Fitting parameters


%lambdas = 10.^(0:5);     
%lambdas = 1e4;

lambdas = 10.^(0:6);
lambda0 = 1;        


nknots = 21;
norder = 3;
nquad = 5;     

%% Profiling optimisation control

lsopts_out = optimset('DerivativeCheck','off','Jacobian','on',...
    'Display','iter','MaxIter',1000,'TolFun',1e-8,'TolX',1e-10);

lsopts_in = optimset('DerivativeCheck','off','Jacobian','on',...
    'Display','off','MaxIter',1000,'TolFun',1e-14,'TolX',1e-14,...
    'JacobMult',@SparseJMfun);

lsopts_other = optimset('DerivativeCheck','off','Jacobian','on',...
    'Display','on','MaxIter',1000,'TolFun',1e-14,'TolX',1e-14,...
    'JacobMult',@SparseJMfun);


%% Setting up Functional Data Objects

range = [min(tspan),max(tspan)];

knots_cell = cell(1,length(y0));
knots_cell(:) = {linspace(range(1),range(2),nknots)};

basis_cell = cell(1,length(y0)); 
Lfd_cell = cell(1,length(y0));

nbasis = zeros(length(y0),1);

bigknots = knots_cell{1};               
nbasis(1) = length(knots_cell{1}) + norder - 2;          

for i = 2:length(y0)
    bigknots = [bigknots knots_cell{i}];
    nbasis(i) = length(knots_cell{i}) + norder -2;
end

%quadvals = MakeQuadPoints(bigknots,nquad);   

quadvals = [knots_cell{1}' ones(nknots,1)/nknots];

for i = 1:length(y0)
    basis_cell{i} = MakeBasis(range,nbasis(i),norder,...  
        knots_cell{i},quadvals,1);                        
    Lfd_cell{i} = fdPar(basis_cell{i},1,lambda0);         
end

%% Calculate paths

odeopts = odeset('RelTol',1e-13);
[full_time,full_path] = ode45(odefn,tspan,y0,odeopts,pars);
[plot_time,plot_path] = ode45(odefn,tfine,y0,odeopts,pars);

%% Set up observations

Tcell = cell(1,size(full_path,2));
path = Tcell;

for i = 1:length(obs_pts)
    if ~isempty(obs_pts{i})
        Tcell{i} = full_time(obs_pts{i});
        path{i} = full_path(obs_pts{i},i);
    end
    tYcell{i} = plot_path(:,i);
    tTcell{i} = plot_time;
end

wts = [1 1];
for i = 1:length(path)
    if ~isempty(path{i})
        wts(i) = 1./sqrt(var(path{i}));
    else
        wts(i) = 1;
    end
end


% Smooth the data

DEfd = smoothfd_cell(path,Tcell,Lfd_cell);
coefs = getcellcoefs(DEfd);

coefs = lsqnonlin(@SplineCoefErr,coefs,[],[],...
    lsopts_other,basis_cell,tYcell,tTcell,[],lambdas(length(lambdas)),fn,[],pars);

DEfd = Make_fdcell(coefs,basis_cell);

% Start the simulations

parest = zeros([nrep length(lambdas) length(pars)]);
covest = zeros([nrep length(lambdas) length(pars) length(pars)]);
GNCovest = zeros([nrep length(lambdas) length(pars) length(pars)]);
errs = zeros([nrep length(lambdas) 2]);
errs_true = zeros([nrep length(lambdas) 2]);
sigmahat = zeros(nrep,length(lambdas));
df = zeros(3,nrep,length(lambdas));

for g = 1:nrep

    Ycell = path;
    for i = 1:length(path)
        if ~isempty(Ycell{i})
            Ycell{i} = path{i} + sigma*randn(size(path{i}));
        end
    end

    ppars = pars + jitter*randn(length(pars),1);
    disp(ppars')


    for h = 1:length(lambdas)
        disp([g h])

        lambda = lambdas(h) * wts;
        disp(lambda)
        
        %% Perform the Profiled Estimation

       [newpars,newDEfd_cell] = Profile_GausNewt(ppars,lsopts_out,DEfd,fn,...
           lambda,Ycell,Tcell,wts,[],lsopts_in);

       disp(newpars');

       parest(g,h,:) = newpars;

        %% Comparison with Smooth Using True Parameters

%         coefs = getcellcoefs(DEfd);
% 
%         [truecoefs,resnorm4] = lsqnonlin(@SplineCoefErr,coefs,[],[],...
%             lsopts_other,basis_cell,Ycell,Tcell,wts,lambda,fn,[],pars);
% 
%         trueDEfd_cell = Make_fdcell(truecoefs,basis_cell);
%         
%        [f,J] = ProfileErr(pars,trueDEfd_cell,fn,lambda,Ycell,Tcell,wts,[],lsopts_in);
        
% 
%         newpreds = eval_fdcell(Tcell,newDEfd_cell,0);
% 
%         new_err = cell(length(newpreds));
%         new_err_true = cell(length(newpreds));
%         for i = 1:length(path)
%             new_err{i} = wts(i)*(newpreds{i} - Ycell{i}).^2;
%             new_err_true{i} = wts(i)*(newpreds{i} - path{i}).^2;
%         end
% 
%         new_err = mean(cell2mat(new_err));
%         new_err_true = mean(cell2mat(new_err_true));
% 
%         truepreds = eval_fdcell(Tcell,trueDEfd_cell,0);
%         true_err = cell(length(truepreds));
%         true_err_true = cell(length(truepreds));
%         for i = 1:length(path)
%             true_err{i} = wts(i)*(truepreds{i} - Ycell{i}).^2;
%             true_err_true{i} = wts(i)*(truepreds{i} - path{i}).^2;
%         end
% 
%         true_err = mean(cell2mat(true_err));
%         true_err_true = mean(cell2mat(true_err_true));
%         
%         disp([new_err true_err new_err_true true_err_true]);
% 
%         errs(g,h,:) = [new_err true_err];
%         errs_true(g,h,:) = [new_err_true true_err_true];
        
        
%         figure(1)
%         devals_new = eval_fdcell(Tcell,newDEfd_cell);
%         devals_true = eval_fdcell(Tcell,trueDEfd_cell);
%         for i = 1:numel(path)
%             subplot(numel(path),1,i)
%             plot(Tcell{i},Ycell{i},'.')
%             hold on
%             plot(Tcell{i},path{i},'g')
%             plot(Tcell{i},devals_new{i})
%             plot(Tcell{i},devals_true{i},'r')
%             hold off
%         end
%         
%         pause

        %% Calculate Sample Information and Variance-Covariance Matrices


%         [dhYdY,dpdY,df(:,g,h)] = est_df(trueDEfd_cell,fn,Ycell,Tcell,wts,lambda,pars);
%         
%         
%         sigmahatt = make_sigma(trueDEfd_cell,Tcell,Ycell,0);
%         sigmahat(g,h) = sigmahatt(1,1);
% 
%         Cov = sigma*dpdY*dpdY';
% 
%         GNCovest(g,h,:,:) = sigma*inv(J'*J);
%         
%         covest(g,h,:,:) = Cov;

    end

    save 'fhn_newcolloc.mat'

end


