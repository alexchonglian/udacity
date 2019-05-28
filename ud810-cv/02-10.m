im = imread('dolphin.png'); %semicolon suppress printing result
%imgreen = im(:,:,2);
disp(size(im));
imshow(im);
%line([1 512], [256 256], 'color', 'r')
plot(im(256, :));
