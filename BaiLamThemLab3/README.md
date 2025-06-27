# Thông tin ảnh sử dụng:
- `fruit.jpg`: ảnh trái cây gốc.
- `world_cup.jpg`: ảnh phong cảnh dùng cho các biến đổi hình học.

# Câu 1.8 – Chọn đối tượng khác (trái dâu)

Mục tiêu: Chọn trái dâu trong ảnh gốc `fruit.jpg` để áp dụng tiếp các biến đổi.  
Tọa độ dùng: `[500:850, 950:1250]`  

**Nhận xét**: Vị trí này cắt gọn vùng quả dâu rõ nét, phù hợp để áp dụng các phép biến đổi tiếp theo.

---

# Câu 1.9 – Tịnh tiến trái dâu

Nhận xét: Dâu được tịnh tiến nhẹ, nếu dịch nhiều hơn có thể gây mất một phần ảnh ở viền.

---

# Câu 1.10 – Thay đổi kích thước trái dâu

Nhận xét: Phóng to làm ảnh rõ chi tiết nhưng có thể bị mờ nếu nội dung ban đầu nhỏ. Thu nhỏ làm mất chi tiết nhưng nhẹ và nhanh hơn.

---

# Câu 1.11 – Xoay ảnh trái dâu

Xoay: 45 độ  
**Nhận xét**:  
- `reshape=True`: không cắt góc nhưng tạo vùng ảnh đen xung quanh.  
- `reshape=False`: giữ kích thước gốc nhưng bị cắt góc ảnh.

---

## Câu 1.12 – Dilation và Erosion trên trái dâu

**Thao tác**:
- Dilation size=(5,5)  
- Erosion size=(5,5)

**Nhận xét**:  
- Dilation làm ảnh dày và rõ nét hơn (phồng ra).  
- Erosion làm ảnh mảnh và mờ hơn (co lại).

---

# Câu 1.13 – Biến đổi hình học sóng (Cos và Sin)

Biến đổi ảnh `world_cup.jpg`:
- Sử dụng hàm `cos`: tạo hiệu ứng sóng nhẹ 
- Sử dụng hàm `sin`: hiệu ứng lượn sóng mạnh hơn
**Nhận xét**:  
- `cos` tạo biến dạng đều, mượt.  
- `sin` tạo hiệu ứng cong mềm mại rõ ràng hơn.
