# MediCare AI | AI-Powered Healthcare Prediction System

## Overview
MediCare AI is a machine learning-based healthcare prediction project that analyzes user-provided symptoms to predict a possible disease and provide relevant medicine recommendations. It combines a web interface with a Flask backend and machine learning models.

**Disclaimer:** This project is for educational purposes only and is not a substitute for professional medical advice or diagnosis.

## Features
- Symptom-based disease prediction
- Machine learning classification
- Medicine recommendation functionality
- Web-based user interface
- Flask API for frontend-backend communication

## Technologies Used
- Python
- Flask and Flask-CORS
- Pandas and NumPy
- Scikit-learn
- Joblib
- HTML, CSS and JavaScript

## Machine Learning
The project includes data preprocessing, model training, prediction, and evaluation using metrics such as accuracy, precision, recall, F1-score, and a confusion matrix.

The classifier achieved approximately **77% accuracy** on the evaluation dataset in the current training run. Results may vary with different datasets and train-test splits.

## Project Structure
```text
medicare-ai/
├── app.py
├── train_model.py
├── train_classifier.py
├── requirements.txt
├── best_model.pkl
├── disease_encoder.pkl
├── medicine_database.pkl
├── data/
└── templates/
    ├── index.html
    ├── about.html
    └── contact.html
```

## Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/heeradeepsingh5252/medicare-ai.git
   cd medicare-ai
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask application:
   ```bash
   python3 app.py
   ```

5. Open the local URL shown in your terminal.

## Deployment
The Flask application is deployed using Render.

**Live Demo:** Add your public Render URL here.

## Future Improvements
- Improve model performance and validate it on independent datasets
- Add stronger input validation and error handling
- Improve accessibility and mobile responsiveness
- Expand model evaluation and testing

## Author
Developed as a machine learning and web development project.
