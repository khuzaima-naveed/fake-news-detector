# import joblib
# from utils.preprocessor import Preprocessor

# class Predictor:
#     def __init__(self, model_path, vectorizer_path):
#         self.model = joblib.load(model_path)
#         self.vectorizer = joblib.load(vectorizer_path)
#         self.preprocessor = Preprocessor()

#     def predict(self, text):
#         cleaned_text = self.preprocessor.clean_text(text)
#         vectorized_text = self.vectorizer.transform([cleaned_text])
#         prediction = self.model.predict(vectorized_text)
#         return "Real News" if prediction[0] == 1 else "Fake News"



import joblib
from utils.preprocessor import Preprocessor

class Predictor:
    def __init__(self, model_path, vectorizer_path):
        self._load_model(model_path)
        self._load_vectorizer(vectorizer_path)
        self.preprocessor = Preprocessor()

    def _load_model(self, path):
        self.model = joblib.load(path)

    def _load_vectorizer(self, path):
        self.vectorizer = joblib.load(path)

    def predict(self, text):
        clean = self.preprocessor.clean_text(text)
        vector = self.vectorizer.transform([clean])
        result = self.model.predict(vector)[0]
        return "Real News" if result == 1 else "Fake News"
