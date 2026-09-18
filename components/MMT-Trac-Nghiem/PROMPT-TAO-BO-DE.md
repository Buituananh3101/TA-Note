# Prompt tạo bộ đề mới

Copy phần trong khối dưới đây. Gửi kèm PDF đề, các tài liệu nguồn dùng để giải thích và file MAU-CAU-HOI.md của dự án. Thay tên file đầu ra và tên bộ đề theo ý bạn.

```text
Hãy chuyển file đề trắc nghiệm tôi gửi thành file Markdown UTF-8 để nạp vào dự án MMT-Trac-Nghiem hiện có.

Tên file đầu ra: chuong-2.md
Tên bộ đề: Chương 2 · [điền tên chủ đề]

Yêu cầu:
1. Chuyển đầy đủ tất cả câu hỏi và lựa chọn trong đề, giữ thứ tự và nội dung. Đánh số liên tục từ 1 theo thứ tự xuất hiện; đây là số câu gốc dùng trong danh sách câu sai. Nếu đề có mã câu riêng, giữ mã đó trong Lưu ý.
2. Lấy đáp án từ đáp án gốc hoặc các lựa chọn được đánh dấu/in đậm trong đề. Không tự đoán khi không xác định được đáp án: báo rõ câu cần tôi xác nhận trước khi hoàn tất bộ file có thể chấm.
3. Giải thích dễ hiểu, chỉ dựa vào tài liệu nguồn tôi gửi. Mỗi giải thích phải ghi tên tài liệu và số trang PDF tính từ 1. Không dùng Internet hoặc kiến thức ngoài nguồn để bổ sung.
4. Khi tài liệu nguồn không đủ căn cứ để giải thích đáp án, ghi đúng hai dòng:
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Không viết thêm giải thích cho câu đó.
5. Nếu đáp án gốc và tài liệu nguồn không khớp, giữ đáp án gốc để chấm, ghi rõ khác biệt trong Lưu ý và chỉ giải thích những gì nguồn thực sự có. Không âm thầm sửa đề hoặc đáp án.
6. Dùng đúng định dạng dưới đây. Mỗi câu có ít nhất hai lựa chọn; số ở Chọn phải bằng số chữ cái trong Đáp án. Số câu không trùng. Chỉ một tiêu đề # cho bộ đề, mỗi câu bắt đầu bằng ## Câu N.
7. Nội dung câu hỏi, lựa chọn, giải thích và nguồn là văn bản thuần, không dùng HTML. Có thể xuống dòng để nối tiếp cùng một trường, nhưng không dùng tiêu đề phụ trong câu. Nếu đề có hình hoặc công thức không thể biểu diễn chính xác bằng văn bản thuần, báo rõ để tôi quyết định; không bỏ hình rồi tự suy diễn câu hỏi.
8. Kiểm tra số câu, đầy đủ lựa chọn, đáp án thuộc các lựa chọn và Chọn khớp số đáp án. Trả lại file .md hoàn chỉnh để tôi đặt vào thư mục questions, kèm một dòng cấu hình để thêm vào QUESTION_FILES của index.html. Không tạo lại HTML và không nhúng câu hỏi vào HTML.

Định dạng ví dụ:

# Tên bộ đề

## Câu 1
Câu hỏi: Nội dung câu hỏi
Chọn: 1
A. Lựa chọn A
B. Lựa chọn B
C. Lựa chọn C
D. Lựa chọn D
Đáp án: B
Giải thích: Giải thích có căn cứ từ tài liệu nguồn.
Nguồn: Tên tài liệu.pdf — trang 12
Trang đề: 1
Lưu ý: Chỉ thêm trường này khi cần ghi chú.

## Câu 2
Câu hỏi: Nội dung câu hỏi chọn nhiều (Chọn 3)
Chọn: 3
A. Lựa chọn A
B. Lựa chọn B
C. Lựa chọn C
D. Lựa chọn D
Đáp án: A, C, D
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 2
```

Sau khi nhận file:

1. Đặt vào `questions/chuong-2.md`.
2. Trong `index.html`, thêm dòng sau vào mảng `QUESTION_FILES` (giữ dấu phẩy phân cách các mục):

```js
{ title: 'Chương 2 · Tên chủ đề', path: 'questions/chuong-2.md' },
```

3. Đẩy thay đổi lên GitHub, chờ website GitHub Pages cập nhật rồi tải lại trang và chọn bộ đề mới.
