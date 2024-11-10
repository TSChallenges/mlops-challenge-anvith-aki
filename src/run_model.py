import os
import pickle
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

def load_model():
    
    model_path = '/models/churn_model.pkl' 
    # model_path = '/workspaces/mlops-challenge-anvith-aki/models/churn_model.pkl' 
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def get_customer_input():
    credit_score = float(sys.argv[1])
    input2 = int(sys.argv[2])
    input3 = float(sys.argv[3])
    input4 = int(sys.argv[4])
    input5 = int(sys.argv[5])
    input6 = int(sys.argv[6])
    input7 = int(sys.argv[7])
    input8 = int(sys.argv[8])
    return [[credit_score, input2, input3, input4, input5, input6, input7, input8]]

def predict_churn(model, customer_data):
    prediction = model.predict(customer_data)
    return prediction[0]

if __name__ == "__main__":
    model = load_model()
    customer_data = get_customer_input()
    result = predict_churn(model, customer_data)
    print("Churn Prediction:", "Will Churn" if result == 1 else "Will Not Churn")
