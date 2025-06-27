Lab3 và bài tập làm thêm trong lab 3
Thư mục làm bài gồm các phần như sau:

lab3_biendoi_hinhhoc/
│
├── lab3_biendoi_hinhhoc.ipynb    # Notebook chính chứa toàn bộ bài làm
├── README.md                     # Mô tả nội dung bài thực hành
├── exercise/                     # Thư mục chứa ảnh gốc sử dụng trong bài
│   ├── colorful-ripe-tropical-fruits.jpg
│   ├── quang_ninh.jpg
│   └── pagoda.jpg
└── ketqua/                       # Chua ket qua
```



# Nội dung bài làm
# Câu 1 – Chọn quả kiwi và tịnh tiến
- Ảnh sử dụng: `colorful-ripe-tropical-fruits.jpg`
- Thao tác: chọn vùng quả kiwi, tịnh tiến sang phải 30 pixel
- Kết quả lưu vào file `kiwi_shifted.jpg`

# Câu 2 – Chọn quả đu đủ và quả dưa hấu, đổi màu
- Ảnh sử dụng: `colorful-ripe-tropical-fruits.jpg`
- Thao tác: chọn hai vùng tương ứng, đổi màu (âm bản)
- Kết quả hiển thị trực tiếp trên giao diện

# Câu 3 – Chọn ngọn núi và con thuyền, xoay ảnh
- Ảnh sử dụng: `quang_ninh.jpg`
- Thao tác: chọn 2 đối tượng, xoay mỗi vùng 45 độ
- Kết quả lưu vào file `quangninh_rotated.jpg`

# Câu 4 – Chọn ngôi chùa và phóng to
- Ảnh sử dụng: `pagoda.jpg`
- Thao tác: chọn vùng ngôi chùa, phóng to lên 5 lần
- Kết quả lưu vào file `pagoda_zoom.jpg`

# Câu 5 – Viết chương trình tạo menu
- Hiển thị menu với các lựa chọn:
  - Tịnh tiến (`T`)
  - Xoay (`X`)
  - Phóng to (`P`)
  - Thu nhỏ (`H`)
  - Coordinate Map (`C`)
- Khi người dùng chọn, chương trình hỏi muốn áp dụng trên ảnh nào từ 3 ảnh gốc trong thư mục `exercise` và thực hiện biến đổi tương ứng


- Sử dụng các thư viện cơ bản đã học:
  - `numpy`
  - `scipy.ndimage`
  - `imageio.v2`
  - `matplotlib.pyplot`
- Không sử dụng OpenCV hoặc các thư viện ngoài tài liệu thực hành
- Thực hiện trên môi trường Jupyter Notebook hoặc Google Colab
