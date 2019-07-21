dolphin = imread('dolphin.png');
bicycle = imread('bicycle.png');
avg1 = dolphin/2 + bicycle/2;
avg2 = (dolphin+bicycle)/2;
imshow(avg1);
imshow(avg2);