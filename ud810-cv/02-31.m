% Generate Gaussian noise
noise = randn([5 5 1000]);
[n x y] = hist2(noise, meshgrid(linspace(-3, 3, 7), linspace(-3, 3, 7)));
%disp([x; n]);
plot(x, n);

% TODO: Try generating other kinds of random numbers.
%       How about a 2D grid of random Gaussian values?