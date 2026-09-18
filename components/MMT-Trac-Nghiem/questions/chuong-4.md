# Chương 4 · Tầng giao vận (Transport Layer – TCP/UDP)

Bộ đề: 60 câu; số câu được đánh liên tục theo thứ tự từ trên xuống trong PDF đề gốc (form Eduso).
Đáp án: vì không có PDF bài giảng chương 4 được cung cấp, đáp án và giải thích được suy luận dựa trên kiến thức chuẩn về tầng Giao vận, giao thức TCP (RFC 793) và UDP (RFC 768) theo giáo trình mạng máy tính phổ biến (CCNA/Cisco Networking Academy). Mục "Nguồn" vì vậy ghi "Không có" cho toàn bộ câu.
Quy tắc riêng cho câu dạng điền từ/chọn từ đúng chính tả: nếu câu hỏi thực chất là kiểm tra chính tả của một thuật ngữ tiếng Anh (các phương án chỉ khác nhau ở cách viết), đáp án chỉ có 1 lựa chọn viết đúng chính tả, phần giải thích chỉ nêu ngắn gọn cách nhận diện (so sánh cách viết với thuật ngữ chuẩn).
Chấm điểm: mỗi câu đúng hoàn toàn tính 1 câu, không tính trọng số mức độ (Nhận biết/Thông hiểu/Vận dụng) của bảng gốc.

## Câu 1
Câu hỏi: UDP và TCP là các giao thức nằm ở tầng giao vận?
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: TCP và UDP là hai giao thức chính hoạt động ở tầng Giao vận (Transport Layer) trong cả mô hình OSI lẫn TCP/IP.
Nguồn: Không có
Trang đề: 1

## Câu 2
Câu hỏi: Các ứng dụng trao đổi dữ liệu giữa hai máy đều liên quan tới số hiệu cổng tầng giao vận
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Số hiệu cổng (port number) dùng để xác định ứng dụng/tiến trình cụ thể trên máy, nên mọi trao đổi dữ liệu giữa ứng dụng đều gắn với một cặp cổng nguồn – cổng đích.
Nguồn: Không có
Trang đề: 1

## Câu 3
Câu hỏi: Tầng giao vận đảm bảo dữ liệu có thể được tập hợp lại một cách chính xác ở bên nhận bằng các quá trình phân mảnh (hoặc phân đoạn) và tập hợp lại?
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Tầng Giao vận phân đoạn (segment) dữ liệu ở bên gửi và tập hợp lại (reassemble) đúng thứ tự ở bên nhận, đây là một trong các chức năng cơ bản của tầng này.
Nguồn: Không có
Trang đề: 1

## Câu 4
Câu hỏi: Địa chỉ Default Gateway là một thành phần của Socket?
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Socket là sự kết hợp giữa địa chỉ IP và số hiệu cổng của một ứng dụng; Default Gateway là địa chỉ IP của thiết bị định tuyến, không phải thành phần của socket.
Nguồn: Không có
Trang đề: 1

## Câu 5
Câu hỏi: Phát biểu nào sau đây (tầng giao vận) là sai:
Chọn: 1
A. Port dùng để kết nối Client/Server
B. Port xác định ứng dụng truyền/nhận dữ liệu
C. Port có giá trị từ 1 đến 1023
D. Port được dùng cho TCP và UDP
Đáp án: C
Giải thích: Số hiệu cổng có dải giá trị từ 0 đến 65535 (16-bit), trong đó 0–1023 chỉ là dải cổng "well-known"; phát biểu giới hạn toàn bộ port chỉ từ 1–1023 là sai.
Nguồn: Không có
Trang đề: 1

## Câu 6
Câu hỏi: Port mặc định của HTTP server là:
Chọn: 1
A. TCP/80
B. TCP/23
C. UDP/25
D. UDP/110
Đáp án: A
Giải thích: HTTP dùng TCP làm giao thức giao vận và cổng mặc định là 80.
Nguồn: Không có
Trang đề: 1

## Câu 7
Câu hỏi: Phát biểu nào dưới đây là đúng với số hiệu cổng (port number):
Chọn: 1
A. Địa chỉ của một ứng dụng trên internet
B. Địa chỉ của một máy tính trên internet
C. Địa chỉ của một ứng dụng trên một máy tính
D. Liên kết với giao thức tầng Giao vận để xác định một ứng dụng
Đáp án: C
Giải thích: Số hiệu cổng dùng để xác định ứng dụng/tiến trình cụ thể đang chạy trên một máy tính (host); việc định vị máy tính trên mạng là nhiệm vụ của địa chỉ IP, không phải của port.
Nguồn: Không có
Trang đề: 1

## Câu 8
Câu hỏi: Để phát hiện lỗi trong khi truyền segment ở tầng giao vận, người ta sử dụng kỹ thuật:
Chọn: 1
A. Số thứ tự
B. Số thứ tự ghi nhận
C. Bộ định thời
D. Checksum
Đáp án: D
Giải thích: Checksum là trường trong header TCP/UDP dùng để kiểm tra tính toàn vẹn dữ liệu, giúp phát hiện lỗi trong quá trình truyền.
Nguồn: Không có
Trang đề: 2

## Câu 9
Câu hỏi: Giao thức tầng giao vận nào sau đây được sử dụng trong mạng?
Chọn: 1
A. TCP và FTP
B. UDP và HTTP
C. TCP và UDP
D. HTTP và FTP
Đáp án: C
Giải thích: TCP và UDP là hai giao thức thuộc tầng Giao vận; FTP và HTTP là giao thức tầng Ứng dụng nên các phương án còn lại đều trộn lẫn sai tầng.
Nguồn: Không có
Trang đề: 2

## Câu 10
Câu hỏi: Các giao thức tầng giao vân xử lý vấn đề nào sau đây?
Chọn: 1
A. Giao tiếp giữa ứng dụng với ứng dụng
B. Giao tiếp giữa tiến trình với tiến trình
C. Giao tiếp giữa node với node
D. Giao tiếp giữa con người với con người
Đáp án: B
Giải thích: Nhờ số hiệu cổng, tầng Giao vận thiết lập giao tiếp giữa các tiến trình (process-to-process) cụ thể chạy trên các máy, chứ không chỉ giữa hai thiết bị (node) nói chung.
Nguồn: Không có
Trang đề: 2

## Câu 11
Câu hỏi: Điểm truy cập dịch vụ ở tầng giao vận có tên là?
Chọn: 1
A. Port
B. Pipe
C. Node
D. Protocol
Đáp án: A
Giải thích: Điểm truy cập dịch vụ (Service Access Point) ở tầng Giao vận chính là số hiệu cổng (port).
Nguồn: Không có
Trang đề: 2

## Câu 12
Câu hỏi: Chức năng của tầng giao vận:
Chọn: 1
A. Đảm bảo các yêu cầu truyền dữ liệu qua các phương tiện vật lý
B. Mã hóa dữ liệu để bảo mật thông tin trên đường tuyền
C. Thực hiện việc tạo luồng dữ liệu kết nối giữa các đầu cuối
D. Nén dữ liệu để việc truyền qua mạng nhanh hơn
Đáp án: C
Giải thích: Tầng Giao vận có nhiệm vụ thiết lập luồng truyền dữ liệu end-to-end giữa ứng dụng nguồn và đích; truyền qua phương tiện vật lý thuộc tầng Vật lý, còn mã hóa/nén không phải chức năng cốt lõi của tầng này.
Nguồn: Không có
Trang đề: 2

## Câu 13
Câu hỏi: Ưu điểm của dịch vụ không kết nối (Connectionless service) khi so sánh với dịch vụ hướng kết nối (Connection-oriented service) ở tầng giao vận là
Chọn: 1
A. Giải quyết tắc nghẽn tốt hơn
B. Chất lượng dịch vụ có thể được đảm bảo
C. Không mất thời gian thiết lập và quản lý kết nối
D. Độ tin cậy cao
Đáp án: C
Giải thích: Dịch vụ không kết nối (như UDP) gửi dữ liệu ngay mà không cần bắt tay thiết lập kết nối trước, nên tiết kiệm thời gian và tài nguyên so với dịch vụ hướng kết nối.
Nguồn: Không có
Trang đề: 2

## Câu 14
Câu hỏi: Nhiệm vụ nào dưới đây là của các tầng giao vận?
Chọn: 1
A. Cung cấp quyền truy cập mạng
B. Phân tách các luồng dữ liệu
C. Xác định đường đi tốt nhất để chuyển tiếp gói
D. Dịch địa chỉ IP riêng sang địa chỉ IP công cộng
Đáp án: B
Giải thích: Phân tách (ghép kênh) các luồng dữ liệu của nhiều ứng dụng khác nhau là nhiệm vụ của tầng Giao vận; truy cập mạng thuộc tầng Network Access, định tuyến và NAT thuộc tầng Mạng.
Nguồn: Không có
Trang đề: 3

## Câu 15
Câu hỏi: Thông tin nào dưới đây KHÔNG có trong tiêu đề của hai giao thức cơ bản ở tầng giao vận?
Chọn: 1
A. Sequence number
B. Checksum
C. Source port
D. Destination port
Đáp án: A
Giải thích: Checksum, Source port và Destination port có mặt trong cả header TCP và UDP; riêng Sequence number chỉ có trong header TCP, không có trong header UDP.
Nguồn: Không có
Trang đề: 3

## Câu 16
Câu hỏi: Dải số hiệu cổng thông dụng được sử dụng trong tầng giao vận (TCP và UDP) là:
Chọn: 1
A. 0 – 255
B. 0 – 1023
C. 256 – 1023
D. 1024 - 49151
Đáp án: B
Giải thích: Dải cổng "well-known ports" (cổng thông dụng do IANA quy định cho các dịch vụ phổ biến) là từ 0 đến 1023.
Nguồn: Không có
Trang đề: 3

## Câu 17
Câu hỏi: Ở tầng giao vận, socket là:
Chọn: 1
A. Sự kết hợp giữa địa chỉ IP, số hiệu cổng và giao thức tầng ứng dụng
B. Sự kết hợp giữa địa chỉ IP, số hiệu mạng và giao thức tầng giao vận
C. Sự kết hợp giữa địa chỉ IP, số hiệu cổng và giao thức tầng giao vận
D. Sự kết hợp giữa địa chỉ IP, số hiệu cổng thông dụng và giao thức tầng ứng dụng
Đáp án: C
Giải thích: Socket được định nghĩa là bộ ba địa chỉ IP + số hiệu cổng + giao thức tầng Giao vận (TCP hoặc UDP), dùng để định danh duy nhất một phiên giao tiếp.
Nguồn: Không có
Trang đề: 3

## Câu 18
Câu hỏi: Loại số hiệu cổng nào được IANA chỉ định cho các dịch vụ và ứng dụng thường được sử dụng?
Chọn: 1
A. Private port
B. Registered port
C. Well-known port
D. Dynamic port
Đáp án: C
Giải thích: Well-known port (0–1023) là dải cổng được IANA gán cố định cho các dịch vụ phổ biến như HTTP, FTP, DNS.
Nguồn: Không có
Trang đề: 3

## Câu 19
Câu hỏi: Tầng giao vận sử dụng cổng 53 để mô tả giao thức nào?
Chọn: 1
A. SNMP
B. SMTP
C. DHCP
D. DNS
Đáp án: D
Giải thích: Cổng 53 (cả TCP và UDP) được gán cho dịch vụ phân giải tên miền DNS.
Nguồn: Không có
Trang đề: 4

## Câu 20
Câu hỏi: Nhiệm vụ chính trong tầng giao vận (Chọn 3)
Chọn: 3
A. Theo dõi giao tiếp
B. Phân mảnh (hoặc phân đoạn) dữ liệu
C. Xác định các ứng dụng
D. Kiểm soát luồng dữ liệu
Đáp án: A, B, C
Giải thích: Ba nhiệm vụ nền tảng, chung cho tầng Giao vận (áp dụng cho cả TCP lẫn UDP) là theo dõi từng phiên giao tiếp, phân đoạn/tập hợp dữ liệu và xác định ứng dụng qua số hiệu cổng; kiểm soát luồng chỉ là chức năng bổ sung riêng của TCP, không phải nhiệm vụ chung của mọi giao thức giao vận.
Nguồn: Không có
Trang đề: 4

## Câu 21
Câu hỏi: Các phát biểu nào sau đây liên quan tới số hiệu cổng (Chọn 3)
Chọn: 3
A. Mỗi số hiệu cổng được hiển thị bằng một số nguyên không dấu
B. Mỗi số hiệu cổng có độ dài 16-bit do ICANN cấp
C. Mỗi số hiệu cổng có độ dài 16-bit do IANA cấp
D. Số hiệu cổng được dùng để xác định một ứng dụng
Đáp án: A, C, D
Giải thích: Số hiệu cổng là số nguyên không dấu 16-bit, do IANA (không phải ICANN) quản lý cấp phát, và dùng để xác định ứng dụng cụ thể trên một máy.
Nguồn: Không có
Trang đề: 4

## Câu 22
Câu hỏi: Dữ liệu được đóng gói trong tầng Giao vận KHÔNG được gọi là (Chọn 3)
Chọn: 3
A. Segment hoặc Datagrama
B. Segmen hoặc Datagram
C. Segment hoặc Datagram
D. Segmen hoặc Datagrama
Đáp án: A, B, D
Giải thích: Đây là câu dạng chọn từ đúng chính tả: tên chuẩn của đơn vị dữ liệu tầng Giao vận là "Segment" (TCP) hoặc "Datagram" (UDP), chỉ đúng ở phương án C; ba phương án còn lại đều sai chính tả (Segmen thiếu "t", Datagrama thừa "a") nên không phải tên gọi đúng.
Nguồn: Không có
Trang đề: 4

## Câu 23
Câu hỏi: UDP quản lý và theo dõi thứ tự Datagram
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: UDP là giao thức connectionless, không có số thứ tự (sequence number) và không theo dõi thứ tự các datagram đã gửi.
Nguồn: Không có
Trang đề: 4

## Câu 24
Câu hỏi: UDP phải sắp xếp lại Datagram theo thứ tự truyền
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: UDP giao dữ liệu cho tầng trên theo đúng thứ tự nhận được, không thực hiện sắp xếp lại các datagram.
Nguồn: Không có
Trang đề: 4

## Câu 25
Câu hỏi: Một trong các nhiệm vụ của UDP thiết lập phiên trước khi truyền dữ liệu giữa 2 thiết bị đầu cuối
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: UDP là giao thức không hướng kết nối (connectionless), không thực hiện bắt tay thiết lập phiên trước khi truyền dữ liệu như TCP.
Nguồn: Không có
Trang đề: 4

## Câu 26
Câu hỏi: UDP không có cơ chế phát hiện lỗi
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Header UDP có trường Checksum để kiểm tra lỗi cơ bản, dù không có cơ chế truyền lại khi lỗi; vì vậy nói UDP "không có cơ chế phát hiện lỗi" là sai.
Nguồn: Không có
Trang đề: 4

## Câu 27
Câu hỏi: UDP là giao thức truyền tin tin cậy
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: UDP không đảm bảo phân phối, không truyền lại gói mất và không sắp xếp lại thứ tự nên được xem là giao thức không tin cậy (unreliable).
Nguồn: Không có
Trang đề: 5

## Câu 28
Câu hỏi: Ứng dụng nào sau đây phù hợp nhất với UDP:
Chọn: 1
A. Video Conference
B. Truyền tải file qua mạng
C. Thanh toán qua mạng
D. Truyền tải email qua mạng
Đáp án: A
Giải thích: Hội thảo video cần độ trễ thấp và chấp nhận mất một phần dữ liệu, phù hợp với đặc tính nhanh, không đảm bảo của UDP; các ứng dụng còn lại cần độ tin cậy cao nên dùng TCP.
Nguồn: Không có
Trang đề: 5

## Câu 29
Câu hỏi: Giao thức UDP được gọi là không kết nối vì lý do nào sau đây
Chọn: 1
A. Các gói UDP được xử lý độc lập bởi lớp vận chuyển
B. Nó gửi dữ liệu dưới dạng luồng các gói liên quan
C. Nó được nhận theo thứ tự như thứ tự đã gửi
D. Nó gửi dữ liệu rất nhanh
Đáp án: A
Giải thích: Mỗi datagram UDP được xử lý độc lập, không có trạng thái phiên liên kết giữa các gói, đó là lý do UDP được gọi là giao thức connectionless.
Nguồn: Không có
Trang đề: 5

## Câu 30
Câu hỏi: Số hiệu cổng được sử dụng bởi Giao thức Network Time Protocol (NTP) với UDP là?
Chọn: 1
A. 161
B. 123
C. 162
D. 124
Đáp án: B
Giải thích: NTP sử dụng cổng UDP/123 theo quy định của IANA.
Nguồn: Không có
Trang đề: 5

## Câu 31
Câu hỏi: Cổng kết nối ở tầng Transport (giao thức UDP) của giao thức SNMP là
Chọn: 1
A. UDP/16
B. UDP/25
C. UDP/161
D. UDP/23
Đáp án: C
Giải thích: SNMP sử dụng cổng UDP/161 để nhận yêu cầu quản lý (cổng 162 dùng cho SNMP trap).
Nguồn: Không có
Trang đề: 5

## Câu 32
Câu hỏi: Đặc điểm của giao thức UDP là gì?
Chọn: 1
A. Truyền các gói dữ liệu theo đúng thứ tự
B. Truyền lại các gói dữ liệu mất trên đường truyền
C. Không truyền lại các gói dữ liệu bị lỗi
D. Không có câu nào đúng
Đáp án: C
Giải thích: UDP không có cơ chế truyền lại; nếu gói bị mất hoặc lỗi, UDP không tự động gửi lại như TCP.
Nguồn: Không có
Trang đề: 5

## Câu 33
Câu hỏi: Loại ứng dụng nào phù hợp nhất để sử dụng UDP?
Chọn: 1
A. Các ứng dụng nhạy cảm với độ trễ
B. Các ứng dụng cần phân phối đáng tin cậy
C. Các ứng dụng yêu cầu truyền lại các gói bị mất
D. Các ứng dụng nhạy cảm với việc mất gói
Đáp án: A
Giải thích: UDP không có overhead thiết lập kết nối và xác nhận nên độ trễ thấp, phù hợp cho ứng dụng nhạy cảm với độ trễ như thoại/video thời gian thực; các ứng dụng cần độ tin cậy hoặc nhạy cảm với mất gói nên dùng TCP.
Nguồn: Không có
Trang đề: 5

## Câu 34
Câu hỏi: Hoạt động nào được máy khách thực hiện khi thiết lập liên lạc với máy chủ thông qua việc sử dụng UDP ở tầng giao vận?
Chọn: 1
A. Máy khách đặt kích thước cửa sổ cho phiên.
B. Máy khách gửi SYN đến máy chủ để bắt đầu bắt tay 3 bước.
C. Máy khách chọn ngẫu nhiên một số hiệu cổng
D. Máy khách gửi một gói tin đồng bộ hóa để yêu cầu kết nối.
Đáp án: C
Giải thích: Vì UDP không có bắt tay ba bước hay cửa sổ trượt, hoạt động duy nhất phù hợp là máy khách tự chọn ngẫu nhiên một cổng nguồn trước khi gửi dữ liệu.
Nguồn: Không có
Trang đề: 6

## Câu 35
Câu hỏi: Tại sao UDP lại phù hợp làm giao thức tầng giao vận cho các ứng dụng như video, voice?
Chọn: 1
A. UDP đáp ứng nhanh và ít tiêu tốn tài nguyên.
B. UDP cung cấp khả năng kiểm soát luồng bằng cách sử dụng cửa sổ trượt windows.
C. UDP cung cấp xác nhận dữ liệu đã nhận.
D. UDP cung cấp một phiên đáng tin cậy.
Đáp án: A
Giải thích: UDP không tốn thời gian thiết lập kết nối, xác nhận hay kiểm soát luồng nên có độ trễ thấp và ít tiêu tốn tài nguyên, phù hợp với ứng dụng thời gian thực; các phương án B, C, D là đặc điểm của TCP chứ không phải UDP.
Nguồn: Không có
Trang đề: 6

## Câu 36
Câu hỏi: Đặc điểm của UDP là gì?
Chọn: 1
A. Nó thiết lập phiên kết nối qua quá trình bắt tay ba bước
B. Nó đóng phiên đã thiết lập qua quá trình bắt tay bốn bước
C. Nó cung cấp khả năng phân phối các datagram một cách không tin cậy
D. Nó cung cấp khả năng phân phối các segment một cách không tin cậy
Đáp án: C
Giải thích: UDP phân phối dữ liệu dưới dạng datagram một cách không đảm bảo (unreliable); các phương án A, B mô tả TCP, còn D nhầm đơn vị dữ liệu là segment (thuộc TCP) thay vì datagram.
Nguồn: Không có
Trang đề: 6

## Câu 37
Câu hỏi: Các ứng dụng sử dụng giao thức UDP là (Chọn 3)
Chọn: 3
A. Ứng dụng video và đa phương tiện trực tiếp
B. Ứng dụng yêu cầu và trả lời đơn giản
C. Các ứng dụng tự xử lý độ tin cậy
D. Ứng dụng gửi thư điện tử
Đáp án: A, B, C
Giải thích: Video/đa phương tiện trực tiếp, ứng dụng dạng yêu cầu–trả lời đơn giản (như DNS) và ứng dụng tự đảm nhiệm việc kiểm soát độ tin cậy ở tầng trên (như TFTP) đều phù hợp dùng UDP; gửi thư điện tử dùng SMTP/POP3/IMAP chạy trên TCP.
Nguồn: Không có
Trang đề: 6

## Câu 38
Câu hỏi: Các giao thức nào chỉ sử dụng UDP (Chọn 3)
Chọn: 3
A. DHCP
B. TFTP
C. NTP
D. DNS
Đáp án: A, B, C
Giải thích: DHCP, TFTP và NTP chỉ hoạt động trên UDP; riêng DNS chủ yếu dùng UDP nhưng vẫn có thể chuyển sang TCP (ví dụ khi truyền zone transfer hoặc phản hồi dữ liệu lớn), nên không phải giao thức "chỉ" dùng UDP.
Nguồn: Không có
Trang đề: 6

## Câu 39
Câu hỏi: Phát biểu nào dưới đây là đúng khi nói về giao thức UDP (Chọn 3)
Chọn: 3
A. Không có giai đoạn thiết lập kết nối
B. Không duy trì trạng thái kết nối
C. Không kiểm soát tốc độ gửi
D. Chỉ kiểm soát tốc độ nhận
Đáp án: A, B, C
Giải thích: UDP không bắt tay thiết lập kết nối, không lưu trạng thái phiên và không có cơ chế kiểm soát luồng/tốc độ gửi; UDP cũng không kiểm soát tốc độ nhận nên phương án D sai.
Nguồn: Không có
Trang đề: 7

## Câu 40
Câu hỏi: Các thành phần nằm trong UDP Header là (Chọn 3)
Chọn: 3
A. Source Port
B. Checksum
C. Length
D. SYN Bit
Đáp án: A, B, C
Giải thích: Header UDP gồm 4 trường: Source Port, Destination Port, Length và Checksum; cờ SYN chỉ tồn tại trong header TCP.
Nguồn: Không có
Trang đề: 7

## Câu 41
Câu hỏi: Chức năng của giao thức UDP là (Chọn 3)
Chọn: 3
A. Dữ liệu được xây dựng lại theo thứ tự nhận được.
B. Bất kỳ datagram nào bị mất sẽ không được gửi lại.
C. Không thiết lập phiên
D. Kiểm soát luồng
Đáp án: A, B, C
Giải thích: UDP tái tạo dữ liệu đúng theo thứ tự nhận được (không sắp xếp lại), không truyền lại gói bị mất và không thiết lập phiên; kiểm soát luồng không phải chức năng của UDP.
Nguồn: Không có
Trang đề: 7

## Câu 42
Câu hỏi: Giao thức TCP sử dụng cửa sổ trượt để kiểm soát luồng
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: TCP dùng cơ chế sliding window (cửa sổ trượt) để điều tiết lượng dữ liệu gửi đi, thực hiện chức năng kiểm soát luồng.
Nguồn: Không có
Trang đề: 7

## Câu 43
Câu hỏi: Trong giao thức TCP, các gói tin được gọi là segment
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Đơn vị dữ liệu (PDU) của TCP ở tầng Giao vận được gọi là segment.
Nguồn: Không có
Trang đề: 7

## Câu 44
Câu hỏi: TCP là một giao thức không tin cậy?
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: TCP là giao thức tin cậy (reliable) nhờ cơ chế số thứ tự, xác nhận (ACK) và truyền lại khi mất gói; vì vậy phát biểu "TCP không tin cậy" là sai.
Nguồn: Không có
Trang đề: 7

## Câu 45
Câu hỏi: TCP không có chức năng sắp xếp lại các segment
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Nhờ trường Sequence Number, TCP có khả năng sắp xếp lại các segment đến sai thứ tự tại bên nhận; do đó phát biểu "không có chức năng sắp xếp lại" là sai.
Nguồn: Không có
Trang đề: 7

## Câu 46
Câu hỏi: TCP sử dụng cơ chế cửa sổ trượt để điều khiển tốc độ truyền dữ liệu
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Cửa sổ trượt (sliding window) cho phép TCP điều chỉnh lượng dữ liệu được gửi trước khi cần xác nhận, qua đó kiểm soát tốc độ truyền.
Nguồn: Không có
Trang đề: 7

## Câu 47
Câu hỏi: Trong TCP, việc gửi và nhận dữ liệu được thực hiện dưới dạng
Chọn: 1
A. Dòng bytes
B. Chuỗi các ký tự
C. Các đường dữ liệu
D. Các gói tin
Đáp án: A
Giải thích: TCP xem dữ liệu ứng dụng như một dòng byte liên tục (byte stream) rồi mới chia thành các segment để truyền đi, chứ không xử lý theo đơn vị ký tự hay "gói tin" như một khái niệm độc lập ở tầng này.
Nguồn: Không có
Trang đề: 7

## Câu 48
Câu hỏi: Một máy khách đã thực hiện yêu cầu HTTP tới trình duyệt web. Số hiệu địa chỉ cổng thông dụng nào được liên kết với địa chỉ đích?
Chọn: 1
A. TCP/404
B. TCP/110
C. TCP/443
D. TCP/80
Đáp án: D
Giải thích: HTTP (không mã hóa) sử dụng cổng thông dụng TCP/80; TCP/443 dành cho HTTPS, TCP/110 dành cho POP3.
Nguồn: Không có
Trang đề: 8

## Câu 49
Câu hỏi: Ứng dụng nào sau đây không phù hợp với giao thức TCP?
Chọn: 1
A. Trình duyệt Web
B. Hệ thống hội thảo video trực tuyến
C. Hệ thống thanh toán qua mạng
D. Email
Đáp án: B
Giải thích: Hội thảo video trực tuyến cần độ trễ thấp và chấp nhận mất một phần dữ liệu, nên phù hợp UDP hơn; TCP với cơ chế xác nhận và truyền lại sẽ gây trễ không phù hợp cho truyền thời gian thực. Web, thanh toán và email đều cần độ tin cậy nên phù hợp TCP.
Nguồn: Không có
Trang đề: 8

## Câu 50
Câu hỏi: Acknowledgment number trong tiêu đề TCP là một số
Chọn: 1
A. Độc lập
B. Ngẫu nhiên
C. Liên quan tới số SeqN của bên gửi
D. Không liên quan tới số SeqN của bên gửi
Đáp án: C
Giải thích: Số Acknowledgment mà bên nhận gửi lại được tính dựa trên số Sequence Number của segment đã nhận (thường bằng SeqN nhận được cộng với số byte dữ liệu), nên nó liên quan trực tiếp tới SeqN của bên gửi.
Nguồn: Không có
Trang đề: 8

## Câu 51
Câu hỏi: Byte dữ liệu được truyền trong mỗi kết nối được đánh số bởi TCP. Những con số này có dạng?
Chọn: 1
A. Số cố định
B. Số 0
C. Số 1
D. Chuỗi số 0 và số 1
Đáp án: D
Giải thích: Về bản chất, mọi số thứ tự byte mà TCP gán cho dữ liệu đều được biểu diễn dưới dạng nhị phân, tức chuỗi các bit 0 và 1.
Nguồn: Không có
Trang đề: 8

## Câu 52
Câu hỏi: Cổng kết nối của giao thức SMTP là
Chọn: 1
A. TCP/24
B. TCP/26
C. TCP/25
D. TCP/27
Đáp án: C
Giải thích: SMTP (giao thức gửi thư điện tử) sử dụng cổng mặc định TCP/25.
Nguồn: Không có
Trang đề: 8

## Câu 53
Câu hỏi: Quá trình bộ nhận kiểm soát lượng dữ liệu được gửi bởi người gửi được gọi là?
Chọn: 1
A. Điều khiển luồng
B. Điều khiển lỗi
C. Kiểm soát tắc nghẽn
D. Phát hiện lỗi
Đáp án: A
Giải thích: Điều khiển luồng (flow control) là cơ chế bên nhận thông báo (qua kích thước cửa sổ) để điều tiết tốc độ gửi của bên gửi, tránh làm tràn bộ đệm nhận.
Nguồn: Không có
Trang đề: 8

## Câu 54
Câu hỏi: Thông số nào được nút nguồn lựa chọn ngẫu nhiên trước khi gửi dữ liệu
Chọn: 1
A. Địa chỉ IP đích.
B. Địa chỉ MAC nguồn.
C. Địa chỉ cổng mặc định.
D. Cổng nguồn.
Đáp án: D
Giải thích: Trước khi gửi dữ liệu, thiết bị nguồn tự chọn ngẫu nhiên một cổng nguồn (thường trong dải cổng động) để định danh phiên giao tiếp của mình; địa chỉ IP đích, MAC nguồn và cổng mặc định đều là các giá trị cố định/được cấu hình sẵn, không chọn ngẫu nhiên.
Nguồn: Không có
Trang đề: 9

## Câu 55
Câu hỏi: Trường thông tin Sequence Number trong tiêu đề của giao thức TCP dùng để làm gì?
Chọn: 1
A. Lưu số thứ tự của gói tin
B. Lưu mã xử lý lỗi của gói tin
C. Lưu thông tin điều khiển lưu lượng
D. Lưu thông tin điều khiển xung đột
Đáp án: A
Giải thích: Sequence Number đánh số thứ tự byte dữ liệu trong segment, giúp bên nhận sắp xếp lại đúng thứ tự và phát hiện dữ liệu bị thiếu.
Nguồn: Không có
Trang đề: 9

## Câu 56
Câu hỏi: Trường nào trong tiêu đề TCP được sử dụng để bắt đầu quá trình bắt tay ba bước?
Chọn: 1
A. FIN
B. PSH
C. RST
D. SYN
Đáp án: D
Giải thích: Cờ SYN (Synchronize) được thiết lập trong segment đầu tiên để khởi tạo quá trình bắt tay ba bước, thiết lập kết nối TCP.
Nguồn: Không có
Trang đề: 9

## Câu 57
Câu hỏi: Các chức năng trong giao thức TCP là (Chọn 3)
Chọn: 3
A. Thiết lập phiên
B. Đảm bảo tin cậy
C. Điều khiển luồng
D. Giữ và chuyển tiếp
Đáp án: A, B, C
Giải thích: TCP thiết lập phiên qua bắt tay ba bước, đảm bảo độ tin cậy bằng ACK/truyền lại và điều khiển luồng bằng cửa sổ trượt; "giữ và chuyển tiếp" (store-and-forward) là cơ chế của thiết bị chuyển mạch, không phải chức năng của TCP.
Nguồn: Không có
Trang đề: 9

## Câu 58
Câu hỏi: Các dịch vụ sử dụng giao thức TCP là (Chọn 3)
Chọn: 3
A. FTP
B. HTTP
C. SMTP
D. Streaming
Đáp án: A, B, C
Giải thích: FTP, HTTP và SMTP đều cần truyền dữ liệu tin cậy nên chạy trên TCP; streaming thời gian thực thường ưu tiên UDP/RTP để giảm độ trễ, chấp nhận mất một phần dữ liệu.
Nguồn: Không có
Trang đề: 9

## Câu 59
Câu hỏi: Ba trường nào sau đây có trong tiêu đề TCP? (Chọn 3)
Chọn: 3
A. ISN
B. SYN
C. FIN
D. URG
Đáp án: B, C, D
Giải thích: SYN, FIN và URG là các cờ (control bit) thực sự tồn tại trong header TCP; ISN (Initial Sequence Number) chỉ là giá trị khởi tạo được ghi vào trường Sequence Number lúc bắt đầu kết nối, không phải tên một trường riêng trong header.
Nguồn: Không có
Trang đề: 9

## Câu 60
Câu hỏi: Các ý nào dưới đây nằm trong quá trình kết thúc phiên kết nối (Chọn 3)
Chọn: 3
A. Khi Client không còn dữ liệu để gửi, nó sẽ gửi một segment có gán cờ FIN
B. Server gửi lại ACK để xác nhận đã nhận được FIN để chấm dứt phiên kết nối
C. Server gửi ISN để đóng phiên kết nối này
D. Client gửi lại ACK để xác nhận đã nhận được FIN từ Server
Đáp án: A, B, D
Giải thích: Quá trình đóng kết nối TCP diễn ra qua trao đổi cờ FIN/ACK giữa hai bên (Client gửi FIN, Server ACK lại, Server cũng gửi FIN của mình, Client ACK lại); ISN (Initial Sequence Number) chỉ dùng khi thiết lập kết nối lúc bắt đầu, không liên quan đến việc đóng phiên.
Nguồn: Không có
Trang đề: 9
