from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
import pandas as pd
import time
df = pd.read_csv("~/kafka_netflix_project/netflix_titles_clean.csv")
for i in df.index:
    row = df.loc[i].to_json()
    #producer.send('netflix_data', str(row))
    producer.send('netflix_data', bytes(row, encoding="UTF-8") )
    print("Sent packet: ", i)
    time.sleep(1)
