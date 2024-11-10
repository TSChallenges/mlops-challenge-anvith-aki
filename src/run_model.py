import os
import pickle
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

def load_model():
    
    # model_path = '/models/churn_model.pkl' 
    model_path = '/workspaces/mlops-challenge-anvith-aki/models/churn_model.pkl' 
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def get_customer_input():
    credit_score = float(input("Enter credit score: "))
    age = int(input("Enter age: "))
    balance = float(input("Enter balance: "))
    num_of_products = int(input("num_of_products: "))
    input5 = int(input("input: "))
    input6 = int(input("input: "))
    input7 = int(input("input: "))
    input8 = int(input("input: "))
    return [[credit_score, age, balance, num_of_products, input5, input6, input7, input8]]

def predict_churn(model, customer_data):
    prediction = model.predict(customer_data)
    return prediction[0]

if __name__ == "__main__":
    model = load_model()
    customer_data = get_customer_input()
    result = predict_churn(model, customer_data)
    print("Churn Prediction:", "Will Churn" if result == 1 else "Will Not Churn")
