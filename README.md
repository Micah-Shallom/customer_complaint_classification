### Customer Complaint Classification

This project focuses on classifying customer complaints into different categories using natural language processing (NLP) techniques and machine learning algorithms. By accurately categorizing complaints, businesses can efficiently address customer concerns and improve overall customer satisfaction.

#### Dataset
The dataset consists of customer complaints collected from various sources, such as customer service calls, emails, and online reviews. Each complaint is labeled with a specific category or issue, allowing for supervised learning-based classification.

#### Methodology
1. **Data Collection**: Customer complaints were gathered from multiple channels, including customer service databases, online forums, and social media platforms.
2. **Data Preprocessing**: Text preprocessing techniques were applied to clean and standardize the text data, including tokenization, stopword removal, and lemmatization.
3. **Exploratory Data Analysis (EDA)**: Exploratory data analysis was performed to understand the distribution of complaints across different categories and identify any patterns or trends.
4. **Feature Extraction**: Text features were extracted from the complaint text using techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
5. **Model Selection and Training**: Various machine learning models were evaluated for classification, including Naive Bayes, Logistic Regression, Support Vector Machines (SVM), and Neural Networks. Hyperparameter tuning was conducted to optimize model performance.
6. **Model Evaluation**: The trained models were evaluated using metrics such as accuracy, precision, recall, and F1-score to assess their performance in classifying customer complaints.
7. **Model Deployment**: The best-performing model was deployed using a web-based application, allowing users to input their complaints and receive predictions about the likely category or issue.

#### Repository Structure
- **data/**: Contains the dataset used for training and testing the classification models.
- **models/**: Stores the trained machine learning models.
- **notebooks/**: Jupyter notebooks used for data preprocessing, model training, and evaluation.
- **app.py**: Flask application for model deployment.
- **templates/**: HTML templates for the web application.
- **static/**: Contains CSS stylesheets and images for the web application.

#### Usage
1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python server.py`
4. Access the web application in your browser at `http://localhost:5000`

