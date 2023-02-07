clear all; clf;
load (' FRF data.mat');
X = x - mean (x); %(input) white noise
y = y - mean (y); %(output) Low pass filtered white noise
% (2nd LPF, fc = about 7%0 Hz)
fs = 25600;
nfft = fs * 0.5; %  d_f = 2 Hz
window = hann (nfft / 4);
noverlap = round (length (window) * 0.5);

[txy, f] = tfestimate(x, y, window, noverlap, nfft, fs);
figure (1); clf; subplot (211);
plot (f, 20 * log10 (abs (ty)), 'k', 'Linewidth', 1.3);
xlabel ('Frequency (Hz) '); ylabel ('magnitude (dB) ');
grid on; grid minor; box on;
xlim([0 5000]); ylim([-15 0]);
subplot (212);
plot (f, unwrap (angle (txy) * 180 / pi), 'k', 'Linewidth', 1.3);
xlabel ('Frequency (Hz) '); ylabel ('phase (degree)'); xlim ([O 5000]);
ylim([-80 0]); grid on; grid minor; box on;
figure(2); clf;
plot (real (txy (1:6200)), imag (ty (1:6200)), 'k', 'Linewidth', 1.3);
axis equal; grid on; grid minor; box on; xlabel ('Real'); ylabel ('Imaginary');
