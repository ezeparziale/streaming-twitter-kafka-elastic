from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import config

def main():             
    consumer = KafkaConsumer(config.TOPIC_NAME)
    try:
        es = Elasticsearch(hosts="http://elastic:somethingsecret@localhost:9200/")        
        for msg in consumer:
            output = []
            output.append(json.loads(msg.value))
            print(json.loads(msg.value))
            tweet = json.loads(msg.value)
            # Inserta tweet a elastic
            es.index(
                    index="tweets",
                    doc_type="test-type",
                    body={
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