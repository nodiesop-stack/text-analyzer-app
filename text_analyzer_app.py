import streamlit as st
import spacy
import pandas as pd

# Tải mô hình ngôn ngữ tiếng Anh của SpaCy
# Sử dụng cache của Streamlit để không phải tải lại mô hình mỗi lần tương tác
@st.cache_resource
def load_model():
    """Tải và trả về mô hình SpaCy."""
    # Bạn cần chạy 'python -m spacy download en_core_web_sm' trong terminal trước
    return spacy.load("en_core_web_sm")

nlp = load_model()

# --- Giao diện người dùng (UI) của ứng dụng ---

st.set_page_config(layout="wide", page_title="Công cụ Phân tích Văn bản", page_icon="📝")

st.title("📝 Công cụ Phân tích Văn bản NLP")
st.markdown("""
    Ứng dụng này sử dụng **SpaCy** để thực hiện các tác vụ xử lý ngôn ngữ tự nhiên (NLP) cơ bản.
    Nhập một đoạn văn bản bằng tiếng Anh vào ô bên dưới và nhấn "Phân tích" để xem kết quả.
""")

# Khu vực nhập văn bản từ người dùng
default_text = "Apple is looking at buying a U.K. startup for $1 billion in London. Tim Cook is the CEO."
user_text = st.text_area("Nhập văn bản của bạn vào đây:", default_text, height=150)

# Nút để bắt đầu phân tích
if st.button("Phân tích Văn bản"):
    if user_text:
        # Xử lý văn bản bằng mô hình SpaCy
        doc = nlp(user_text)

        st.success("Đã phân tích văn bản thành công! Dưới đây là kết quả:")

        # Chia giao diện thành các tab để dễ xem
        tab1, tab2, tab3 = st.tabs(["1️⃣ Mã hóa (Tokens)", "2️⃣ Gán nhãn Từ loại (POS)", "3️⃣ Nhận dạng Thực thể (NER)"])

        # --- Tab 1: Hiển thị Tokens ---
        with tab1:
            st.header("Danh sách các Tokens")
            st.info("Mã hóa (Tokenization) là quá trình tách văn bản thành các đơn vị nhỏ hơn gọi là token (từ, dấu câu, v.v.).")
            
            # Chuyển tokens thành một chuỗi dễ đọc
            tokens = [token.text for token in doc]
            st.code(", ".join(tokens), language=None)
            st.write(f"**Tổng số tokens:** {len(tokens)}")


        # --- Tab 2: Hiển thị Part-of-Speech (POS) Tagging ---
        with tab2:
            st.header("Gán nhãn Từ loại (Part-of-Speech)")
            st.info("POS Tagging xác định vai trò ngữ pháp của mỗi token (ví dụ: danh từ, động từ, tính từ).")
            
            pos_data = []
            for token in doc:
                pos_data.append({
                    "Token": token.text,
                    "Từ loại (Coarse)": token.pos_,
                    "Nhãn chi tiết (Fine)": token.tag_,
                    "Giải thích": spacy.explain(token.pos_)
                })
            
            df_pos = pd.DataFrame(pos_data)
            st.dataframe(df_pos, use_container_width=True)


        # --- Tab 3: Hiển thị Named Entity Recognition (NER) ---
        with tab3:
            st.header("Nhận dạng Thực thể được đặt tên (Named Entities)")
            st.info("NER tìm và phân loại các thực thể trong văn bản như tên người, tổ chức, địa điểm, ngày tháng, v.v.")
            
            entities = []
            for ent in doc.ents:
                entities.append({
                    "Thực thể": ent.text,
                    "Nhãn": ent.label_,
                    "Giải thích": spacy.explain(ent.label_)
                })

            if entities:
                df_ner = pd.DataFrame(entities)
                st.dataframe(df_ner, use_container_width=True)
            else:
                st.warning("Không tìm thấy thực thể được đặt tên nào trong văn bản.")

    else:
        st.warning("Vui lòng nhập văn bản để phân tích.")

st.sidebar.header("Về ứng dụng")
st.sidebar.markdown("""
    **Tác giả:** Nhóm 09-Thien-Tung
    **Công nghệ:** Python, Streamlit, SpaCy
    
    Đây là một dự án demo giúp minh họa các bước cốt lõi trong một quy trình NLP cổ điển.
""")
