pkg load image;

lena = imread('lena.png');
figure, imshow(lena), title('orig img, color');

lenaMono = rgb2gray(lena);
figure, imshow(lenaMono), title('orig img, mono');

h = fspecial('gaussian', [11 11], 4);
imshow(h, []);
figure, surf(h);

lenaSmooth = imfilter(lenaMono, h);
figure, imshow(lenaSmooth), title('smoothed');

% Method 1, shift left and right, and show diff images
lenaL = lenaSmooth;
lenaL(:, [1:(end-1)]) = lenaL(:, [2:end]);
lenaR = lenaSmooth;
lenaR(:, [2:(end)]) = lenaR(:, [1:(end-1)]);
lenaDiff = double(lenaR) - double(lenaL);
figure, imshow(lenaDiff, []), title('diff btwn l and r shifted img');

% Method 2, Canny edge detector
cannyEdges = edge(lenaMono, 'canny');
figure, imshow(cannyEdges, []), title('og edges');

cannyEdges = edge(lenaSmooth, 'canny');
figure, imshow(cannyEdges, []), title('smoothed edges');

% Method 3, Laplacian of Gaussian
cannyEdges = edge(lenaMono, 'log');
figure, imshow(cannyEdges, []), title('og edges');

cannyEdges = edge(lenaSmooth, 'log');
figure, imshow(cannyEdges, []), title('smoothed edges');



