pkg load image;

img = imread('shapes.png');
grays = rgb2gray(img);
edges = edge(grays, 'canny');

figure, imshow(img), title('orig');
figure, imshow(grays), title('grayscale');
figure, imshow(edges), title('edges');

[accum theta rho] = hough(edges);

figure, imagesc(theta, rho, accum), title('hough');

peaks = houghpeaks(accum, 100);

hold on;
plot(theta(peaks(:, 2)), rho(peaks(:, 1)), 'rs');
hold off;

size(peaks);

line_segs = houghlines(edges, theta, rho, peaks);

line_segs

figure, imagesc(theta, rho, accum), title('hough');
peaks = houghpeaks(accum, 100, 'Threshold', ceil(0.6 * max(accum(:))), 'NHoodSize', [5 5]);
hold on;
plot(theta(peaks(:, 2)), rho(peaks(:, 1)), 'rs');
hold off;

size(peaks);








