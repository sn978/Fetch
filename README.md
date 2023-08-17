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
   -> Use the following cmd in the cmd prompt
       docker-compose up -d
   This will create a local environment with AWS services and a PostgreSQL database
4. Open a different command prompt in the same directory
5. Run the ETL script by executing the following command in the command prompt
   ->   python FetchRewards.py
The script is designed to extract user login data from the SQS Queue, safeguarding sensitive details such as IP addresses and device IDs, before depositing the secured data into the PostgreSQL database.

6. Stop the Docker containers when you're done:
 ->docker-compose down

**Assumptions**
The provided JSON data has a specific structure as defined in the SQS message format.
The masking of sensitive information is done using MD5 hashing.

**Next Steps**

The project could be further enhanced with:
->Comprehensive error handling and logging mechanisms.
->Unit tests to ensure the correctness of the processing pipeline.
->Better separation of concerns through modularization and clean architecture.
->Containerization of the application for easier deployment.
->CI/CD integration to automate testing and deployment processes.

**Deployment in Production**
consider the following steps:
->Use actual AWS SQS and RDS services instead of Localstack and Dockerized Postgres.
->Implement security measures, including access controls, encryption, and secure credentials management.
->Set up monitoring and alerting to track pipeline performance and errors.
->Use a container orchestration tool (e.g., Kubernetes) to manage the application's deployment and scaling.

**Scaling with Growing Dataset**

->To handle a growing dataset:
->Optimize the database schema with proper indexing and partitioning strategies.
->Consider using distributed message queues (e.g., Amazon SQS) and database sharding for scalability.
->Implement data parallelization and batching for more efficient processing.

**PII Recovery**
PII recovery could be achieved using secure key management and encryption techniques. Decrypting masked data would require proper authorization and authentication mechanisms.
   

 
