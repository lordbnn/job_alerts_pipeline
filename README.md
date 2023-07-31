# Data Engineering Job Vacancies ETL Pipeline

![Data Engineering](https://img.shields.io/badge/Data%20Engineering-Job%20Vacancies-blue)

This project implements a robust Extract, Transform, and Load (ETL) pipeline that extracts, processes, and stores data engineering job vacancies in Ontario, Canada. The pipeline is designed to keep hiring managers, recruiters, and data enthusiasts informed about the latest job opportunities in the data engineering domain.

## Project Overview

The Data Engineering Job Vacancies ETL Pipeline aims to automate the process of gathering relevant job vacancy data from a RapidAPI service, performing data transformations, and storing the processed data in a PostgreSQL database. The structured data is enriched with extracted skills from the job descriptions, providing valuable insights into the sought-after skills in the job market.

## How it Works

1. **Data Extraction**: The pipeline queries a reputable RapidAPI endpoint to fetch up-to-date job vacancies for data engineering positions in Ontario, Canada. The data is fetched daily to ensure real-time information.

2. **Data Transformation**: The extracted data is meticulously processed and transformed into a structured DataFrame. As a unique feature, this pipeline identifies essential skills from the job descriptions using predefined lists and categorizes them accordingly.

3. **Data Loading**: The structured and enriched data is securely loaded into a dedicated PostgreSQL database table named "new_rapid_api_jobs." The PostgreSQL database acts as a centralized repository for easy access and analysis.

## Key Features

- **Dynamic Scheduling**: The pipeline is orchestrated to run daily, ensuring the database is always up-to-date with the latest job vacancies.

- **Error Resilience**: To ensure a seamless data extraction process, the pipeline is configured with robust error handling mechanisms. Failed tasks are automatically retried up to five times with a short delay between retries.

- **Enriched Data Insights**: The pipeline goes beyond standard data extraction by identifying key skills in the job market. This information empowers hiring managers to make data-driven decisions while hiring talent.

- **Fully Configurable**: The pipeline allows for easy customization, enabling users to adapt it to different job search queries, locations, and API parameters.

## Requirements

- Python 3.x
- Airflow
- Requests
- Pandas
- SQLAlchemy
- PostgreSQL

## Usage

1. Start up Airflow as configured in the docker-compose file using `docker-compose up -d`.

2. Set up a PostgreSQL database with credentials and ensure the connection URL is correctly provided in the script.

3. Create a RapidAPI account and obtain an API key for accessing the job vacancy data.

4. Customize the `querystring` in the `get_data_from_api` function to match your desired job search criteria.

5. Run the pipeline with Airflow using the provided DAG, ensuring that the required connections and variables are properly configured.

## Contribution and Feedback

Contributions are welcomed to enhance and extend this ETL pipeline further. Feel free to submit pull requests, raise issues, or provide feedback to help us improve the project.


![Data Engineering](https://img.shields.io/badge/Data%20Engineering-Job%20Vacancies-blue)

---

Byron's Note: Make sure to replace [YOUR API KEY] in the `get_data_from_api` function with your actual RapidAPI key. Additionally, fill in the Requirements section with the necessary versions of the required libraries and software. Feel free to add your GitHub profile link, and if you have any additional credentials or accolades, you can include them as well. Make sure the code is well-documented and adheres to best practices for readability and maintainability.

