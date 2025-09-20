Công cụ Phân tích Văn bản NLP
Đây là một ứng dụng web đơn giản được xây dựng bằng Streamlit và SpaCy để thực hiện phân tích văn bản cơ bản, bao gồm mã hóa (tokenization), gán nhãn từ loại (POS tagging) và nhận dạng thực thể được đặt tên (NER).

Yêu cầu
Python 3.8+

Các thư viện được liệt kê trong requirements.txt.

Cài đặt và Chạy ứng dụng
Tạo một môi trường ảo (khuyến khích):

python -m venv venv
source venv/bin/activate  # Trên Windows, dùng `venv\Scripts\activate`

Cài đặt các thư viện Python cần thiết:
Mở terminal và chạy lệnh sau:

pip install -r requirements.txt

Tải mô hình ngôn ngữ của SpaCy:
Ứng dụng này sử dụng mô hình tiếng Anh en_core_web_sm. Chạy lệnh sau để tải nó:

python -m spacy download en_core_web_sm

Chạy ứng dụng Streamlit:
Sau khi cài đặt xong, chạy lệnh sau trong terminal:

streamlit run text_analyzer_app.py

Mở trình duyệt:
Trình duyệt web của bạn sẽ tự động mở một tab mới với địa chỉ như http://localhost:8501. Bây giờ bạn có thể bắt đầu sử dụng ứng dụng!

Cách sử dụng
Nhập một đoạn văn bản bằng tiếng Anh vào hộp văn bản.

Nhấn nút "Phân tích Văn bản".

Kết quả sẽ được hiển thị trong ba tab riêng biệt:

Mã hóa (Tokens): Danh sách các token đã được tách ra từ văn bản.

Gán nhãn Từ loại (POS): Bảng chi tiết về từ loại của mỗi token.

Nhận dạng Thực thể (NER): Bảng liệt kê các thực thể được đặt tên đã được xác định.

Xử lý sự cố (Troubleshooting)
Lỗi ModuleNotFoundError: No module named 'spacy' (hoặc 'streamlit')
Lỗi này thường xảy ra khi bạn cài đặt các thư viện vào một môi trường Python khác với môi trường đang được dùng để chạy ứng dụng.

Nguyên nhân: Máy tính của bạn có thể có nhiều phiên bản Python. Bạn có thể đã cài đặt thư viện vào phiên bản hệ thống, nhưng lại đang chạy ứng dụng bằng phiên bản của Anaconda (hoặc ngược lại).

Giải pháp:

Luôn sử dụng Môi trường ảo (venv): Đây là cách tốt nhất để tránh xung đột.

Đảm bảo bạn đã kích hoạt môi trường ảo trước khi chạy BẤT KỲ lệnh nào khác. Bạn phải thấy (venv) ở đầu dòng lệnh trong terminal.

Thực hiện tất cả các lệnh (pip install, python -m spacy download, streamlit run) trong cùng một cửa sổ terminal sau khi đã kích hoạt môi trường ảo. Nếu bạn mở một terminal mới, bạn phải kích hoạt lại môi trường ảo.
