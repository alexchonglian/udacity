im = imread('dolphin.png');
noise = randn(size(dolphin)) .* 10;
imout = im + noise;
imshow(imout)