# import re
# import string


# class Preprocessor:
#     def clean_text(self, text):
#         text = text.lower()
#         text = re.sub(r"http\S+", "", text)  # remove URLs
#         text = re.sub(r"<.*?>", "", text)  # remove HTML tags
#         text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
#         text = re.sub(r"\d+", "", text)  # remove numbers
#         text = re.sub(r"\s+", " ", text).strip()
#         return text


import re
import string

class Preprocessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>+', '', text)
        text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\w*\d\w*', '', text)
        return text
