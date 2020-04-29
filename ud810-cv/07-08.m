% For Your Eyes Only
pkg load image;

frizzy = imread('frizzy.png');
froomer = imread('froomer.png');
imshow(frizzy);
imshow(froomer);

% TODO: Find edges in frizzy and froomer images

% TODO: Display common edge pixels
frizzy_edges = edge(rgb2gray(frizzy), 'canny');
froomer_edges = edge(rgb2gray(froomer), 'canny');
imshow(frizzy_edges);
imshow(froomer_edges);

imshow(frizzy_edges & froomer_edges);