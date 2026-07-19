import json
import pandas as pd
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/mcq/generate"

st.set_page_config(
    page_title="AI Powered MCQ Generator",
    page_icon="🧠",
    layout="wide",
)

st.sidebar.title("⚙️ Settings")

st.sidebar.markdown("""
### AI Pipeline

- 📄 PDF Upload
- ✂️ Text Chunking
- 🧠 Gemini Embeddings
- 🗂️ ChromaDB
- 🔍 RAG Retrieval
- 🤖 Gemini LLM
- ✅ Structured Output
""")

st.title("🧠 AI-Powered MCQ Generator")

st.caption(
    "Powered by LangChain • Gemini • ChromaDB • RAG"
)

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
)

difficulty = st.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard",
    ],
)

num_questions = st.slider(
    "Number of Questions",
    min_value=1,
    max_value=20,
    value=5,
)

if st.button(
    "🚀 Generate MCQs",
    use_container_width=True,
):

    if uploaded_file is None:

        st.warning("Please upload a PDF.")

    else:

        with st.spinner("Generating MCQs..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf",
                )
            }

            data = {
                "difficulty": difficulty,
                "num_questions": num_questions,
            }

            st.write("Calling API:", API_URL)

            try:

                response = requests.post(
                    API_URL,
                    files=files,
                    data=data,
                    timeout=120,
                )

                st.write("Status Code:", response.status_code)

            except Exception as e:

                st.exception(e)
                st.stop()

            if response.status_code == 200:

                result = response.json()

                st.success("MCQs Generated Successfully!")

                # -------------------------------
                # Download Buttons
                # -------------------------------

                col1, col2 = st.columns(2)

                with col1:

                    st.download_button(
                        label="⬇ Download JSON",
                        data=json.dumps(result, indent=4),
                        file_name="mcqs.json",
                        mime="application/json",
                        use_container_width=True,
                    )

                with col2:

                    df = pd.DataFrame(result["mcqs"])

                    st.download_button(
                        label="⬇ Download CSV",
                        data=df.to_csv(index=False),
                        file_name="mcqs.csv",
                        mime="text/csv",
                        use_container_width=True,
                    )

                for index, mcq in enumerate(result["mcqs"], start=1):

                    with st.expander(f"📘 Question {index}", expanded=True):

                        st.markdown(f"### {mcq['question']}")

                        st.markdown(f"**A.** {mcq['option_a']}")
                        st.markdown(f"**B.** {mcq['option_b']}")
                        st.markdown(f"**C.** {mcq['option_c']}")
                        st.markdown(f"**D.** {mcq['option_d']}")

                        st.success(
                            f"✅ Correct Answer: {mcq['answer']}) {mcq['correct_option']}"
                        )

                        st.info(
                            f"💡 {mcq['explanation']}"
                        )

            else:

                st.error(response.text)

st.markdown("---")

st.caption(
    "Built with ❤️ using Python • FastAPI • LangChain • Google Gemini • ChromaDB • Streamlit"
)