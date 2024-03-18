FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
ENV NAME EmployeeAttrition

ENTRYPOINT ["streamlit", "run"]
CMD ["./App/main.py"]