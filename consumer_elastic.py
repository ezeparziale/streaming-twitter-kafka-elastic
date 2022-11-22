from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
from config import settings

def main():             
    consumer = KafkaConsumer(settings.TOPIC_NAME)
    try:
        es = Elasticsearch(hosts=f"http://{settings.ELASTICSEARCH_USERNAME}:{settings.ELASTICSEARCH_PASSWORD}@{settings.ELASTIC_SERVER}/")        
        for msg in consumer:
            output = []
            output.append(json.loads(msg.value))
            print(json.loads(msg.value))
            tweet = json.loads(msg.value)
            # Inserta tweet a elastic
            es.index(
                    index="tweets",
                    document={
                        "author": tweet["user"]["screen_name"],
                        "fecha": tweet["created_at"],
                        "mensaje": tweet["text"]
                        }
                    )
            print ('\n')
    except Exception as e:        
        print("Error >>> ", e)

if __name__ == "__main__":
    main()