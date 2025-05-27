import numpy as np
import imageio.v2 as iio
import matplotlib.pyplot as plt
import colorsys
import scipy.ndimage as sn

#BÀI 1: Lưu ảnh với 3 màu khác nhau (R, G, B)
img = iio.imread('bird.png')  # dùng 1 ảnh ví dụ

red = np.zeros_like(img)
red[:, :, 0] = img[:, :, 0]
iio.imwrite('bai1_red.png', red)

green = np.zeros_like(img)
green[:, :, 1] = img[:, :, 1]
iio.imwrite('bai1_green.png', green)

blue = np.zeros_like(img)
blue[:, :, 2] = img[:, :, 2]
iio.imwrite('bai1_blue.png', blue)

#BÀI 2: Hoán đổi giá trị các kênh màu (R->G, G->B, B->R)
swapped = np.zeros_like(img)
swapped[:, :, 0] = img[:, :, 2]  # B → R
swapped[:, :, 1] = img[:, :, 0]  # R → G
swapped[:, :, 2] = img[:, :, 1]  # G → B
iio.imwrite('bai2_swapped.png', swapped)

#BÀI 3: Chuyển ảnh sang hệ màu HSV và lưu 3 ảnh với H, S, V
def rgb_to_hsv_img(rgb_img):
    r = rgb_img[:, :, 0] / 255.0
    g = rgb_img[:, :, 1] / 255.0
    b = rgb_img[:, :, 2] / 255.0
    hsv = np.vectorize(colorsys.rgb_to_hsv)(r, g, b)
    return np.stack(hsv, axis=-1)

hsv_img = rgb_to_hsv_img(img)
iio.imwrite('bai3_H.png', (hsv_img[:, :, 0] * 255).astype(np.uint8))
iio.imwrite('bai3_S.png', (hsv_img[:, :, 1] * 255).astype(np.uint8))
iio.imwrite('bai3_V.png', (hsv_img[:, :, 2] * 255).astype(np.uint8))

# ===== BÀI 4: Chuyển HSV, thay đổi H và V, lưu lại
h = hsv_img[:, :, 0] / 3
s = hsv_img[:, :, 1]
v = hsv_img[:, :, 2] * 0.75

rgb_new = np.vectorize(colorsys.hsv_to_rgb)(h, s, v)
rgb_new = np.stack(rgb_new, axis=-1)
iio.imwrite('bai4_HV_changed.png', (rgb_new * 255).astype(np.uint8))

#BÀI 5: Sử dụng mean filter (5x5) để lọc ảnh xám
gray = iio.imread('bird.png', as_gray=True)
k = np.ones((5, 5)) / 25  # Kernel 5x5
mean_filtered = sn.convolve(gray, k).astype(np.uint8)
iio.imwrite('bai5_mean_filter.png', mean_filtered)
