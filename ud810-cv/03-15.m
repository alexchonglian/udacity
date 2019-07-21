pkg load image;
im = imread('dolphin.png');

hsize = 31;
sigma = 5;
h = fspecial('gaussian', hsize, sigma);

surf(h);
imagesc(h);
outim = imfilter(im, h);
imshow(outim);
