from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load your model and TF-IDF vectorizer
model = joblib.load('../model/linear_svc_model.pkl')
vectorizer = joblib.load('../model/vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        new_complaint = request.form['complaint']
        # Perform TF-IDF vectorization
        complaint_vectorized = vectorizer.transform([new_complaint])
        # Make prediction
        prediction = model.predict(complaint_vectorized)
        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
