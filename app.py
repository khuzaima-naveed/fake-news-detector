# import streamlit as st
# from utils.predictor import Predictor

# # Load model and vectorizer
# predictor = Predictor("model/fake_news_model.pkl", "model/vectorizer.pkl")

# # Streamlit App UI
# st.set_page_config(page_title="Fake News Detector", layout="centered")

# st.title("📰 Fake News Detector App")
# st.write("Enter a news article below, and I'll tell you if it's **Real** or **Fake**!")

# news_input = st.text_area("✏️ Paste your news content here:")

# if st.button("🔍 Detect"):
#     if news_input.strip() == "":
#         st.warning("⚠️ Please enter some news text.")
#     else:
#         result = predictor.predict(news_input)
#         st.success(f"🧠 Prediction: **{result}**")



import streamlit as st
from utils.predictor import Predictor

class NewsDetectorApp:
    def __init__(self):
        self.predictor = Predictor("model/fake_news_model.pkl", "model/vectorizer.pkl")

    def run(self):
        st.set_page_config(page_title="Fake News Detector", layout="centered")
        st.title("📰 Fake News Detector App")
        st.write("Paste any news content below to check if it's real or fake:")

        news_text = st.text_area("Enter News Content")

        if st.button("Detect"):
            if not news_text.strip():
                st.warning("Please enter some news text.")
            else:
                result = self.predictor.predict(news_text)
                st.success(f"Prediction: **{result}**")

if __name__ == "__main__":
    app = NewsDetectorApp()
    app.run()
