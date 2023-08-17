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
Start the Docker containers for Localstack and Postgres:
