Bài 1: Lưu ảnh với 3 màu khác nhau (R, G, B) Đọc ảnh màu bird.png vào mảng img.

Tạo 3 ảnh mới, mỗi ảnh chỉ giữ lại một kênh màu đỏ, xanh lá, hoặc xanh dương, các kênh còn lại bằng 0.

Ví dụ: Ảnh red giữ kênh đỏ, 2 kênh còn lại được gán giá trị 0 → ảnh chỉ còn màu đỏ.

Lưu từng ảnh ra file tương ứng: bai1_red.png, bai1_green.png, bai1_blue.png.

Mục đích: Tách riêng từng kênh màu cơ bản từ ảnh gốc.

Bài 2: Hoán đổi giá trị các kênh màu (R→G, G→B, B→R) Tạo ảnh mới swapped có cùng kích thước với ảnh gốc.

Gán kênh đỏ của ảnh mới bằng kênh xanh dương của ảnh gốc.

Kênh xanh lá ảnh mới bằng kênh đỏ ảnh gốc.

Kênh xanh dương ảnh mới bằng kênh xanh lá ảnh gốc.

Lưu ảnh hoán đổi màu ra bai2_swapped.png.

Mục đích: Thay đổi thứ tự kênh màu để tạo hiệu ứng màu mới cho ảnh.

Bài 3: Chuyển ảnh sang hệ màu HSV và lưu 3 ảnh riêng biệt H, S, V Viết hàm rgb_to_hsv_img chuyển từng pixel từ RGB sang HSV.

Bình thường RGB có 3 kênh đỏ, xanh lá, xanh dương; HSV gồm Hue (màu sắc), Saturation (độ bão hòa), Value (độ sáng).

Dùng colorsys.rgb_to_hsv chuyển đổi màu cho từng pixel.

Kết quả trả về ảnh HSV có 3 kênh tương ứng.

Lưu riêng từng kênh H, S, V thành 3 file ảnh bai3_H.png, bai3_S.png, bai3_V.png (mỗi ảnh biểu diễn kênh tương ứng).

Mục đích: Phân tách ảnh theo hệ màu HSV để phân tích hoặc xử lý riêng biệt từng thành phần màu.

Bài 4: Chuyển ảnh sang HSV, thay đổi kênh H và V, sau đó chuyển lại RGB và lưu ảnh Dùng ảnh HSV đã có từ Bài 3.

Thay đổi kênh Hue (H) bằng cách chia cho 3 để thay đổi sắc độ.

Giảm cường độ sáng Value (V) xuống 75% (nhân với 0.75).

Giữ nguyên kênh Saturation (S).

Chuyển ảnh HSV mới về lại RGB bằng colorsys.hsv_to_rgb.

Lưu ảnh RGB mới thành file bai4_HV_changed.png.

Mục đích: Thực hiện biến đổi màu sắc và độ sáng ảnh trong không gian HSV để tạo hiệu ứng thay đổi màu.

Bài 5: Sử dụng bộ lọc trung bình (mean filter 5x5) để lọc ảnh xám Đọc ảnh gốc bird.png dưới dạng ảnh xám (grayscale).

Tạo kernel lọc trung bình kích thước 5x5 với các phần tử đều bằng 1/25.

Dùng hàm scipy.ndimage.convolve để áp dụng bộ lọc trung bình lên ảnh xám.

Bộ lọc trung bình giúp làm mịn ảnh, giảm nhiễu.

Lưu ảnh kết quả ra bai5_mean_filter.png.

Mục đích: Lọc làm mịn ảnh xám bằng kỹ thuật lọc trung bình để giảm nhiễu hoặc làm mềm ảnh.
