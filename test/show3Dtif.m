clc
close all
clear all
% Read the 3D TIFF file
t = Tiff('test3D_watershed.tiff', 'r');
info = imfinfo('test3D_watershed.tiff');
num_slices = numel(info); % Number of slices

% Preallocate a 3D matrix
data = zeros(info(1).Height, info(1).Width, num_slices, 'like', imread('output.tiff'));

% Loop through each slice
for i = 1:num_slices
    t.setDirectory(i);
    data(:, :, i) = t.read();
end
t.close();

volshow(data);
