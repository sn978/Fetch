#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import json
import psycopg2
from hashlib import md5


# In[2]:


# AWS SQS configuration
queue_url = 'http://localhost:4566/000000000000/login-queue'
sqs = boto3.client('sqs', region_name='us-east-2', endpoint_url=queue_url,
                   aws_access_key_id='dummy', aws_secret_access_key='dummy')


# In[3]:


# Postgres configuration
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres', 
    password='postgres',
    host='localhost', 
    port='5432'
)
cur = conn.cursor()


# In[4]:


def mask_field(value):
    # Replace this with your masking logic
    return "MASKED"


# In[5]:


def main():
    # Receive messages from the SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        body = json.loads(message['Body'])
        
        # Mask sensitive fields
        masked_ip = mask_field(body.get('ip', '0.0.0.0'))
        masked_device_id = mask_field(body.get('device_id', '19991'))

        # Connect to the database
        with conn:
            with conn.cursor() as cur:
                # Insert the masked data into user_logins table
                insert_query = """
                    INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW())
                """
                cur.execute(insert_query, (
                    body['user_id'],
                    body['device_type'],
                    masked_ip,
                    masked_device_id,
                    body['locale'],
                    int(body['app_version'].replace('.', '')) if body['app_version'] else None
                ))
                conn.commit()

        # Delete the message from the queue after processing
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )

    else:
        print('No messages in the queue')


# In[6]:


if __name__ == '__main__':
    main()


# In[ ]:




