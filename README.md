# FetchRewards

**ETL off a SQS Queue**

This repository contains a small application that demonstrates the process of reading JSON data from an AWS SQS Queue, transforming the data, and writing it to a PostgreSQL database. The application is designed to run locally using Dockerized services for Localstack and Postgres

**Overview**

This project focuses on building a data pipeline that processes JSON data from an SQS Queue, applies transformations, masks sensitive information, and stores the data in a PostgreSQL database. The application simulates this process using Docker containers for Localstack and Postgres, making it possible to run the pipeline locally.

**Prerequisites**

Before you begin, ensure that you have the following software installed:
 Docker
 Python
 AWS CLI
 Required Python packages: boto3, psycopg2

**Setting Up the Environment**

Clone this repository to your local machine.
Navigate to the repository directory: cd Project path

**Running the Application**
1. Open the command prompt and navigate to the directory of the project
2. make sure the docker-compose Yaml file exists in the same directory and is correct
3. Start the Docker containers for Localstack and Postgres to start the local environment
   -Use the following cmd in the cmd prompt
       docker-compose up -d
   This will create a local environment with AWS services and a PostgreSQL database
4. Open a different command prompt in the same directory
5. Run the ETL script by executing the following command in the command prompt
   -python AppFetch.py
The script is designed to extract user login data from the SQS Queue, safeguarding sensitive details such as IP addresses and device IDs, before depositing the secured data into the PostgreSQL database.

7. Stop the Docker containers when you're done:
   -docker-compose down
   
**Checking The DataBase**

To check if the Data is loaded as expected in the Data Base:

1. Open a new command prompt and connect it to the Postgres database using the following command
   **docker exec -it <Container Name>psql -U postgres -d postgres**
2. Use the following command to retrieve data from the User_logins Table
   SELECT * FROM user_logins;  

 
