# Lab 2 – Xử lý Ảnh Số (Digital Image Processing)

# Mục đích
Notebook này được xây dựng cho Lab2 trong học phần *Xử lý ảnh số*. Nội dung áp dụng các kỹ thuật xử lý ảnh cơ bản và nâng cao, bao gồm:

- Biến đổi ảnh theo điểm ảnh
- Biến đổi ảnh trong miền tần số (Fourier)
- Lọc ảnh với bộ lọc thông thấp / thông cao
- Giao diện tương tác người dùng đơn giản qua dòng lệnh

#Nội dung chính

File `lab2_baitap_final.ipynb` bao gồm 4 phần chính:

#1. Xử lý điểm ảnh (Pixel-level)
Cung cấp menu các chức năng:
- **Gốc (I):** Hiển thị ảnh ban đầu
- **Grayscale (G):** Chuyển sang ảnh xám
- **Log (L):** Biến đổi log để làm rõ chi tiết vùng tối
- **Histogram Equalization (H):** Cân bằng mức sáng
- **Power-Law (C):** Biến đổi gamma để điều chỉnh độ tương phản

#2. Xử lý tần số (Frequency-level)
Các chức năng:
- **Fourier Transform (F):** Hiển thị phổ tần số
- **Lowpass Filter (L):** Lọc thông thấp Butterworth
- **Highpass Filter (H):** Lọc thông cao Butterworth

#3. So sánh kết quả
- Hiển thị hình ảnh gốc và ảnh đã xử lý
- So sánh histogram và chất lượng trực quan

#4. Giao diện chọn menu
- Cho phép người dùng nhập lựa chọn để thực hiện từng loại xử lý ảnh

Yêu cầu hệ thống

- Python 3.x
- Jupyter Notebook
- Thư viện cần cài:
  ```bash
  pip install numpy matplotlib pillow scipy scikit-image
  ```

#Hướng dẫn sử dụng

1. Mở Jupyter Notebook và load file `lab2_baitap_final.ipynb`.
2. Đảm bảo bạn có sẵn một ảnh đầu vào (file `.jpg` hoặc `.png`) và đã cập nhật đúng đường dẫn ảnh trong phần đầu notebook.
3. Chạy từng ô lệnh từ trên xuống dưới.
4. Khi được yêu cầu, nhập lựa chọn xử lý ảnh tương ứng để thực hiện thao tác (theo hướng dẫn trong menu).

## 📌 Lưu ý
Kết quả được chụp hình và để tại file ketqua
