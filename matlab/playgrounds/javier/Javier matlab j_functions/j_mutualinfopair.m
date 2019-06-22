function I = j_mutualinfopair(series1,series2)

%series1 = [4 0 2 0 1 0]';
%series2 = [1 0 2 0 1 5]';
%series2 = num2str([1 0 1 0 0 0]')
%series1 = ['a' 'a' 'a' 'a' 'a' 'a']'

%disp('start j_mutualinfopair')
series = [series1 series2];

%determine number of categories in each series
cat_count = j_count(series);
tcat=size(find(cat_count(:,2)),1);
ncat=size(find(cat_count(:,3)),1);
mcat=size(find(cat_count(:,4)),1);

%build count_matrix
count_matrix = zeros(tcat);
for n = 1:size(series,1)
    index1 = find(cat_count(:,1) == series(n,1),1);
    index2 = find(cat_count(:,1) == series(n,2),1);
%    disp([index1 index2])
    count_matrix(index1,index2)=count_matrix(index1,index2)+1;
end
%count_matrix

%remove cols and rows of zeros
col_keep=~all(count_matrix==0,1);
row_keep=~all(count_matrix==0,2);
count_matrix=count_matrix(row_keep,col_keep);

%calculte p and I
p = count_matrix./sum(sum(count_matrix));
I = 0;
for n = 1:ncat
    for m =1:mcat
       I= I + log2((p(n,m)/(sum(p(n,:))*sum(p(:,m))))^p(n,m));
    end
end
%count_matrix
%}




