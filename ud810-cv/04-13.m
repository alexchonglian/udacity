% Explore edge options
pkg load image;

%% Load an image
img = imread('fall-leaves.png');  % also available: fall-leaves.png, peppers.png, mandrill.png
imshow(img);

%% TODO: Create a Gaussian filter
f = fspecial('gaussian', 21, 3);

%% TODO: Apply it, specifying an edge parameter (try different parameters)
smoothed = imfilter(img,f, 0);
%smoothed = imfilter(img,f, 255);
%smoothed = imfilter(img,f,'circular');
%smoothed = imfilter(img,f,'replicate');
%smoothed = imfilter(img,f,'symmetric')
imshow(smoothed);