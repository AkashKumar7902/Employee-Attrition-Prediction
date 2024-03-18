# Employee-Attrition-Prediction
The project provides accurate predictions of employee attrition within an organization by analyzing multiple employee-related features.

## Datasets
The data set has been made available by IBM.
https://zenodo.org/record/4088439#.Y9Y3rtJBwUE
    
## Getting Started
### Installation
```
git clone https://github.com/akashkumar7902/Employee-Attrition-Prediction
cd Employee-Attrition-Prediction 
pip install -r requirements.txt
```

### Running locally 
To run the web locally
```
streamlit run App/main.py
``` 
visit localhost:8501 to access the web app

### Running using Docker 
1. build the image
```
docker build -t employee-attrition .
```
2. run the container
```
docker run -p 8501:8501 employee-attrition
```