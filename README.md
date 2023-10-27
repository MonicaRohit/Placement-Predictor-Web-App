# Placement-Predictor-Web-App
Streamlit app: Predict student placement &amp; salary using ML models with user input.

Welcome to the Placement Predictor Web App, an interactive tool for predicting student placements and estimated salaries. This web application is built with Streamlit and utilizes machine learning models and preprocessed data for making predictions.

## How to Use

1. **Installation**

   First, ensure you have the necessary dependencies installed:

   - Python
   - Streamlit
   - NumPy
   - Pickle (for model loading)

   You can install Streamlit and NumPy using `pip`:

   ```bash
   pip install streamlit numpy
    ```
1. Running the App

-Run the app using the streamlit run command in your terminal:
```bash
streamlit run placement_predictor.py
```
2. Input Student Details

- Use the form provided in the web app to enter student details, including gender, academic scores, degree field, work experience, and more.

3. Get Predictions

- Click the "Predict" button to obtain predictions for student placement and the expected salary if placed.

## Customization

The app can be customized to suit your specific use case. You can modify the machine learning models, preprocessing steps, or add more input fields to the form as needed.

## Data and Models

The app uses machine learning models for prediction. The trained models and preprocessed data are loaded from the following files:

- placed.pkl: Model for placement prediction.
- preprocess.pkl: Data preprocessing scaler.
- model.pkl: Model for salary prediction (used when placement is predicted).

You can replace these files with your own models and data for customization.
