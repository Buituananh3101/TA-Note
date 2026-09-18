# MMT · Luyện trắc nghiệm

## Bộ dự án

- `index.html`: ứng dụng, giao diện và mã xử lý trong một file; không cần thư viện ngoài.
- `questions/chuong-1.md`: đầy đủ 66 câu hỏi, đáp án, giải thích và trang nguồn.
- `MAU-CAU-HOI.md`: mẫu định dạng để tạo thêm bộ đề.

## Chạy dự án trên GitHub Pages

GitHub lưu các file dự án; GitHub Pages phục vụ chúng thành trang web. `index.html` chỉ chứa giao diện và logic, không nhúng bất kỳ câu hỏi hay đáp án nào. Khi bạn chọn một bộ đề, ứng dụng tải file `.md` riêng qua đường dẫn tương đối.

Đưa nội dung folder này vào vị trí bạn dùng để xuất bản GitHub Pages. Giữ `index.html` và thư mục `questions` cạnh nhau. Nếu đặt cả folder trong một website hiện có, mở URL trỏ đến folder đó. Các đường dẫn tương đối hoạt động cả khi website nằm dưới đường dẫn tên repository.

Bộ dự án không cần npm, bước build hoặc thư viện ngoài. Sau khi thay đổi câu hỏi trong `.md` và đẩy bản mới lên GitHub, tải lại trang khi bản xuất bản đã cập nhật.

Mở URL website GitHub Pages để làm bài; trang xem mã nguồn của repository không phải trang chạy ứng dụng. Giao diện vẫn dùng được trên máy tính và điện thoại.

### Các file

| File | Vai trò |
| --- | --- |
| `index.html` | Giao diện, xử lý chấm bài và danh sách đường dẫn QUESTION_FILES |
| `questions/chuong-1.md` | Toàn bộ dữ liệu 66 câu Chương 1 |
| `MAU-CAU-HOI.md` | Mẫu cấu trúc một bộ câu hỏi |
| `PROMPT-TAO-BO-DE.md` | Prompt dùng lại khi gửi đề mới cho AI |
| `README.md` | Hướng dẫn sử dụng |

### Làm bài

1. Chọn bộ đề và Làm toàn bộ hoặc 20 câu ngẫu nhiên.
2. Câu chọn một được chấm ngay khi chạm. Câu chọn nhiều được chấm khi chọn đủ số ý; trước khi đủ có thể chạm lại để bỏ chọn.
3. Xem đáp án và giải thích ngay dưới câu vừa làm. Câu đã chấm được khóa trong lượt đó.
4. Khi làm đủ, kết quả và ô câu sai tự hiện. Có thể bấm Xem kết quả bất cứ lúc nào.
5. Sao chép danh sách câu sai: chỉ gồm số câu gốc, ví dụ `2, 9, 25`, kể cả khi làm ngẫu nhiên.

Mỗi câu đúng hoàn toàn tính 1 câu, không áp dụng trọng số mức độ của PDF. Câu chưa trả lời hiển thị riêng, không tính là câu sai. Hãy sao chép kết quả trước khi tải lại hoặc bắt đầu lượt mới.

## Thêm một bộ câu hỏi

### Cách 1 — chọn file, không sửa code

Trong màn hình đầu, mở **Thêm bộ câu hỏi .md** → **Chọn file .md từ thiết bị**. Chọn file đúng định dạng, bộ đề sẽ xuất hiện trong danh sách. Nút này cũng dùng để nạp bản Chương 1 bạn vừa sửa khi đang mở HTML trực tiếp.

### Cách 2 — khai báo đường dẫn trong index.html

1. Đặt file, ví dụ `chuong-2.md`, vào thư mục `questions`.
2. Tìm `const QUESTION_FILES` trong `index.html`, thêm một dòng:

```js
const QUESTION_FILES = [
  { title: 'Chương 1 · Tổng quan về Mạng máy tính và Internet', path: 'questions/chuong-1.md' },
  { title: 'Chương 2 · Ethernet', path: 'questions/chuong-2.md' },
];
```

3. Mở trang qua máy chủ HTTP/HTTPS. Chọn bộ đề trong danh sách để tải file.

Đường dẫn tương đối tính từ `index.html`; tên file phân biệt chữ hoa và chữ thường. Giữ các đường dẫn dưới dạng `questions/chuong-2.md` để chạy được dưới đường dẫn repository. Mục đầu tiên trong QUESTION_FILES là bộ đề mặc định. Mỗi file được tải với `cache: no-store`. Không có bộ câu hỏi nhúng dự phòng: thiếu file hoặc sai đường dẫn sẽ hiện lỗi thay vì dùng dữ liệu cũ trong HTML.

Để xem thử trên máy trước khi đẩy lên GitHub, chạy máy chủ web trong thư mục dự án, ví dụ `python -m http.server 8000`, rồi mở `http://localhost:8000`. Mở trực tiếp bằng `file://` thường không tải được file lân cận; lúc đó có thể dùng nút Chọn file .md.

Có thể nhập đường dẫn ngay trong giao diện để nạp tạm một bộ đề, không cần sửa danh sách. Đường dẫn khác tên miền cần máy chủ đó cho phép CORS.

## Quy ước định dạng Markdown

Xem `MAU-CAU-HOI.md`. File phải được lưu bằng UTF-8:

- Dòng `# Tên bộ đề` là tiêu đề.
- Mỗi câu bắt đầu bằng `## Câu N`. N là số nguyên dương, không trùng trong bộ đề, giữ nguyên khi làm ngẫu nhiên.
- Trường `Chọn` bằng số đáp án đúng; câu chọn một là 1, câu chọn ba là 3.
- Lựa chọn dùng `A.`, `B.`, `C.`, `D.`; có thể thêm chữ cái khác.
- `Đáp án: A, C, D` ghi tập đáp án dùng để chấm.
- `Giải thích` và `Nguồn` bắt buộc. Nếu tài liệu không đủ căn cứ, dùng chính xác `Giải thích: Không có trong tài liệu nguồn.` và `Nguồn: Không có`.
- `Lưu ý` và `Trang đề` không bắt buộc.
- Nội dung được hiển thị như văn bản thuần; không chạy HTML hoặc JavaScript từ file đề, không hỗ trợ hình ảnh/công thức Markdown ở phiên bản này.
- Làm toàn bộ sắp xếp theo số câu gốc; ngẫu nhiên xáo trộn toàn bộ ngân hàng, lấy 20 câu không trùng, không dùng mức độ. Nếu bộ có ít hơn 20 câu, lấy toàn bộ và hiển thị đúng số lượng.

Sau này bạn có thể gửi một PDF đề khác và yêu cầu: “Chuyển thành Markdown đúng mẫu của dự án MMT-Trac-Nghiem; giữ thứ tự đề, đáp án theo đề; giải thích chỉ dựa vào các tài liệu nguồn tôi gửi; không có thì ghi Không có trong tài liệu nguồn.”

## Căn cứ dữ liệu Chương 1

Câu hỏi và đáp án được lấy từ **MMT - 02 - Ch01 - Trắc nghiệm chương 1 và đáp án.pdf**, 10 trang. PDF không đánh số câu nên bộ này đánh liên tục từ 1 đến 66 theo thứ tự xuất hiện, giữ nguyên lựa chọn và đáp án in đậm.

Đã đối chiếu với các PDF nguồn được cung cấp:

- MMT - 01 - Ch00 - d. Hệ cơ số và chuyển đổi giữa các hệ cơ số.pdf
- MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf
- MMT - 04 - Ch02 - Công nghệ Ethernet.pdf
- MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf
- MMT - 08 - Ch03 - Giao thức Internet.pdf

49 câu có giải thích và trang nguồn; 17 câu không đủ căn cứ giải thích trong các bài giảng được cung cấp, chỉ ghi thông báo thiếu nguồn. Số trang là số trang PDF, tính từ 1. Các PDF nguồn không được chép kèm dự án; tên file và số trang giúp bạn mở tài liệu đang có để đối chiếu.

Các câu 21, 26, 48 có ghi chú về khác biệt giữa đề và cách viết/phân nhóm trong slide. Ứng dụng vẫn giữ đáp án in đậm của đề khi chấm, không âm thầm sửa đáp án. Phần giải thích mô tả đúng tài liệu được cung cấp, không phải kiểm định độc lập mọi kiến thức trong slide.
