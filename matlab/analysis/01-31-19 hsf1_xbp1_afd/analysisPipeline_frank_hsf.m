%% Load Data
rawImageFilePath = "/Users/sean/code/wormAnalysis/matlab/sean/analysis/01-31-19 hsf1_afd/data/2018_11_29_hsf1_afd.tif";
I = loadIndexer("/Users/sean/code/wormAnalysis/matlab/sean/analysis/01-31-19 hsf1_afd/data/indexer.csv");
fig_directory = "/Users/sean/code/wormAnalysis/matlab/sean/analysis/01-31-19 hsf1_afd/figures";

hd233_idx = I.ImgFrame(I.Lambda=="410" & I.Strain == "HD233") / 3;
say179_idx = I.ImgFrame(I.Lambda=="410" & I.Strain == "SAY179") / 3;
say148_idx = I.ImgFrame(I.Lambda=="410" & I.Strain == "SAY148") / 3;

[rawImageDirectory, ~, ~] = fileparts(rawImageFilePath);
allImages = loadTiffImageStack(rawImageFilePath);

%% Split Image Stacks
im_TL_raw  = allImages(:,:,I.ImgFrame(I.LambdaGroup == "TL/470/410" & I.SetFrame == 1));
im_470_raw = allImages(:,:,I.ImgFrame(I.LambdaGroup == "TL/470/410" & I.SetFrame == 2));
im_410_raw = allImages(:,:,I.ImgFrame(I.LambdaGroup == "TL/470/410" & I.SetFrame == 3));

%% Process Images

% Subtract medians
im_470 = subtractMedians(im_470_raw);
im_410 = subtractMedians(im_410_raw);

% Segment Pharynx
seg_470 = segmentPharynx(im_470, 0);
seg_410 = segmentPharynx(im_410, 0);

%% Measure Intensities
% Calculate Midlines
LRBounds_470 = double(getLeftRightBounds(seg_470));
LRBounds_410 = double(getLeftRightBounds(seg_410));

midlines_470 = calculateMidlines(im_TL_raw, seg_470, im_470, 0);
midlines_410 = calculateMidlines(im_TL_raw, seg_410, im_410, 0);

% Measure under midlines
INTERP_METHOD = 'bilinear';
PROFILE_LENGTH = 1000;

[i_470, ~, scaledLRBounds_470] = measureAndTrim(...
    im_470, midlines_470, LRBounds_470, PROFILE_LENGTH);
[i_410, ~, scaledLRBounds_410] = measureAndTrim(...
    im_410, midlines_410, LRBounds_410, PROFILE_LENGTH);

%% Register Midlines
[reg_i410, reg_i470, warp_470, resampled_intensity, fdObjs] = ...
    ChannelRegister(i_410, i_470, 100);

%% Transforms
R_ = i_410 ./ i_470;
oxd_ = ja_oxd(R_);
E_ = ja_E(oxd_);

%%
rm_410 = regionMeans(i_410(:,hd233_idx));

%% Plots

% Plot Means According to Strain
% I_410
figure;
hold on;
plot(mean(i_410(:,hd233_idx), 2));
plot(mean(i_410(:,say179_idx), 2));
plot(mean(i_410(:,say148_idx), 2));
title('Mean I_{410} by Strain');
legend('HD233', 'SAY179', 'SAY148');
hold off;
export_fig(fullfile(fig_directory, "i410.pdf"));


% I_470
figure;
hold on;
plot(mean(i_410(:,hd233_idx), 2));
plot(mean(i_410(:,say179_idx), 2));
plot(mean(i_410(:,say148_idx), 2));
title('Mean I_{470} by Strain');
legend('HD233', 'SAY179', 'SAY148');
hold off;
export_fig(fullfile(fig_directory, "i470.pdf"));

% R
figure;
hold on;
plot(mean(R_(:,hd233_idx), 2));
plot(mean(R_(:,say179_idx), 2));
plot(mean(R_(:,say148_idx), 2));
title('Mean R by Strain');
legend('HD233', 'SAY179', 'SAY148');
hold off;
export_fig(fullfile(fig_directory, "R.pdf"));

% OxD
figure;
hold on;
plot(mean(oxd_(:,hd233_idx), 2));
plot(mean(oxd_(:,say179_idx), 2));
plot(mean(oxd_(:,say148_idx), 2));
title('Mean OxD by Strain');
legend('HD233', 'SAY179', 'SAY148');
hold off;
export_fig(fullfile(fig_directory, "OxD.pdf"));

% E
figure;
hold on;
plot(mean(E_(:,hd233_idx), 2));
plot(mean(E_(:,say179_idx), 2));
plot(mean(E_(:,say148_idx), 2));
title('Mean E by Strain');
legend('HD233', 'SAY179', 'SAY148');
hold off;
export_fig(fullfile(fig_directory, "E.pdf"));