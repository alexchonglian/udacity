% Color planes
img = imread('fruit.png');
imshow(img);

disp(size(img));

% TODO: Select a color plane, display it, inspect values from a row
red = img(:, :, 1);
line([1 500], [101 101]);
plot(red(101,:));
imshow(red);