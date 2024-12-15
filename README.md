# Heart Health Risk Prediction App

## Description
This is a user-friendly web application developed using Streamlit to help users:

1. **Predict the Risk of Heart Disease**: Based on medical details entered by the user, the app predicts whether the user is at risk of heart disease using a trained machine learning model.
2. **Visualize Data**: Explore interactive charts and visualizations created from historical heart disease patient data.

## Features

### 1. Home
- Overview of the app's purpose and functionalities.
- A welcoming interface with a brief description of the dataset.

### 2. Data Exploration
- **Dataset Overview**:
  - Summary statistics and feature descriptions.
  - Data type analysis and distribution insights.
- **Interactive Visualizations**:
  - Histograms, pie charts, scatter plots, and box plots.
  - Outlier detection and correlation heatmaps.

### 3. Risk Prediction
- Input fields for medical attributes (e.g., age, cholesterol, blood pressure).
- Predicts the likelihood of heart disease (High Risk or Low Risk).
- Displays probability scores with clear recommendations.

## How to Run the App

### Prerequisites
Make sure you have Python installed (version >= 3.8). Install the required libraries by running:
```bash
pip install -r requirements.txt
```

### Run the App
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open the app in your browser (default: http://localhost:8501).

## File Structure
- `app.py`: Main application file managing navigation between sections.
- `data_exp.py`: Handles the **Data Exploration** section, including visualizations.
- `risk_predic.py`: Implements the **Risk Prediction** logic and user input handling.
- `heart.csv` & `renamed_heart.csv`: Dataset files for analysis and predictions.
- `requirements.txt`: Lists all dependencies for the project.

## Dataset
The dataset used in this project is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+disease). It includes attributes such as age, sex, cholesterol levels, and chest pain types to evaluate heart health.

## Requirements
Dependencies listed in `requirements.txt`:
```plaintext
pandas>=1.5.0
plotly>=5.0.0
seaborn>=0.12.0
matplotlib>=3.7.0
streamlit>=1.22.0
joblib>=1.3.0
numpy>=1.23.0
Pillow>=9.4.0
scikit-learn>=1.2.0
```
Install these libraries by running:
```bash
pip install -r requirements.txt
```

## Screenshots
- **Home Page**: Welcoming interface with an overview of the app.
  ![Home Page Screenshot](screenshots/home.png)
- **Data Exploration**: Interactive visualizations of the dataset.
  ![Data Exploration Screenshot](screenshots/data_exploration.png)
- **Risk Prediction**: User input form and prediction results.
  ![Risk Prediction Screenshot](screenshots/risk_prediction.png)

## Authors
- Matthieu Richard
