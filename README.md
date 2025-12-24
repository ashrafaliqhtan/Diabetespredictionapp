# 🩺 Diabetes Prediction Web Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3+-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-blue?style=for-the-badge)

**An Advanced AI-Powered Platform for Early Diabetes Detection and Risk Assessment**

[![Live Demo](https://img.shields.io/badge/Live_Demo-Click_Here-red?style=for-the-badge)](https://github.com/ashrafaliqhtan/Diabetespredictionapp)
[![Documentation](https://img.shields.io/badge/Documentation-Read_Here-blue?style=for-the-badge)](DOCUMENTATION.md)
[![Paper](https://img.shields.io/badge/Research_Paper-View_Here-green?style=for-the-badge)](RESEARCH.md)

</div>

## 📋 Project Overview

The **Diabetes Prediction Web Application** is an AI-powered diagnostic tool that leverages deep learning models to predict the likelihood of diabetes mellitus. The application provides three distinct predictive models based on different data types: symptoms, laboratory measurements, and lifestyle factors. Built with a Flask backend and modern web technologies, it offers an accessible, user-friendly interface for early diabetes risk assessment.

## ✨ Key Features

### 🔍 **Multi-Model Prediction System**
- **Symptoms-Based Model**: Uses observable clinical symptoms (polyuria, polydipsia, weight loss, etc.)
- **Laboratory Measurements Model**: Based on Pima Indian Diabetes Dataset (glucose, insulin, BMI, etc.)
- **Lifestyle Factors Model**: Considers risk factors (smoking, hypertension, heart disease, etc.)

### 🌐 **Web Application Features**
- **Bilingual Interface**: Full support for English and Arabic
- **Interactive Forms**: User-friendly input interfaces for all three models
- **Visual Analytics**: Comprehensive data visualizations and correlation matrices
- **Detailed Reporting**: Individualized risk assessment reports
- **Responsive Design**: Accessible on desktop and mobile devices

### 📊 **Technical Capabilities**
- **High Accuracy Models**: Up to 97.35% accuracy on lifestyle factors model
- **Real-time Predictions**: Instant results with confidence scores
- **Data Visualization**: Interactive plots and statistical analyses
- **Model Comparison**: Side-by-side performance evaluation

## 🏗️ System Architecture

### **Technology Stack**
```
Frontend:
├── HTML5/CSS3
├── JavaScript (Chart.js, Plotly)
├── Bootstrap 5
└── Jinja2 Templating

Backend:
├── Flask (Python Web Framework)
├── TensorFlow/Keras (Deep Learning)
├── Scikit-learn (Machine Learning)
└── Pandas/NumPy (Data Processing)

Development Tools:
├── Jupyter Notebook
├── VS Code/PyCharm
├── Git/GitHub
└── PlantUML (Diagram Generation)
```

### **File Structure**
```
diabetespredictionapp/
├── app/
│   ├── models/              # Trained ML models
│   ├── static/              # CSS, JS, images
│   ├── templates/           # HTML templates
│   ├── data/                # Datasets
│   └── routes.py            # Flask routes
├── notebooks/               # Jupyter notebooks for model development
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md               # This file
```

## 📈 Model Performance

### **Comparative Results**

| Model Type | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|------------|----------|-----------|---------|----------|---------|
| Symptoms-Based | 91.53% | 0.92 | 0.91 | 0.915 | 0.93 |
| Laboratory Measurements | 79.27% | 0.85 | 0.84 | 0.80 | 0.79 |
| Lifestyle Factors | **97.35%** | **1.00** | **0.69** | **0.82** | **0.85** |

### **Key Insights**
- **Lifestyle Factors Model** showed superior performance with 97.35% accuracy
- **Symptoms Model** provides good balance for non-invasive screening
- **Laboratory Model** offers reliable predictions when clinical data is available

## 🚀 Installation & Setup

### **Prerequisites**
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

### **Step-by-Step Installation**

1. **Clone the Repository**
```bash
git clone https://github.com/ashrafaliqhtan/Diabetespredictionapp.git
cd Diabetespredictionapp
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
python run.py
```

5. **Access the Application**
Open your browser and navigate to: `http://localhost:5000`

## 🧪 Using the Application

### **Prediction Workflow**
1. **Select Prediction Type**: Choose from Symptoms, Laboratory, or Lifestyle models
2. **Input Data**: Fill in the required fields in the intuitive forms
3. **Get Results**: View instant predictions with confidence scores
4. **Review Reports**: Access detailed analysis and visualizations
5. **Compare Models**: Evaluate different risk factors and their impact

### **Input Requirements**

#### **Symptoms Model**
- Age, Gender
- Clinical symptoms (Polyuria, Polydipsia, Weight Loss, etc.)
- Obesity status

#### **Laboratory Model**
- Pregnancies count
- Glucose level
- Blood Pressure
- Skin Thickness
- Insulin level
- BMI
- Diabetes Pedigree Function
- Age

#### **Lifestyle Model**
- Demographic information
- Medical history (Hypertension, Heart Disease)
- Smoking history
- BMI, HbA1c level
- Blood glucose level

## 🔬 Technical Methodology

### **Data Processing Pipeline**
1. **Data Collection**: Multi-source aggregation from hospitals, surveys, and public datasets
2. **Preprocessing**: Handling missing values, normalization, feature engineering
3. **Exploratory Analysis**: Statistical analysis and pattern discovery
4. **Model Training**: Deep Neural Networks with hyperparameter optimization
5. **Validation**: Cross-validation and performance metric evaluation

### **Model Architectures**
- **Deep Neural Networks** with multiple hidden layers
- **Dropout Regularization** to prevent overfitting
- **Early Stopping** for optimal training epochs
- **Adam Optimizer** for efficient gradient descent

## 📊 Data Analysis & Visualization

### **Symptoms Model Data Analysis**

![Polydipsia Distribution](IMAGES/image14.png)
*Figure: Distribution of polydipsia (excessive thirst) symptom*

![Obesity Distribution](IMAGES/image15.png)
*Figure: Distribution of obesity among participants*

![Gender Distribution Analysis](IMAGES/image16.png)
*Figure: Detailed gender distribution analysis*

![Age Distribution Analysis](IMAGES/image17.png)
*Figure: Detailed age distribution analysis*

![Symptom Distribution Analysis](IMAGES/image18.png)
*Figure: Comprehensive symptom distribution analysis*

![Data Cleaning Process](IMAGES/image19.png)
*Figure: Data cleaning and preparation workflow*

![Model Training Process](IMAGES/image20.png)
*Figure: Model training and validation process*

### **Laboratory Measurements Model**

![Summary Statistics](IMAGES/image21.png)
*Figure: Summary statistics of Pima Indian Diabetes Dataset*

![Age Distribution](IMAGES/image22.png)
*Figure: Age distribution in laboratory dataset*

![Blood Pressure Distribution](IMAGES/image23.png)
*Figure: Blood pressure distribution analysis*

![BMI Distribution](IMAGES/image24.png)
*Figure: Body Mass Index distribution analysis*

![Glucose Distribution](IMAGES/image25.png)
*Figure: Glucose level distribution analysis*

![Age vs Outcome Box Plot](IMAGES/image26.png)
*Figure: Age vs diabetes outcome box plot analysis*

![Age vs Outcome Violin Plot](IMAGES/image27.png)
*Figure: Age vs diabetes outcome violin plot*

![BMI vs Outcome Box Plot](IMAGES/image28.png)
*Figure: BMI vs diabetes outcome box plot analysis*

![BMI vs Outcome Detailed](IMAGES/image29.png)
*Figure: Detailed BMI vs diabetes outcome analysis*

![Glucose vs BMI Scatter](IMAGES/image30.png)
*Figure: Glucose level vs BMI scatter plot*

![Age, Glucose, BMI Scatter](IMAGES/image31.png)
*Figure: 3D scatter plot of age, glucose, and BMI*

![Inter-variable Relationships](IMAGES/image32.png)
*Figure: Inter-variable relationship matrix*

![Correlation Matrix](IMAGES/image33.png)
*Figure: Correlation matrix of all features*

### **Lifestyle Factors Model**

![Lifestyle Factors Model](IMAGES/image34.png)
*Figure: Lifestyle factors model overview*

![Summary Statistics](IMAGES/image35.jpeg)
*Figure: Summary statistics of lifestyle dataset*

![Feature Distribution](IMAGES/image36.png)
*Figure: Feature distribution analysis*

![Age and Gender Distribution](IMAGES/image37.png)
*Figure: Age and gender distribution analysis*

![Additional Distribution Analysis](IMAGES/image38.png)
*Figure: Additional distribution analysis*

![Correlation Matrix](IMAGES/image39.png)
*Figure: Correlation matrix for lifestyle factors*

![Neural Network Architecture](IMAGES/image40.png)
*Figure: Neural network architecture diagram*

### **Web Application Interface**

![File Structure](IMAGES/image41.png)
*Figure: Project file structure*

![Home Page English](IMAGES/image42.png)
*Figure: Home page (English version)*

![Home Page Arabic](IMAGES/image43.png)
*Figure: Home page (Arabic version)*

![Symptom-Based Prediction Page](IMAGES/image44.png)
*Figure: Symptom-based prediction input form*

![Laboratory Measurements Prediction Page](IMAGES/image45.png)
*Figure: Laboratory measurements prediction input form*

![Lifestyle Factors Prediction Page](IMAGES/image46.png)
*Figure: Lifestyle factors prediction input form*

![Symptom-Based Result Page](IMAGES/image47.png)
*Figure: Symptom-based prediction results*

![Laboratory Measurements Result Page](IMAGES/image48.png)
*Figure: Laboratory measurements prediction results*

![Lifestyle Factors Result Page](IMAGES/image49.png)
*Figure: Lifestyle factors prediction results*

![Symptom-Based Report Page](IMAGES/image50.png)
*Figure: Symptom-based detailed report*

![Laboratory Measurements Report Page](IMAGES/image51.png)
*Figure: Laboratory measurements detailed report*

![Lifestyle Factors Report Page](IMAGES/image52.png)
*Figure: Lifestyle factors detailed report*

![Visualization Page](IMAGES/image53.png)
*Figure: Data visualization dashboard*

![About Page 1](IMAGES/image54.png)
*Figure: About page section 1*

![About Page 2](IMAGES/image55.png)
*Figure: About page section 2*

![About Page 3](IMAGES/image56.png)
*Figure: About page section 3*

![About Page 4](IMAGES/image57.png)
*Figure: About page section 4*

![About Page 5](IMAGES/image58.png)
*Figure: About page section 5*

![About Page 6](IMAGES/image59.png)
*Figure: About page section 6*

![About Page 7](IMAGES/image60.png)
*Figure: About page section 7*

### **Tools and Technologies**

| Icon | Description | Name of Tool, Program, or Technology |
|------|-------------|--------------------------------------|
| ![Python](IMAGES/image61.png) | Programming language used for developing the models and web application | Python |
| ![Flask](IMAGES/image62.png) | Micro web framework for Python used to build the web application | Flask |
| ![TensorFlow/Keras](IMAGES/image63.png) | Libraries for building and training deep learning models | TensorFlow/Keras |
| ![Scikit-learn](IMAGES/image64.png) | Library for machine learning and data preprocessing | Scikit-learn |
| ![NumPy](IMAGES/image65.png) | Library for numerical computations | NumPy |
| ![Pandas](IMAGES/image66.png) | Library for data manipulation and analysis | Pandas |
| ![Plotly](IMAGES/image67.png) | Library for creating interactive visualizations | Plotly |
| ![Jinja2](IMAGES/image68.png) | Template engine for Python used with Flask for rendering HTML | Jinja2 |
| ![Jupyter Notebook](IMAGES/image69.png) | Interactive environment for developing and documenting code | Jupyter Notebook |
| ![VS Code](IMAGES/image70.png) | Source code editor for programming and development | VS Code |
| ![Excel](IMAGES/image71.png) | Spreadsheet software used for data analysis and manipulation | Excel |
| ![Anaconda](IMAGES/image72.png) | Distribution of Python and R for scientific computing and data science | Anaconda |
| ![PlantUML](IMAGES/image73.png) | Tool for creating various diagrams using simple text | PlantUML |

### **System Design Diagrams**

![Use Case Diagram](IMAGES/image74.png)
*Figure: System use case diagram*

![Sequence Diagram](IMAGES/image75.svg)
*Figure: System sequence diagram*

![Component Diagram](IMAGES/image76.png)
*Figure: System component diagram*

![Composite Structure Diagram](IMAGES/image77.png)
*Figure: Composite structure diagram*

![State Machine Diagram](IMAGES/image78.png)
*Figure: State machine diagram*

![Architecture Diagram](IMAGES/image79.svg)
*Figure: System architecture diagram*

![Dynamic Diagram](IMAGES/image80.png)
*Figure: Dynamic system diagram*

### **Model Performance Results**

![Training and Validation Accuracy/Loss](IMAGES/image81.png)
*Figure: Symptoms model training and validation accuracy/loss*

![Model Accuracy Plot](IMAGES/image82.png)
*Figure: Model accuracy over training epochs*

![Model Loss Plot](IMAGES/image83.png)
*Figure: Model loss over training epochs*

![Laboratory Model Training](IMAGES/image84.png)
*Figure: Laboratory model training and validation metrics*

![Precision-Recall Curve](IMAGES/image85.png)
*Figure: Precision-recall curve for lifestyle model*

![ROC Curve](IMAGES/image86.png)
*Figure: ROC curve for lifestyle model*

## 🎯 Use Cases

### **Healthcare Applications**
- **Primary Care Screening**: Rapid preliminary assessment for physicians
- **Patient Self-Monitoring**: Personal health risk evaluation
- **Public Health Initiatives**: Population-level risk factor analysis
- **Medical Education**: Teaching tool for diabetes risk factors

### **User Scenarios**
1. **Individuals**: Self-assessment of diabetes risk
2. **Healthcare Providers**: Clinical decision support
3. **Researchers**: Model validation and comparison
4. **Public Health Officials**: Population risk analysis

## 🔮 Future Enhancements

### **Planned Features**
- **Mobile Application**: iOS and Android native apps
- **API Integration**: RESTful API for third-party integration
- **Electronic Health Record (EHR) Integration**: Direct data import from healthcare systems
- **Advanced Analytics**: Longitudinal tracking and trend analysis
- **Multi-Language Support**: Additional language interfaces

### **Technical Improvements**
- **Ensemble Methods**: Combine predictions from multiple models
- **Explainable AI**: SHAP values for model interpretability
- **Real-time Data Processing**: Stream processing capabilities
- **Cloud Deployment**: Scalable cloud infrastructure

## 📚 Research Contribution

This project contributes to the field of medical AI by:
- Developing a comprehensive multi-model diabetes prediction system
- Demonstrating the efficacy of lifestyle factors in diabetes prediction
- Providing an open-source tool for researchers and practitioners
- Offering insights into feature importance across different prediction approaches

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### **Contribution Guidelines**
- Follow PEP 8 style guidelines for Python code
- Add comprehensive documentation for new features
- Include tests for new functionality
- Update the README.md as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Datasets**: Pima Indian Diabetes Dataset, Lifestyle Factors Dataset
- **Libraries**: TensorFlow, Flask, Scikit-learn, Pandas, NumPy
- **Research Support**: All contributors and test participants
- **Academic Guidance**: Faculty and advisors for research direction

## 📞 Support & Contact

For questions, issues, or collaboration opportunities:

- **GitHub Issues**: [Report a bug or request a feature](https://github.com/ashrafaliqhtan/Diabetespredictionapp/issues)
- **Documentation**: [Link to detailed documentation]

---

<div align="center">

**⚠️ Medical Disclaimer**

*This tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.*

</div>