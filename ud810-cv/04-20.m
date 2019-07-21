% Apply a median filter
pkg load image;

%% Read an image
img = imread('moon.png');  % also try: brooklyn-bridge.png, penny-farthing.png
imshow(img);

%% TODO: Add salt & pepper noise
noisy_img = imnoise(img, 'salt & pepper', 0.02);
imshow(noisy_img);

%% TODO: Apply a median filter (how is the result different compared to Gaussian smoothing?)
imout = medfilt2(noisy_img);
imshow(imout);