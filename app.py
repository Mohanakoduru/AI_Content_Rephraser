import streamlit as st
import os
from dotenv import load_dotenv
from groq_client import generate_response
from prompt_engine import build_prompt

# ---------- LOAD ENV ----------
load_dotenv()

st.set_page_config(
    page_title="AI Content Rephraser",
    layout="wide"
)




# ---------------- BACKGROUND + UI CSS ----------------
st.markdown("""
<style>
/* Fixed background image */
.stApp {
    background-image: url("https://th.bing.com/th/id/OIP.q7ZK-MtqVwFfzZ4Bb7Q5VQHaEo?w=292&h=182&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

/* Dark overlay */
.overlay {
    background-color: rgba(15, 23, 42, 0.70);
    padding: 20px;
    border-radius: 20px;
    color: white;
}

/* Chat container */
.chat-container {
    max-height: 420px;
    overflow-y: auto;
    padding: 10px;
}

/* User bubble */
.chat-user {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    padding: 12px 16px;
    border-radius: 16px 16px 4px 16px;
    margin: 10px 0 10px auto;
    max-width: 75%;
    width: fit-content;
    white-space: pre-wrap;
}

/* Bot bubble */
.chat-bot {
    background: #f9fafb;
    color: #111827;
    padding: 12px 16px;
    border-radius: 16px 16px 16px 4px;
    margin: 10px auto 10px 0;
    max-width: 75%;
    width: fit-content;
    box-shadow: 0 6px 20px rgba(0,0,0,0.18);
    white-space: pre-wrap;
}

/* Text area styling */
textarea {
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)



# ---------- SIDEBAR ----------
st.sidebar.title("Settings")

use_client_key = st.sidebar.toggle("Use your own Groq API key")

if use_client_key:
    api_key = st.sidebar.text_input(
        "Enter Groq API Key",
        type="password"
    )
else:
    api_key = os.getenv("GROQ_API_KEY")

# ---------- HEADER ----------
st.title("AI Content Rephraser")
st.write("Turn one caption into five high-quality content versions")

# ---------- INPUT ----------
user_input = st.text_area(
    "Enter your caption",
    height=150,
    placeholder="Type or paste your content here..."
)

# ---------- HELPER FUNCTION ----------
def extract_section(text, label):
    start = text.find(label)
    if start == -1:
        return "Error: content not generated"

    start += len(label)
    end = text.find("<<<END>>>", start)
    return text[start:end].strip()

# ---------- ACTION ----------
if st.button("Generate Content"):
    if not user_input.strip():
        st.warning("Please enter content.")
    elif not api_key:
        st.error("API key is missing.")
    else:
        with st.spinner("Generating professional content..."):
            prompt = build_prompt(user_input)
            result = generate_response(prompt, api_key)

        viral = extract_section(result, "VIRAL:")
        short = extract_section(result, "SHORT:")
        emotional = extract_section(result, "EMOTIONAL:")
        seo = extract_section(result, "SEO:")
        kpop = extract_section(result, "KPOP:")

        outputs = {
            "Viral Version": viral,
            "Short Version": short,
            "Emotional Version": emotional,
            "SEO Version": seo,
            "K-pop Style Version": kpop
        }

        st.divider()

        all_text = ""

        for title, content in outputs.items():
            st.subheader(title)

            st.text_area(
                label=f"{title} Output",
                value=content,
                height=120,
                key=title
            )

            st.download_button(
                label=f"Download {title}",
                data=content,
                file_name=f"{title.replace(' ', '_').lower()}.txt",
                mime="text/plain"
            )

            all_text += f"{title}\n{content}\n\n"

        st.download_button(
            "Download All Versions (.txt)",
            data=all_text,
            file_name="ai_content_rephraser_output.txt",
            mime="text/plain"
        )



# ---------- FOOTER ----------
st.markdown(
    """
    <hr style="margin-top:50px;">
    <div style="text-align:center; font-size:14px; color:gray;">
        Built by @MOHAN KODURU  2025
    </div>
    """,
    unsafe_allow_html=True
)
