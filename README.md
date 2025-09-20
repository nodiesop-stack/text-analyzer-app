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

