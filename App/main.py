import sys
import pathlib 
import pandas as pd
import streamlit as st

dir = pathlib.Path(__file__).absolute()
sys.path.append(dir.parent.parent)

MODEL_PATH = './models/2023-06-23T13:43:35_LR.pkl'

def prediction(data):
    """
        params:
            data: pd.dataframe  -> input dataset
        
        return:
            df_pred: pd.dataframe  -> predicted result
    """
    
    # Load the model
    model = pd.read_pickle(MODEL_PATH)
    # predict the data
    pred = model.predict(data)

    print(data)

    df_pred = pd.DataFrame(pred).rename({0: "Attrition"}, axis=1)

    dict = {
        "Yes": "Leave",
        "No": "Stay"
    }

    df_pred["Attrition"].replace(dict, inplace=True)

    # return the predicted
    return df_pred

def header():
    st.title("Employee Attrition Prediction")

if __name__ == "__main__":
    header()
    
    form = st.form(key='my_form')

    AGE = form.number_input("Age", min_value=18, max_value=100, value=18)
    BUSINESS_TRAVEL = form.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
    DAILY_RATE = form.number_input("Daily Rate", min_value=0, max_value=100000, value=0)
    DEPARTMENT = form.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
    DISTANCE_FROM_HOME = form.number_input("Distance From Home", min_value=0, max_value=100, value=0)
    EDUCATION = form.number_input("Education", min_value=1, max_value=5, value=1)
    EDUCATION_FIELD = form.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])
    ENVIRONMENT_SATISFACTION = form.number_input("Environment Satisfaction", min_value=1, max_value=4, value=1)
    GENDER = form.selectbox("Gender", ["Female", "Male"])
    HOURLY_RATE = form.number_input("Hourly Rate", min_value=0, max_value=100, value=0)
    JOB_INVOLVEMENT = form.number_input("Job Involvement", min_value=1, max_value=4, value=1)
    JOB_LEVEL = form.number_input("Job Level", min_value=1, max_value=5, value=1)
    JOB_ROLE = form.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
    JOB_SATISFACTION = form.number_input("Job Satisfaction", min_value=1, max_value=4, value=1)
    MARITAL_STATUS = form.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    MONTHLY_INCOME = form.number_input("Monthly Income", min_value=0, max_value=100000, value=0)
    MONTHLY_RATE = form.number_input("Monthly Rate", min_value=0, max_value=100000, value=0)
    NUM_COMPANIES_WORKED = form.number_input("Number of Companies Worked", min_value=0, max_value=10, value=0)
    OVER_TIME = form.selectbox("Over Time", ["Yes", "No"])
    PERCENT_SALARY_HIKE = form.number_input("Percent Salary Hike", min_value=0, max_value=100, value=0)
    PERFORMANCE_RATING = form.number_input("Performance Rating", min_value=1, max_value=4, value=1)
    RELATIONSHIP_SATISFACTION = form.number_input("Relationship Satisfaction", min_value=1, max_value=4, value=1)
    STOCK_OPTION_LEVEL = form.number_input("Stock Option Level", min_value=0, max_value=3, value=0)
    TOTAL_WORKING_YEARS = form.number_input("Total Working Years", min_value=0, max_value=40, value=0)
    TRAINING_TIMES_LAST_YEAR = form.number_input("Training Times Last Year", min_value=0, max_value=10, value=0)
    WORK_LIFE_BALANCE = form.number_input("Work Life Balance", min_value=1, max_value=4, value=1)
    YEARS_AT_COMPANY = form.number_input("Years At Company", min_value=0, max_value=40, value=0)
    YEARS_IN_CURRENT_ROLE = form.number_input("Years In Current Role", min_value=0, max_value=40, value=0)
    YEARS_SINCE_LAST_PROMOTION = form.number_input("Years Since Last Promotion", min_value=0, max_value=40, value=0)
    YEARS_WITH_CURR_MANAGER = form.number_input("Years With Current Manager", min_value=0, max_value=40, value=0)

    form.form_submit_button('Add')

    # predict the data
    data = {
        "Age": AGE,
        "BusinessTravel": BUSINESS_TRAVEL,
        "DailyRate": DAILY_RATE,
        "Department": DEPARTMENT,
        "DistanceFromHome": DISTANCE_FROM_HOME,
        "Education": EDUCATION,
        "EducationField": EDUCATION_FIELD,
        "EnvironmentSatisfaction": ENVIRONMENT_SATISFACTION,
        "Gender": GENDER,
        "HourlyRate": HOURLY_RATE,
        "JobInvolvement": JOB_INVOLVEMENT,
        "JobLevel": JOB_LEVEL,
        "JobRole": JOB_ROLE,
        "JobSatisfaction": JOB_SATISFACTION,
        "MaritalStatus": MARITAL_STATUS,
        "MonthlyIncome": MONTHLY_INCOME,
        "MonthlyRate": MONTHLY_RATE,
        "NumCompaniesWorked": NUM_COMPANIES_WORKED,
        "OverTime": OVER_TIME,
        "PercentSalaryHike": PERCENT_SALARY_HIKE,
        "PerformanceRating": PERFORMANCE_RATING,
        "RelationshipSatisfaction": RELATIONSHIP_SATISFACTION,
        "StockOptionLevel": STOCK_OPTION_LEVEL,
        "TotalWorkingYears": TOTAL_WORKING_YEARS,
        "TrainingTimesLastYear": TRAINING_TIMES_LAST_YEAR,
        "WorkLifeBalance": WORK_LIFE_BALANCE,
        "YearsAtCompany": YEARS_AT_COMPANY,
        "YearsInCurrentRole": YEARS_IN_CURRENT_ROLE,
        "YearsSinceLastPromotion": YEARS_SINCE_LAST_PROMOTION,
        "YearsWithCurrManager": YEARS_WITH_CURR_MANAGER
    }

    df = pd.DataFrame(data, index=[0])

    if st.button('Predict'):
        pred = prediction(df)
        st.write(pred)




