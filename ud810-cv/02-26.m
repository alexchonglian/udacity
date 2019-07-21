% Blend two images
function output = blend(a, b, alpha)
    % TODO: Your code here; finally assign: output = <something>;
    output = alpha * a + (1-alpha) * b;
endfunction

% Test code:
dolphin = imread('dolphin.png');
bicycle = imread('bicycle.png');

result = blend(dolphin, bicycle, 0.75);
imshow(result); % note: will result in an error if blend() returns empty or incorrect value
