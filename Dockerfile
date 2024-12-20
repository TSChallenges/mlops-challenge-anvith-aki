# This is from Question 
# CANDIDATES ENTER YOUR CODE HERE
FROM python:3.8-slim

WORKDIR /app

COPY models /models
COPY src /src
COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

CMD ["python", "/src/run_model.py"]