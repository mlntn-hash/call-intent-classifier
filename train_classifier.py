import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.shape)
print(df['label'].value_counts())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

print("Train_size: ", len(X_train))
print("Test_size: ", len(X_test))

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print(X_train_vec.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)
print(predictions[:40])
print(list(y_test[:40]))

from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.3f}")

print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions, labels=model.classes_)
print("Confusion matrix:", model.classes_)
print(cm)

from visualize import plot_confusion_matrix
plot_confusion_matrix(cm, model.classes_)