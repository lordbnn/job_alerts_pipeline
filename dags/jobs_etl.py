from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
import requests
import pandas as pd
from sqlalchemy import create_engine



    
#create a function to extract skills from an input
def extract_skills(c):
    ##lIST OF SKILLS
    words = ['ETL','Orchestration', 'modeling', 'python', 
         'sql','pandas','docker','aws','gcp','google cloud',
         'postgres','mongodb','spark','jira','databricks',
         'azure','dbt','amazon','s3','linux','hadoop','kubernetes',
         'hbase','hive','fivetran','mage','airflow','ci/cd','elt']

    acronyms = ['sql','dbt','elt','etl','aws','gcp'] #Acronyms from skills list that would need to be made uppercase

    skills = []
    for i in words:
        if i.lower() in c.lower():
            if i.lower() in acronyms:
                skills.append(i.upper())
            else: skills.append(i.title())
    return skills





def get_data_from_api():
    #VARIABLES DECLARATION
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query":"Data Engineer in Ontario, Canada","page":"1","num_pages":"1","date_posted":"month"}

    headers = {
	"X-RapidAPI-Key": [YOUR_API_KEY],
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data



def extract_relevant_records_from_overall_data(data):
    
    employer_website = []
    job_id = []
    job_employment_type = []
    job_title = []
    job_apply_link=[]
    job_description=[]
    job_city=[]
    job_country =[]
    job_posted_at_date =[]
    employer_company_type =[]

    for i in range(len(data['data'])):
        employer_website.append(data['data'][i]['employer_website'])
        job_id.append(data['data'][i]['job_id'])
        job_employment_type.append(data['data'][i]['job_employment_type'])
        job_title.append(data['data'][i]['job_title'])
        job_apply_link.append(data['data'][i]['job_apply_link'])
        job_description.append(data['data'][i]['job_description'])
        job_city.append(data['data'][i]['job_city'])
        job_country.append(data['data'][i]['job_country'])
        job_posted_at_date.append(data['data'][i]['job_posted_at_datetime_utc'][:10])
        employer_company_type.append(data['data'][i]['employer_company_type'])
    return employer_website,job_id,job_employment_type,job_title,job_apply_link,job_description,job_city,job_country,job_posted_at_date,employer_company_type





def translate_extractions_to_dataframe_and_transform(employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type):
    
    
    #placing values into columns
    rapid_dict = {
                    'job_id': job_id,
                    'employer_website':employer_website,
                    'job_employment_type':job_employment_type,
                    'job_title':job_title,
                    'job_apply_link':job_apply_link,
                    'job_description':job_description,
                    'job_city':job_city,
                    'job_country':job_country,
                    'job_posted_at_date':job_posted_at_date,
                    'employer_company_type':employer_company_type        

                 }
    
    job_df = pd.DataFrame(rapid_dict)#convert to dataframe
    
    #convert date column datatype from string to datetime
    job_df['job_posted_at_date'] = pd.to_datetime(job_df['job_posted_at_date'])
    
    #Add a new column in the dataframe and extract skills from the job_description column
    #using the job_description column as an input in the extract_skills function
    job_df['skillset'] = job_df['job_description'].apply(lambda x: extract_skills(x))
    
    #CHANGE THE POSITION OF THE SKILLSET COLUMN FROM LAST TO AFTER THE JOB DESCRIPTION COLUMN
    
    #remove the skillset column and save it in a variable
    skillset_col = job_df.pop('skillset')
    
    # insert column using insert(position,column_name,skillset_col) function
    job_df.insert(6, 'skillset', skillset_col)
  
    return job_df




def to_sql_task(df,table_name):
    engine = create_engine('postgresql://airflow:airflow@host.docker.internal:5436/postgres')
    df.to_sql(table_name, engine)
       


data = get_data_from_api()
employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type = extract_relevant_records_from_overall_data(data)
df_rapid = translate_extractions_to_dataframe_and_transform(employer_website, job_id, job_employment_type, job_title, job_apply_link, job_description, job_city, job_country, job_posted_at_date, employer_company_type)


default_args={
    'owner':'byron',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
    
}
with DAG(
    dag_id='rapid_api_v1',
    description='DE job vacancies in ontario, Canada: an ETL pipeline',
    start_date=datetime(2023,7,31),
    schedule_interval='@daily',
    default_args = default_args    
    )as dag:
    
    get_data_fromapi = PythonOperator(
        task_id = 'get_data_from_api',
        python_callable = get_data_from_api
        
    )
    
    
    extract_relevant_records = PythonOperator(
        task_id = 'extract_relevant_records',
        python_callable = extract_relevant_records_from_overall_data,
        provide_context = True,
        op_args=[data]
        
    )    

load_db=PythonOperator(
    task_id='load_db',
    python_callable=to_sql_task,
    op_args=[df_rapid,'new_rapid_api_jobs']
    
)
    
    # Define the task dependencies

get_data_fromapi >> extract_relevant_records  >> load_db