# 📩 Spam vs Ham Classification System (End-to-End ML Project)

## 🚀 Overview

This project is a complete end-to-end machine learning system designed to classify text messages as **Spam** or **Ham (Not Spam)**.
It demonstrates the full ML lifecycle — from data preprocessing and model training to deployment using a **Flask API** and an interactive **Streamlit frontend**.

The system evaluates multiple machine learning models and automatically selects the best-performing model for accurate predictions.

---

## 🎯 Features

* 🔍 Multi-model training and evaluation
* 🧠 Automatic best model selection
* ⚡ TF-IDF based text vectorization
* 🌐 REST API using Flask
* 💻 Interactive UI with Streamlit
* 💾 Model persistence using Pickle
* 📊 Scalable and deployment-ready architecture

---

## 🧠 Tech Stack

| Category      | Tools Used    |
| ------------- | ------------- |
| Language      | Python        |
| ML Libraries  | Scikit-learn  |
| Data Handling | Pandas, NumPy |
| Backend       | Flask         |
| Frontend      | Streamlit     |
| Model Storage | Pickle        |

---

## 📂 Project Structure

```
spam_project/
│
├── data/
│   └── SMSSpamCollection.txt
│
├── notebooks/
│   └── model_training.ipynb
│
├── models/
│   ├── best_model.pkl
│   └── vectorizer.pkl
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. **Data Preprocessing**

   * Raw text messages are cleaned and prepared
   * Labels (Spam/Ham) are encoded

2. **Feature Engineering**

   * Text is converted into numerical form using **TF-IDF Vectorization**

3. **Model Training**

   * Multiple models are trained:

     * Naive Bayes
     * Logistic Regression
     * Support Vector Machine (SVM)
     * Random Forest

4. **Model Selection**

   * Best model is selected based on accuracy

5. **Deployment**

   * Flask API serves predictions
   * Streamlit UI provides user interaction

---

## 🏃‍♂️ Getting Started

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the Model

Run the Jupyter Notebook:

```
notebooks/model_training.ipynb
```

This will generate:

* `models/best_model.pkl`
* `models/vectorizer.pkl`

---

### 4️⃣ Run Flask Backend

```
cd backend
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

### 5️⃣ Run Streamlit Frontend

Open a new terminal:

```
cd frontend
streamlit run streamlit_app.py
```

---

## 🔌 API Documentation

### POST `/predict`

#### Request:

```
{
  "message": "Congratulations! You won a free prize!"
}
```

#### Response:

```
{
  "prediction": "Spam"
}
```

---

## 🧪 Example Inputs

### ✅ Ham Message

```
Hey, are we meeting tomorrow for the project discussion?
```

### 🚨 Spam Message

```
Congratulations! You have won ₹10,00,000. Click here to claim now!
```

---

## 📊 Models Used

| Model               | Description                         |
| ------------------- | ----------------------------------- |
| Naive Bayes         | Best suited for text classification |
| Logistic Regression | Baseline linear model               |
| SVM (LinearSVC)     | High-performance classifier         |
| Random Forest       | Ensemble learning method            |

---

## 🎯 Use Cases

* Email/SMS spam detection
* Fraud message filtering
* Content moderation systems
* Customer communication analysis