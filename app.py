from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import BayesianRidge
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

app = Flask('income_predictor')

df = pd.read_csv('Salary_Data.csv')

selected_columns = ['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience', 'Salary']
df = df[selected_columns]

categorical_cols = ['Gender', 'Education Level', 'Job Title']
numeric_cols = ['Age', 'Years of Experience']

X = df.drop('Salary', axis=1)
y = df['Salary']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Impute missing values in the target variable
y_imputer = SimpleImputer(strategy='mean')
y = y_imputer.fit_transform(y.values.reshape(-1, 1)).flatten()

# Define the model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', BayesianRidge())
])

# Fit the model
model.fit(X, y)

@app.route('/')
def index():
    job_titles = df['Job Title'].unique().tolist()
    education_levels = df['Education Level'].unique().tolist()

    return render_template('index.html', job_titles=job_titles, education_levels=education_levels)


@app.route('/predict', methods=['POST'])
def predict():
    user_data = request.form.to_dict()
    user_df = pd.DataFrame([user_data], columns=['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience'])
    user_df = pd.DataFrame(user_df.values, columns=user_df.columns)
    user_df_transformed = preprocessor.transform(user_df)
    predicted_income, prediction_std_dev = model.named_steps['regressor'].predict(user_df_transformed, return_std=True)
    feature_importances = model.named_steps['regressor'].coef_

    response_data = {
        'predictedIncome': float(predicted_income[0]),
        'predictionStdDev': float(prediction_std_dev[0]),
        'featureImportances': {feature: float(importance) for feature, importance in zip(X.columns, feature_importances)}
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
