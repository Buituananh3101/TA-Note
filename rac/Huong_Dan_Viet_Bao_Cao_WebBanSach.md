# HƯỚNG DẪN VIẾT BÁO CÁO ĐỒ ÁN MÔN HỌC / THỰC TẬP
**Dự án:** Website Bán Sách (WebBanSach)
**Công nghệ:** Frontend (ReactJS/TypeScript) - Backend (Java Spring Boot)

---

## 1. Cấu Trúc Tổng Quan Của Cuốn Báo Cáo
Một cuốn báo cáo đồ án phần mềm chuẩn thường gồm các phần sau:
1. **Trang bìa & Lời cảm ơn:** Thông tin sinh viên, giảng viên hướng dẫn.
2. **Mục lục, Danh mục hình ảnh, Danh mục bảng biểu.**
3. **Lời mở đầu:** Lý do chọn đề tài xây dựng Web bán sách.
4. **Chương 1: Tổng quan dự án & Cơ sở lý thuyết**
   - Giới thiệu bài toán (Website bán sách trực tuyến).
   - Các công nghệ sử dụng (ReactJS, Spring Boot, MySQL, v.v.).
5. **Chương 2: Phân tích và Thiết kế hệ thống**
   - Biểu đồ Use Case (Các chức năng của Admin, Khách hàng).
   - Sơ đồ cơ sở dữ liệu (ERD/Relational Database).
   - Các biểu đồ UML khác (Sequence Diagram, Activity Diagram).
6. **Chương 3: Hiện thực hệ thống** (Trọng tâm)
   - Hiện thực Backend (`webbansach_backend`).
   - Hiện thực Frontend (`webbansach_fontend`).
   - Giao diện và kết quả thử nghiệm.
7. **Kết luận và Hướng phát triển.**
8. **Tài liệu tham khảo.**

---

## 2. Hướng Dẫn Viết Phần Backend (Thư mục `webbansach_backend`)
Phần này tập trung vào cách hệ thống quản lý dữ liệu và cung cấp API. Bạn nên trình bày theo các ý sau:

### 2.1. Kiến trúc hệ thống Backend
- Mô tả Backend được xây dựng theo **kiến trúc MVC hoặc 3 lớp (3-tier architecture)**:
  - **Controller Layer (REST API):** Tiếp nhận Requests từ Frontend, trả về dữu liệu dạng JSON.
  - **Service Layer (Business Logic):** Chứa các logic nghiệp vụ phức tạp về tính toán, kiểm tra dữ liệu trước khi lưu (ví dụ: tính tổng tiền giỏ hàng, kiểm tra số lượng tồn kho của sách).
  - **Repository Layer (Data Access):** Thao tác với cơ sở dữ liệu (Database) thông qua Spring Data JPA hoặc Hibernate.
- *Tip: Hãy vẽ một sơ đồ kiến trúc khối đơn giản để đưa vào báo cáo.*

### 2.2. Thiết kế Cơ sở dữ liệu (Database)
- Chèn **Sơ đồ ERD** vào báo cáo. Giải thích các bảng chính và mối quan hệ:
  - Bảng `User` (Người dùng), `Role` (Quyền).
  - Bảng `Book` (Sách), `Category` (Thể loại sách), `Image` (Hình ảnh).
  - Bảng `Order` (Đơn hàng), `OrderDetail` (Chi tiết đơn hàng).
- Trình bày về quá trình Mapping các bảng vào hệ thống bằng các **Entity classes** (các class trong thư mục `entity`).

### 2.3. Thiết kế RESTful API
- Lập bảng danh sách các API quan trọng (Ví dụ: Danh sách API liên quan đến Sản phẩm, Giỏ hàng).
- Trình bày phương thức (GET, POST, PUT, DELETE), Endpoint (ví dụ: `/api/books`) và ý nghĩa chức năng.
- **Bảo mật (Security):** Nếu dự án dùng Spring Security & JWT, hãy dành 1 mục giải thích cơ chế Đăng ký / Đăng nhập, cấp phát Token và xác thực (Authentication/Authorization) phân quyền Admin/Customer.

---

## 3. Hướng Dẫn Viết Phần Frontend (Thư mục `webbansach_fontend`)
Phần này tập trung vào cách người dùng tương tác với hệ thống. Trình bày từ mô hình tổ chức code đến luồng chạy ứng dụng.

### 3.1. Kiến trúc và Tổ chức Component
- Ứng dụng xây dựng trên **ReactJS bằng TypeScript**.
- Giải thích cấu trúc thư mục (Folder structure):
  - `src/components`: Chứa các thành phần giao diện dùng chung (Navbar, Footer, Button...).
  - `src/layouts`: Chứa các bố cục trang và luồng chính (Ví dụ: `ChiTietSanPham`).
  - `src/model`: Chứa các định nghĩa kiểu dữ liệu (Interfaces/Classes như `Book.ts`, `CartItem.ts`).
  - `src/api`: (Nếu có) Các file cấu hình gọi Rest API bằng Axios / Fetch.
  
### 3.2. Quản lý Trạng thái (State Management)
- Nếu dùng **React Hooks** (`useState`, `useEffect`), giải thích cách bạn fetch dữ liệu khi component render.
- Nếu dùng Context API hoặc Redux (cho tính năng Giỏ hàng - Card), giải thích luồng cập nhật sản phẩm trong giỏ mà không cần reload trang.
- Đưa mã nguồn minh họa (snippet) ngắn về cách gọi API lấy danh sách sách hiển thị ra giao diện.

### 3.3. Các Luồng Nghiệp Vụ Chính (Kèm ảnh chụp màn hình)
Với mỗi luồng nghiệp vụ sau, hãy chèn **ảnh màn hình (screenshot)** của web thực tế và giải thích ngắn gọn:
1. **Trang chủ & Tìm kiếm sách:** (Hiển thị danh sách slide, carousel sản phẩm, thanh tìm kiếm).
2. **Trang chi tiết sản phẩm (`ChiTietSanPham.tsx`):** Trình bày thông tin chi tiết một cuốn sách, xem nhiều ảnh, thêm vào giỏ.
3. **Luồng Giỏ hàng & Thanh toán:** Mô tả từ lúc nhấn vòng "Thêm giỏ hàng", đến trang xác nhận, nhập địa chỉ và đặt hàng.
4. **Trang Đăng nhập / Đăng ký:** Luồng lấy thông tin đăng nhập gửi về JWT backend.
5. **Trang Quản trị (Admin) (Nếu có):** Quản lý thêm/xóa/sửa thông tin sách, duyệt đơn hàng.

---

## 4. Một Số Mẹo (Tips) Giúp Báo Cáo Điểm Cao
- **Tính thống nhất:** Code trong báo cáo (dùng font code như Courier New), dùng công cụ như *Carbon* hoặc Markdown snippet để show code cho đẹp. Không nên chụp ảnh màn hình của code mờ nhạt.
- **Có số liệu:** Đừng chỉ nói "Tìm kiếm nhanh", hãy nói "API tìm kiếm trả về kết quả trong thời gian ngắn...".
- **Không copy nguyên code vào:** Chỉ trích dẫn các đoạn code quan trọng nhất (như lõi xử lý giỏ hàng, bảo mật). Những đoạn code như Getter/Setter, import không được đưa vào tốn giấy.
- **Kết luận thực tế:** Trong phần "Kết luận", nên trung thực về những gì chưa làm được (ví dụ: chưa tích hợp thanh toán VNPay thực tế, mới làm hình thức COD) và đưa nó vào "Hướng phát triển tương lai".

---
*Hy vọng dàn ý này sẽ giúp bạn dễ dàng trong việc biên soạn báo cáo đồ án cho website WebBanSach của mình! Nếu cần hỗ trợ viết cụ thể một chương nào (như vẽ UML hay mô tả API chi tiết), bạn có thể yêu cầu thêm.*
