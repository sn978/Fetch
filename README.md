# FetchRewards

**#ETL off a SQS Queue**

#Overview
The described procedure involves an uncomplicated ETL (Extract, Transform, Load) operation. It begins by extracting user login details from an AWS SQS (Simple Queue Service) Queue, then proceeds to obfuscate any sensitive information, ultimately depositing the modified data into a PostgreSQL database. This entire process is executed on a local environment utilizing Docker and LocalStack to replicate the functionalities of AWS services

