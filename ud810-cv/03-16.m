%% load an image
img = imread('saturn.png');
imshow(img);

%% add some noise
noise_sigma = 25;
noise = randn(size(img)) .* noise_sigma;
noisy_img = img + noise;
imshow(noisy_img);

%% create a gaussian filter
filter_size = 11
filter_sigma = 2;
pkg load image;
filter = fspecial('gaussian', filter_size, filter_sigma);

smoothed = imfilter(noisy_img, filter);
imshow(smoothed);