# Chương 2 · Chuyển mạch Ethernet

Bộ đề: 51 câu, đánh số liên tục theo thứ tự trong PDF gốc.
Đề và đáp án: MMT - 07 - Ch02 - Trắc nghiệm chương 2 và đáp án.pdf; đáp án theo lựa chọn in đậm.
Giải thích: chỉ dùng các tài liệu nguồn được cung cấp. Số trang tính từ 1 trong PDF.
Chấm theo đáp án đề; những khác biệt đã phát hiện so với slide được ghi chú ngay tại câu.

## Câu 1
Câu hỏi: Một trong những chức năng của tầng liên kết dữ liệu là phát hiện lỗi.
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Tầng Liên kết dữ liệu kiểm tra lỗi khung bằng FCS/CRC. Khung bị lỗi sẽ bị loại bỏ; một số giao thức còn hỗ trợ truyền lại. Vì vậy phát hiện lỗi là một chức năng của tầng này.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 4, 7
Trang đề: 1

## Câu 2
Câu hỏi: Ethernet là một loại giao thức trong tầng liên kết dữ liệu
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Slide liệt kê Ethernet (IEEE 802.3) trong các công nghệ và giao thức tiêu biểu của tầng Liên kết dữ liệu. Phần kiến trúc cũng cho biết Ethernet hoạt động ở cả tầng Vật lý và Liên kết dữ liệu.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 10, 12
Trang đề: 1

## Câu 3
Câu hỏi: PDU được sử dụng ở tầng liên kết dữ liệu gọi là Bits
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: PDU ở tầng Liên kết dữ liệu là Frame; Bits thuộc tầng Vật lý. Do đó phát biểu gọi PDU của tầng Liên kết là Bits là sai.
Nguồn: MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf — trang 19
Trang đề: 1

## Câu 4
Câu hỏi: Cấu trúc khung tầng liên kết dữ liệu có trường tiêu đề (header) và phần đuôi (trailer)
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Khi đóng khung, tầng Liên kết thêm header và trailer chứa thông tin điều khiển. Khung Ethernet gồm Header, Data và Trailer.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 5, 15
Trang đề: 1

## Câu 5
Câu hỏi: Quá trình dữ liệu di chuyển từ tầng trên xuống tầng datalink phải thực hiện việc?
Chọn: 1
A. Phân tích dữ liệu
B. Lọc dữ liệu
C. Nén dữ liệu
D. Đóng gói dữ liệu
Đáp án: D
Giải thích: Slide mô tả đóng khung là chia dữ liệu từ tầng Mạng thành frame, thêm header và trailer. Đây là quá trình đóng gói dữ liệu, tương ứng phương án D.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 5
Trang đề: 1

## Câu 6
Câu hỏi: Đơn vị dữ liệu tầng datalink là:
Chọn: 1
A. Mbs
B. Segment
C. Frame
D. Bits
Đáp án: C
Giải thích: Slide ghi PDU của Data Link là Frame, trong khi Segment thuộc Transport và Bits thuộc Physical.
Nguồn: MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf — trang 19
Trang đề: 1

## Câu 7
Câu hỏi: Frame là dữ liệu ở tầng:
Chọn: 1
A. Physical
B. Network
C. Data Link
D. Transport
Đáp án: C
Giải thích: Frame là tên đơn vị dữ liệu ở tầng Data Link trong chuỗi PDU của mô hình truyền thông.
Nguồn: MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf — trang 19
Trang đề: 1

## Câu 8
Câu hỏi: Card mạng là thiết bị nằm ở tầng nào trong mô hình OSI:
Chọn: 1
A. Physical
B. Data Link
C. Network
D. Transport
Đáp án: B
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 2

## Câu 9
Câu hỏi: Tầng nào cung cấp dịch vụ truyền tin tin cậy qua môi trường vật lý:
Chọn: 1
A. Physical
B. Data link
C. Network
D. Transport
Đáp án: B
Giải thích: Tầng Liên kết có chức năng kiểm soát lỗi và điều khiển luồng: phát hiện lỗi bằng FCS/CRC và điều chỉnh tốc độ cho phù hợp khả năng nhận. Đây là căn cứ để chọn Data Link trong ngữ cảnh truyền qua liên kết vật lý. Slide chỉ nói một số giao thức hỗ trợ truyền lại, không khẳng định mọi giao thức tầng này đều bảo đảm giao hàng.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 4, 7
Trang đề: 2

## Câu 10
Câu hỏi: Dịch vụ nào sau đây mà tầng liên kết dữ liệu phải cung cấp? (Chọn 3)
Chọn: 3
A. Tạo khung
B. Xác định địa chỉ vật lý
C. Kiểm soát lỗi
D. Xác định địa chỉ logic
Đáp án: A, B, C
Giải thích: Slide nêu chức năng đóng khung, gắn địa chỉ MAC nguồn/đích và kiểm soát lỗi. Ba chức năng này tương ứng A, B, C; địa chỉ logic và định tuyến thuộc tầng Mạng.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 4–5; MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf — trang 13
Trang đề: 2

## Câu 11
Câu hỏi: Các giao thức nào dưới đây nằm ở tầng liên kết dữ liệu? (Chọn 3)
Chọn: 3
A. IP
B. Ethernet
C. Token ring
D. PPP
Đáp án: B, C, D
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 2

## Câu 12
Câu hỏi: CSMA/CD là giao thức truy cập ngẫu nhiên
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 2

## Câu 13
Câu hỏi: NIC là viết tắt của Network Interface Card
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Slide ghi đầy đủ Network Interface Card - NIC khi mô tả giao diện mạng được định danh bằng địa chỉ MAC.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 21
Trang đề: 2

## Câu 14
Câu hỏi: Mỗi NIC (Network Interface Card) có thể có nhiều địa chỉ MAC
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 2

## Câu 15
Câu hỏi: LLC là một lớp con (sublayer) trong tầng liên kết dữ liệu
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Tầng Liên kết dữ liệu trong kiến trúc Ethernet được chia thành hai tầng con là LLC và MAC. Vì vậy LLC là một sublayer của tầng này.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 12
Trang đề: 2

## Câu 16
Câu hỏi: Khi địa chỉ MAC đích là Broadcast, nó được dùng để gửi tới một địa chỉ đích duy nhất trong mạng LAN
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Địa chỉ MAC Broadcast dùng cho tất cả thiết bị trong cùng miền quảng bá; gửi tới một thiết bị duy nhất là Unicast. Phát biểu trong đề đã nhầm Broadcast với Unicast.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 23–26
Trang đề: 2

## Câu 17
Câu hỏi: Câu nào đúng về địa chỉ MAC?
Chọn: 1
A. Địa chỉ MAC được thực hiện bằng phần mềm.
B. NIC chỉ cần địa chỉ MAC nếu được kết nối với mạng WAN.
C. Ba bytes cuối trong địa chỉ MAC được gán bởi nhà sản xuất thiết bị.
D. ISO chịu trách nhiệm về các quy định về địa chỉ MAC.
Đáp án: C
Giải thích: Địa chỉ MAC gồm OUI 3 byte và Extension Identifier 3 byte. OUI do IEEE cấp cho nhà sản xuất; phần 3 byte còn lại do nhà sản xuất gán cho từng giao diện mạng.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 21
Trang đề: 3

## Câu 18
Câu hỏi: Công nghệ Ethernet sử dụng phương pháp truy nhập đường truyền nào sau đây:
Chọn: 1
A. CSMA
B. ALOHA
C. CSMA/CD
D. TDMA
Đáp án: C
Giải thích: Slide nêu CSMA/CD áp dụng cho Ethernet Half-Duplex, điển hình khi dùng Hub. Không áp dụng cơ chế này cho Ethernet Full-Duplex, điển hình khi dùng Switch.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 6
Trang đề: 3
Lưu ý: Đáp án C được giữ theo đề; điều kiện Half-Duplex được nêu rõ trong phần giải thích để tránh áp dụng cho mọi Ethernet.

## Câu 19
Câu hỏi: CSMA/CD là viết tắt của:
Chọn: 1
A. Collision Sense Multiple Access / Collision Detection
B. Carrier Sense Multiple Access / Carrier Detection
C. Carrier Sense Multiple Access / Collision Detection
D. Collision Sense Multiple Access / Carrier Detection
Đáp án: C
Giải thích: Slide viết đầy đủ CSMA/CD là Carrier Sense Multiple Access with Collision Detection. Phương án C dùng đúng Carrier Sense và Collision Detection.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 6
Trang đề: 3

## Câu 20
Câu hỏi: Chuỗi số “00-08-ac-41-5d-9f” có thể là:
Chọn: 1
A. Địa chỉ IP
B. Địa chỉ port
C. Địa chỉ MAC
D. Địa chỉ dịch vụ
Đáp án: C
Giải thích: Địa chỉ MAC dài 48 bit, tương đương 12 chữ số hệ 16, có thể viết thành 6 nhóm, mỗi nhóm 2 chữ số, phân cách bằng dấu gạch ngang. Chuỗi trong đề khớp định dạng này.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 22
Trang đề: 3

## Câu 21
Câu hỏi: Chuẩn nào dưới đây đặc tả về chuẩn kiến trúc mạng cục bộ cho Ethernet, bao gồm các chuẩn tầng vật lý và tầng con MAC:
Chọn: 1
A. IEEE 802.2
B. IEEE 802.3
C. Token Bus
D. Token Ring
Đáp án: B
Giải thích: IEEE 802.3 là chuẩn Ethernet. Slide kiến trúc cho biết Ethernet hoạt động ở tầng Vật lý và Liên kết dữ liệu, với tầng con MAC gắn với IEEE 802.3.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 9, 12
Trang đề: 3

## Câu 22
Câu hỏi: Chọn phát biểu ĐÚNG về địa chỉ MAC:
Chọn: 1
A. Được gắn trên card mạng (NIC)
B. Do người quản trị mạng khai báo
C. Được gán trong quá trình thiết bị khởi động
D. Được gán trong quá trình thiết bị truyền thông tin
Đáp án: A
Giải thích: Slide cho biết địa chỉ MAC định danh giao diện mạng NIC; nhà sản xuất gán phần Extension Identifier cho từng NIC thuộc OUI của họ. Điều này phù hợp với lựa chọn A trong ngữ cảnh đề.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 21
Trang đề: 3

## Câu 23
Câu hỏi: Công nghệ nào dưới đây được sử dụng phổ biến nhất trong mạng LAN hiện nay:
Chọn: 1
A. Token Ring
B. FDDI
C. Ethernet
D. ADSL
Đáp án: C
Giải thích: Slide mô tả Ethernet là công nghệ truyền dữ liệu phổ biến nhất trong mạng LAN có dây. Trong các phương án của đề, Ethernet khớp mô tả này.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 11
Trang đề: 4

## Câu 24
Câu hỏi: LLC là viết tắt của:
Chọn: 1
A. Logical Link Control
B. Link Logical Control
C. Logical Link Computer
D. Lan Logical Control
Đáp án: A
Giải thích: Slide ghi LLC = Logical Link Control, lớp điều khiển kết nối logic. Phương án A khớp đúng thứ tự các từ.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 12–13
Trang đề: 4

## Câu 25
Câu hỏi: Địa chỉ MAC nào có dưới đây KHÔNG trong tiêu đề của Frame? (Chọn 3)
Chọn: 3
A. MAC sources
B. MAC Gateway
C. MAC destination
D. MAC Default
Đáp án: A, B, D
Giải thích: Slide liệt kê cả Destination MAC Address và Source MAC Address là các trường của khung Ethernet; phần Header chứa MAC nguồn và MAC đích. Vì vậy phương án A (MAC sources) thực sự có trong header. Trong bốn lựa chọn, chỉ B và D không phải các trường địa chỉ được liệt kê; điều này không khớp yêu cầu chọn 3 và đáp án A, B, D của đề.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 15, 18
Trang đề: 4
Lưu ý: Đề gốc in đậm A, B, D và yêu cầu Chọn 3. File giữ nguyên để chấm theo đề, dù không khớp slide; nên đối chiếu câu này với giảng viên.

## Câu 26
Câu hỏi: Các loại địa chỉ MAC bao gồm? (Chọn 3)
Chọn: 3
A. MAC unicast
B. MAC multicast
C. MAC broadcast
D. MAC anycast
Đáp án: A, B, C
Giải thích: Slide chia địa chỉ MAC thành Unicast, Multicast và Broadcast. Ba lựa chọn tương ứng là A, B, C.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 23
Trang đề: 4

## Câu 27
Câu hỏi: Tốc độ của GigabitEthernet có thể lên đến 10000Mbps?
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Slide nêu 1000BASE-T và 1000BASE-SX có tốc độ 1 Gbps; 10GBASE-T có tốc độ 10 Gbps. Bảng đơn vị cho biết 1 Gbps = 1000 Mbps, nên 10000 Mbps là mức 10 Gbps, không phải mức Gigabit 1 Gbps trong câu hỏi.
Nguồn: MMT - 04 - Ch02 - Công nghệ Ethernet.pdf — trang 28; MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf — trang 23
Trang đề: 4

## Câu 28
Câu hỏi: Thiết bị chuyển mạch lớp 2 hoạt động kém hiệu quả hơn so với Hub?
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Slide mô tả Switch lớp 2 có hiệu năng cao hơn Hub nhờ chuyển tiếp khung thông minh. Do đó nói Switch kém hiệu quả hơn Hub là sai.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 7
Trang đề: 4

## Câu 29
Câu hỏi: Mac Address Table được lưu trữ trong RAM của Switch?
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 4

## Câu 30
Câu hỏi: Một thiết bị chuyển mạch lớp 2 có thể hỗ trợ các loại cổng:
Chọn: 1
A. Cổng dynamic và Well-known
B. Cổng access và Well-known
C. Cổng trunk và Well-known
D. Cổng access và trunk
Đáp án: D
Giải thích: Slide giới thiệu Access Port để nối thiết bị đầu cuối vào một VLAN và Trunk Port để mang lưu lượng nhiều VLAN giữa các thiết bị mạng. Vì vậy chọn access và trunk.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 20, 24
Trang đề: 4

## Câu 31
Câu hỏi: Thiết bị Switch thông thường nằm ở tầng nào của mô hình OSI?
Chọn: 1
A. Tầng 1
B. Tầng 2
C. Tầng 3
D. Tầng 4
Đáp án: B
Giải thích: Switch lớp 2 hoạt động ở tầng Liên kết dữ liệu (Data Link Layer), tức tầng 2 của OSI.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 7
Trang đề: 5

## Câu 32
Câu hỏi: Để hạn chế sự đụng độ (hay va chạm) giữa các gói tin trong mạng người ta sử dụng thiết bị nào dưới đây?
Chọn: 1
A. Repeaters
B. Hubs
C. Switches
D. Card mạng (NIC)
Đáp án: C
Giải thích: Mọi cổng của Hub cùng thuộc một miền va chạm, còn mỗi cổng của Switch thuộc một miền va chạm riêng. Sự phân chia này là căn cứ chọn Switches để hạn chế va chạm.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 4–5
Trang đề: 5

## Câu 33
Câu hỏi: Địa chỉ nào được quan tâm khi một frame đi vào cổng của Switch?
Chọn: 1
A. Địa chỉ IP nguồn
B. Địa chỉ MAC nguồn
C. Địa chỉ IP đích
D. Địa chỉ MAC đích
Đáp án: D
Giải thích: Để quyết định chuyển tiếp hoặc lọc frame, Switch tra cứu địa chỉ MAC đích trong bảng MAC. Đồng thời, Switch dùng MAC nguồn để học địa chỉ. Đáp án D phù hợp khi câu hỏi được hiểu là địa chỉ dùng cho quyết định chuyển tiếp.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 8, 12, 14
Trang đề: 5
Lưu ý: Câu hỏi chưa nói rõ học địa chỉ hay chuyển tiếp. Đề in đậm D; slide cho thấy cả MAC nguồn và MAC đích đều được sử dụng, với vai trò khác nhau.

## Câu 34
Câu hỏi: Các thiết bị nào dưới đây không được sử dụng để hạn chế sự đụng độ của các gói tin trong mạng? (Chọn 3)
Chọn: 3
A. Repeaters
B. Hubs
C. Switches
D. Card mạng (NIC)
Đáp án: A, B, D
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 5

## Câu 35
Câu hỏi: Một miền quảng bá có tính chất như sau (Chọn 3)
Chọn: 3
A. Phạm vi truy cập của các gói Broadcast
B. Các thiết bị trong cùng một miền quảng bá có thể nhận gói quảng bá
C. Bộ định tuyến phân tách các miền quảng bá bằng interface
D. Bộ định tuyến không phân tách được miền quảng bá
Đáp án: A, B, C
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 5

## Câu 36
Câu hỏi: Các cách xử lý frame khi đi vào giao diện trên Switch? (Chọn 3)
Chọn: 3
A. Flooding
B. Saving
C. Forwarding
D. Discarding
Đáp án: A, C, D
Giải thích: Slide trình bày ba cách xử lý: Flooding gửi ra nhiều cổng khi chưa biết MAC đích hoặc gặp broadcast; Forwarding chuyển đến cổng phù hợp; Filtering/Discarding không chuyển tiếp khung. Vì vậy chọn A, C, D.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 9–11
Trang đề: 5

## Câu 37
Câu hỏi: Các chức năng đặc thù của thiết bị chuyển mạch lớp 2? (Chọn 3)
Chọn: 3
A. Xoá bỏ dữ liệu lỗi
B. Học địa chỉ
C. Quyết định chuyển tiếp/lọc khung
D. Tránh Loop
Đáp án: B, C, D
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 6

## Câu 38
Câu hỏi: Các loại cổng Ethernet nào dưới đây dùng để truyền dữ liệu trong mạng LAN? (Chọn 3)
Chọn: 3
A. FastEthernet
B. GigabitEthernet
C. Ten Gigabit Ethernet
D. Console Ethernet
Đáp án: A, B, C
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 6

## Câu 39
Câu hỏi: VLAN là một mạng LAN ảo
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: VLAN viết đầy đủ là Virtual Local Area Network, được định nghĩa là mạng LAN ảo, chia một LAN vật lý thành nhiều LAN logic.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 17
Trang đề: 6

## Câu 40
Câu hỏi: Dữ liệu ở VLAN gốc không được trao đổi qua kết nối Trunking
Chọn: 1
A. Đúng
B. Sai
Đáp án: B
Giải thích: Slide nói frame của Native VLAN vẫn được truyền qua cổng Trunk nhưng không gắn VLAN Tag. Không gắn thẻ không có nghĩa là không được truyền, nên phát biểu sai.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 25, 28
Trang đề: 6

## Câu 41
Câu hỏi: IEEE 802.1Q có tên gọi khác là dot1Q
Chọn: 1
A. Đúng
B. Sai
Đáp án: A
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 6

## Câu 42
Câu hỏi: Thiết bị Hub có bao nhiêu collision domain?
Chọn: 1
A. 1
B. 2
C. 3
D. 4
Đáp án: A
Giải thích: Tất cả các cổng của Hub thuộc cùng một Collision Domain, vì vậy có 1 miền va chạm.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 4
Trang đề: 6

## Câu 43
Câu hỏi: Thiết bị Switch có bao nhiêu collision domain?
Chọn: 1
A. 3 collisions / 1 port
B. 2 collisions / 1port
C. 1 collision / 1port
D. 4 collisions / 1 port
Đáp án: C
Giải thích: Slide nêu mỗi cổng Switch thuộc một Collision Domain riêng. Lựa chọn C diễn đạt 1 miền va chạm trên mỗi cổng.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 5
Trang đề: 6

## Câu 44
Câu hỏi: Thiết bị Switch (cấu hình mặc định) có bao nhiêu Broadcast domain?
Chọn: 1
A. 1
B. 2
C. 3
D. 4
Đáp án: A
Giải thích: Theo slide, mặc định tất cả cổng của Switch thuộc cùng một Broadcast Domain, tức 1 miền quảng bá.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 5
Trang đề: 6

## Câu 45
Câu hỏi: Thiết bị Hub có bao nhiêu Broadcast domain?
Chọn: 1
A. 1
B. 2
C. 3
D. 4
Đáp án: A
Giải thích: Slide mô tả Hub phát lại tín hiệu đến tất cả các cổng còn lại. Kết hợp định nghĩa Broadcast Domain là vùng mà mọi thiết bị nhận được gói broadcast, các thiết bị nối cùng Hub thuộc một miền quảng bá.
Nguồn: MMT - 02 - Ch01 - Tổng quan về Mạng máy tính và Internet.pdf — trang 28; MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 5
Trang đề: 6

## Câu 46
Câu hỏi: Virtual LAN (VLAN) là một nhóm các thiết bị kết nối trong cùng miền nào dưới đây?
Chọn: 1
A. Miền tự trị
B. Miền quảng bá
C. Miền vật lý
D. Miền va chạm
Đáp án: B
Giải thích: Mỗi VLAN là một Broadcast Domain riêng. Vì vậy nhóm thiết bị thuộc một VLAN gắn với cùng miền quảng bá.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 17
Trang đề: 7

## Câu 47
Câu hỏi: Một mạng chứa nhiều VLAN trải rộng trên nhiều thiết bị chuyển mạch (trong các VLAN có VLAN 20). Điều gì xảy ra khi một thiết bị trong VLAN 20 gửi khung Ethernet quảng bá?
Chọn: 1
A. Các thiết bị trong các VLAN đều nhìn thấy frame.
B. Các thiết bị trong VLAN 20 và VLAN quản lý sẽ nhìn thấy frame.
C. Chỉ các thiết bị trong VLAN 20 mới nhìn thấy frame.
D. Chỉ những thiết bị được kết nối với bộ chuyển mạch cục bộ mới nhìn thấy frame.
Đáp án: C
Giải thích: Mỗi VLAN có miền quảng bá riêng. Trunk cho phép mở rộng các VLAN trên nhiều Switch nhưng vẫn duy trì sự tách biệt giữa chúng. Vì thế frame broadcast của VLAN 20 chỉ lan trong VLAN 20, không tự lan sang VLAN khác.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 16–17, 22
Trang đề: 7

## Câu 48
Câu hỏi: Trong Switch Cisco, VLAN mặc định là:
Chọn: 1
A. VLAN 1
B. VLAN 2
C. VLAN 3
D. VLAN 4
Đáp án: A
Giải thích: Slide nêu VLAN 1 là VLAN mặc định trên hầu hết Switch Cisco, nên phương án A phù hợp.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 19
Trang đề: 7

## Câu 49
Câu hỏi: Lợi ích của việc sử dụng VLAN là gì? (Chọn 3)
Chọn: 3
A. Tăng cường bảo mật
B. Giảm chi phí, tăng hiệu suất
C. Dễ quản lý
D. Giảm độ trễ xử lý frame và bits
Đáp án: A, B, C
Giải thích: Không có trong tài liệu nguồn.
Nguồn: Không có
Trang đề: 7

## Câu 50
Câu hỏi: Các dãy giá trị nào dưới đây thoả mãn là VLAN-ID? (Chọn 3)
Chọn: 3
A. 1-1001
B. 1002-1005
C. 1006-4094
D. 4095-5095
Đáp án: A, B, C
Giải thích: Dải VLAN ID hợp lệ trong slide là 1 đến 4094. Các dải A, B, C đều nằm hoàn toàn trong khoảng này; D bắt đầu từ 4095, là giá trị dự phòng và còn vượt giới hạn.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 19, 26
Trang đề: 7

## Câu 51
Câu hỏi: Phát biểu nào sau đây là SAI: khi Switch nhận được một frame gửi tới nó, Switch sẽ xử lý như thế nào nếu địa chỉ MAC đích trong frame không có trong bảng địa chỉ MAC của nó? (Chọn 3)
Chọn: 3
A. Switch sẽ chuyển frame đến địa chỉ default gateway
B. Switch sẽ chuyển frame đến cổng gần nhất
C. Switch sẽ hủy bỏ frame này
D. Switch sẽ chuyển tiếp frame đến các cổng của Switch trừ cổng nhận frame vào
Đáp án: A, B, C
Giải thích: Nếu không tìm thấy MAC đích trong bảng MAC, Switch flood frame ra các cổng đang hoạt động, trừ cổng nhận. Do đó D mô tả cách xử lý trong slide; câu hỏi yêu cầu các phát biểu SAI nên chọn A, B, C.
Nguồn: MMT - 07 - Ch02 - Chuyển mạch Ethernet.pdf — trang 9, 14
Trang đề: 7
