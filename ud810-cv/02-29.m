dolphin = imread('dolphin.png');
bicycle = imread('bicycle.png');

pkg load image;
imout = imabsdiff(dolphin, bicycle);
imshow(imout)