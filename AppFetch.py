{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "55fcbe15",
   "metadata": {},
   "outputs": [],
   "source": [
    "import boto3\n",
    "import json\n",
    "import hashlib\n",
    "import psycopg2\n",
    "from hashlib import md5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6a6b30df",
   "metadata": {},
   "outputs": [],
   "source": [
    "# AWS SQS configuration\n",
    "queue_url = 'http://localhost:4566/000000000000/login-queue'\n",
    "sqs = boto3.client('sqs', region_name='us-east-2', endpoint_url=queue_url,\n",
    "                   aws_access_key_id='dummy', aws_secret_access_key='dummy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "94ae1700",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Postgres configuration\n",
    "conn = psycopg2.connect(\n",
    "    dbname='postgres',\n",
    "    user='postgres', \n",
    "    password='postgres',\n",
    "    host='localhost', \n",
    "    port='5432'\n",
    ")\n",
    "cur = conn.cursor()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "68485d3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n",
      "{'MessageId': '766c2050-6266-40b8-ac65-671194a05e2d', 'ReceiptHandle': 'YmMzMjE4N2UtZDkxZS00NzhkLWEzZWYtMTRjNTVhZjdhZjk2IGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6bG9naW4tcXVldWUgNzY2YzIwNTAtNjI2Ni00MGI4LWFjNjUtNjcxMTk0YTA1ZTJkIDE2OTIzMTg4MTguMzkzMTM0', 'MD5OfBody': 'e4f1de8c099c0acd7cb05ba9e790ac02', 'Body': '{\"user_id\": \"424cdd21-063a-43a7-b91b-7ca1a833afae\", \"app_version\": \"2.3.0\", \"device_type\": \"android\", \"ip\": \"199.172.111.135\", \"locale\": \"RU\", \"device_id\": \"593-47-5928\"}'}\n",
      "1237b6b78f6293ce2714d52b209eb3b4\n",
      "a56e7589b4b780605f7c614d13df6696\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    # Receive messages from the SQS queue\n",
    "    response = sqs.receive_message(\n",
    "        QueueUrl=queue_url,\n",
    "        MaxNumberOfMessages=10,\n",
    "        VisibilityTimeout=0,\n",
    "        WaitTimeSeconds=0\n",
    "    )    \n",
    "\n",
    "    if 'Messages' in response:\n",
    "        for message in response['Messages']:\n",
    "            message = response['Messages'][0]\n",
    "            body = json.loads(message['Body'])\n",
    "            print(message)\n",
    "\n",
    "            # Hash the device_id and ip for masking and duplicate identification\n",
    "            device_id = body.get('device_id', '19991')\n",
    "            ip = body.get('ip', '0.0.0.0')\n",
    "            masked_device_id = hashlib.md5(device_id.encode()).hexdigest()\n",
    "            masked_ip = hashlib.md5(ip.encode()).hexdigest()\n",
    "            print(masked_device_id)\n",
    "            print(masked_ip)\n",
    "\n",
    "            # Insert the masked data into user_logins table\n",
    "            with conn:\n",
    "                with conn.cursor() as cur:\n",
    "                    insert_query = \"\"\"\n",
    "                        INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)\n",
    "                        VALUES (%s, %s, %s, %s, %s, %s, NOW())\n",
    "                    \"\"\"\n",
    "                    cur.execute(insert_query, (\n",
    "                        body['user_id'],\n",
    "                        body['device_type'],\n",
    "                        masked_ip,\n",
    "                        masked_device_id,\n",
    "                        body['locale'],\n",
    "                        int(body['app_version'].replace('.', '')) if body['app_version'] else None\n",
    "                    ))\n",
    "                    conn.commit()\n",
    "\n",
    "            # Delete the message from the queue after processing\n",
    "            sqs.delete_message(\n",
    "                QueueUrl=queue_url,\n",
    "                ReceiptHandle=message['ReceiptHandle']\n",
    "            )\n",
    "\n",
    "    else:\n",
    "        print('No messages in the queue')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "091db198",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "25ab2539",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
