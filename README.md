


---

<div align="center">

# 🩺 Diabetes Prediction Web App  
### Predict Diabetes Risk Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-ML%20Model-orange)
![Flask](https://img.shields.io/badge/Flask-Backend-blueviolet)
![License](https://img.shields.io/badge/License-Open%20Source-success)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

</div>

---

## 📘 Overview

**DiabetesPredictionApp** is a machine-learning-based web application that predicts the probability of diabetes based on user health metrics.  
It uses a trained model (`diabetes_model2.h5`) supported by preprocessing pipelines (scalers & encoders) for real-time inference.

This project demonstrates the integration of ML models into a production-ready web application environment.

> ⚠️ *For educational & research purposes only — not a medical diagnostic tool.*

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🧠 ML-based prediction | Predict diabetes likelihood via trained neural model |
| 🔧 Pre-processing | Encoders & scalers for categorical & numerical data |
| 🌐 Web Interface | User inputs processed in real time |
| 🚀 Deployable | Includes `Procfile` & configurations for cloud hosting |
| 📁 Ready-to-use | Clone → Install → Run locally |

---

## 🗂 Project Structure

Diabetespredictionapp/ 
├── application.py                # Main Flask Application Entry 
├── main.py                       # Optional project runner 
├── diabetes_model2.h5            # Machine Learning Model 
├── scaler2.pkl                   # Numerical Feature Scaler 
├── gender_encoder.pkl            # Gender Label Encoder
├── smoking_history_encoder.pkl   # Smoking Label Encoder 
├── assets/                       # Static UI files 
├── app/                          # Core prediction & routing logic 
├── config.py                     # Project configuration 
├── requirements.txt              # Dependencies 
├── Procfile                      # Deployment config └── .ebextensions/                # AWS deployment config

---

## 🛠 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/ashrafaliqhtan/Diabetespredictionapp.git
cd Diabetespredictionapp

2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3. Install Requirements

pip install -r requirements.txt

```
---

▶️ Run the Application Locally
```
python application.py       # Or: python main.py
```
Then visit:

http://127.0.0.1:5000/


---

🔍 How the Prediction Works

1. User enters health-related attributes (BMI, glucose level, age, smoking status, etc.)


2. Input is preprocessed using pickled encoders/scalers


3. Data is fed into the trained ML model


4. Probability of diabetes is generated & displayed visually in UI



> Model performance depends on dataset quality and preprocessing pipeline.




---

🌍 Deployment

This project can be deployed on:

Platform	Status

Heroku	✔ Supported
AWS Elastic Beanstalk	✔ Supported
Docker	🔜 Possible
Local Machine	✔ Recommended for testing


Example deploy command (Heroku):
```
heroku create
git push heroku main
heroku open

```
---

📦 Requirements

Common dependencies include:
```
Flask
numpy
pandas
tensorflow / keras
scikit-learn
pickle
gunicorn (for deployment)

```
---

💡 Future Improvements

🖥 Enhanced UI/UX with charts & visualization

📊 Model retraining option from uploaded CSV

🔐 User accounts & cloud-stored prediction history

📱 Mobile-friendly responsive frontend



---

🤝 Contributing

Contributions, issues & feature requests are welcome.
```
git checkout -b feature-branch
git commit -m "Feature update"
git push origin feature-branch

```
---

📜 License

This project is open-source. Feel free to use & improve it with credit.


---

❤️ Acknowledgments

Special thanks to open-source ML communities and diabetes datasets research projects.

> Research example used for inspiration:
(e.g. Pima Indians Diabetes Dataset – ML community resources)




---

<div align="center">⭐ If you like this project, give it a star on GitHub!

👉 Visit Repository

</div>
---

