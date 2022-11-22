# 🐦 Streaming tweets with kafka and elastic

Demo of streaming tweets from twitter and save it in elastic search.

- [X] Elastic search
- [X] Kibana
- [X] Kafka topic
- [X] Kafka producer
- [X] Kafka consumer

## :floppy_disk: Installation

```bash
python -m venv env
```

```bash
. env/scripts/activate
```

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## :wrench: Config

Create `.env` file. Check the example `.env.example`

Create your twitter app to get credentils:

```http
https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
```

## 🏃‍♂️ Run

1. Run docker compose to initialize the kakfa server, mongo db and mongo express.

```console
docker-compose -f "docker-compose.yaml" up -d
```

2. Config your search paramaters in `config.py`:

```python
TRACKS = ["#argentina", "argentina", "boca", "river","ronaldo", "messi", "psg", "barcelona", "manchester"]
LOCATION = [-126.2,-56.0,22.3,58.9]
LANGUAGES = ["en", "es"]
```

3. Run **new_topic.py** for create the kafka topic.

4. Run **producer.py** for read tweets and publish in kakfa topic.

5. Run **consumer_elastic.py** for read the topic in kafka and write the tweets in elastic.

6. View the tweets in **kibana**

```http
http://localhost:5601
```
