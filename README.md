Income Predictor

This project is an Income Predictor web application that predicts the salaries of employees at a company based on various input features. The prediction model is trained on a simulated dataset containing information about each employee, including age, gender, education level, job title, years of experience, and salary ranges.

Dataset
The dataset used for training the model is artificially generated for educational purposes. It includes the following columns:
1. Age: Age of each employee in years (numeric).
2. Gender: Gender of each employee (categorical: Male, Female, Other).
3. Education Level: Educational level of each employee (categorical: High School, Bachelor's, Master's, PhD).
4. Job Title: Job title of each employee (categorical).
5. Years of Experience: Number of years of work experience of each employee (numeric).
6. Salary: Annual salary of each employee in US dollars (numeric).
The dataset also includes labeled salary ranges for analysis using the standard deviation.


Prerequisites
Before running the project, ensure you have the following prerequisites installed:
Python (backend)

Getting Started

  Clone the repository:
  
    git clone https://github.com/abbyaguilar/income-predictor.git
    
    cd income-predictor
    
  Install dependencies:
  
    pip install -r requirements.txt

  Download Kaggle Dataset:

    kaggle datasets download -d rkiattisak/salaly-prediction-for-beginer
    
  Run the Python backend:
  
    python app.py
    
The backend should be running at http://127.0.0.1:5000.
Open index.html in your web browser or deploy it to a web server.

Usage

Open the web application in your browser.
Fill in the form with your details (age, gender, education level, job title, and years of experience).
Click the "Predict Income" button.
View the predicted income, uncertainty (standard deviation), and the impact of each feature on the predicted income.

Features

Predict Income: Input your details and get an estimate of your predicted income.
Feature Impact: Understand how each input feature impacts your predicted income, positively or negatively.

Dataset Disclaimer

This dataset is artificially generated for educational purposes, and any commercial use is strictly prohibited. The data used in this project was created by large language models and not collected from actual data sources.

Feel free to customize and extend the application based on your needs. If you have specific questions or need help related to the dataset, feel free to ask!
