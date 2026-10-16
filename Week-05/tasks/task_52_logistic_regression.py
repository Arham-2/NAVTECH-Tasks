from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the digits dataset (MNIST handwritten digits)
digits = load_digits()
print("Image Data Shape:", digits.data.shape)
print("Label Data Shape:", digits.target.shape)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=0
)

# Create and train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict for test dataset
predictions = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, predictions)
print("\nAccuracy Score:", accuracy)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix:\n", conf_matrix)

# Classification Report
print("\nClassification Report:\n", classification_report(y_test, predictions))
