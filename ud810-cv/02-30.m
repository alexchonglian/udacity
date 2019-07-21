noise = randn([1 1000]);
% [n, x] = hist(noise, [-3,-2,-1,0,1,2,3]);
[n, x] = hist(noise, linspace(-3, 3, 7))
disp([x; n]);
plot(x, n);