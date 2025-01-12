clc
close all
clear all
% Read the 3D TIFF file
t = Tiff('Result.tiff', 'r');
info = imfinfo('Result.tiff');
num_slices = numel(info); % Number of slices

% Preallocate a 3D matrix
data = zeros(info(1).Height, info(1).Width, num_slices, 'like', imread('Result.tiff'));

% Loop through each slice
for i = 1:num_slices
    t.setDirectory(i);
    data(:, :, i) = t.read();
end
t.close();

volshow(data);
