# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import PassiveAggressiveClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import joblib
# import os

# # Step 1: Load Data
# fake = pd.read_csv('data/Fake.csv')   # Fake news
# real = pd.read_csv('data/True.csv')   # Real news

# # Step 2: Label Data
# fake['label'] = 0   # 0 for fake
# real['label'] = 1   # 1 for real

# # Step 3: Combine both datasets
# data = pd.concat([fake, real])
# data = data[['text', 'label']]   # Keep only relevant columns

# # Step 4: Split into train/test sets
# X_train, X_test, y_train, y_test = train_test_split(
#     data['text'], data['label'], test_size=0.2, random_state=42)

# # Step 5: Convert text into numbers (TF-IDF)
# vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# # Step 6: Train model
# model = PassiveAggressiveClassifier()
# model.fit(X_train_vec, y_train)

# # Step 7: Save model and vectorizer
# os.makedirs('model', exist_ok=True)
# joblib.dump(model, 'model/fake_news_model.pkl')
# joblib.dump(vectorizer, 'model/vectorizer.pkl')

# # Step 8: Print accuracy (optional)
# accuracy = accuracy_score(y_test, model.predict(X_test_vec))
# print("Model Accuracy:", accuracy)


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Load data
fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

# Label data
fake["label"] = 0
true["label"] = 1

# Combine
data = pd.concat([fake, true])[["text", "label"]]

# Split
X_train, X_test, y_train, y_test = train_test_split(data["text"], data["label"], test_size=0.2)

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Save
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/fake_news_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model trained & saved successfully.")
