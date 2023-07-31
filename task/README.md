# Task -- Building an ETL Pipeline with Apache Airflow

## Objective
The main objective of this assignment is to provide you with hands-on experience in designing and implementing an Extract, Transform, Load (ETL) pipeline using Apache Airflow. Through this assignment, you will learn how to extract data from a publicly available API, perform data transformations, and load the cleaned data into a PostgreSQL database.

## Dataset Source
For this assignment, we will be utilizing the "Random User Generator" API, which generates random user data. You can access the API endpoint at [https://randomuser.me/api/](https://randomuser.me/api/).

## Requirements
1. **Extract Data from the API**: Your task is to use the provided API endpoint to fetch a batch of random user records (e.g., 100 records). The API response will be in JSON format.

2. **Transform the Data**: Once you've obtained the JSON response, you will need to parse it and extract relevant information from the user records. Create a cleaned and structured dataset with the following columns:
   - First Name
   - Last Name
   - Gender
   - Email
   - Date of Birth (in YYYY-MM-DD format)
   - Country
   - Street Address
   - City
   - State
   - Postcode
   - Phone
   - Cell

3. **Load the Data into PostgreSQL**: After transforming the data, you will create a new table in a PostgreSQL database to store the cleaned user data. Your task is to load the transformed data from the previous step into this table.

4. **Airflow DAG**: To orchestrate the entire ETL process, you will design an Apache Airflow Directed Acyclic Graph (DAG). The DAG should include the following tasks:
   a. Extract data from the API
   b. Transform the data
   c. Load the data into PostgreSQL

5. **Scheduling**: You are required to schedule the DAG to run daily at a specific time.


## Document Your Process
Provide clear and concise documentation, explaining the steps you took to complete the assignment. Your documentation should include relevant code explanations, dependencies, and setup instructions.

## Submission
Students should submit their completed assignments through a version control system like GitHub. The submission should include the following:
- The Airflow DAG Python script
- Any relevant Python utility functions or modules used
- Documentation with clear explanations and setup instructions


Happy learning and have fun building your ETL pipeline with Airflow! 🚀