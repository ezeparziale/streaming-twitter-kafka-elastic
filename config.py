from pydantic import BaseSettings


class Settings(BaseSettings):

    # TWITTER API KEYS
    TWITTER_API_KEY: str
    TWITTER_API_SECRET_KEY: str
    TWITTER_ACCESS_TOKEN: str
    TWITTER_ACCESS_TOKEN_SECRET: str

    # KAFKA
    SERVER_KAFKA: str = "localhost:9092"
    TOPIC_NAME: str = "twitter"

    # ELASTIC
    ELASTIC_SERVER: str = "localhost:9200"
    ELASTICSEARCH_USERNAME: str
    ELASTICSEARCH_PASSWORD: str

    # CONFIG TWEETS
    TRACKS: list = [
        "#argentina",
        "argentina",
        "seleccion",
        "messi",
        "escaloneta",
        "afa",
    ]
    LOCATION: list = [-126.2, -56.0, 22.3, 58.9]
    LANGUAGES: list = ["en", "es"]

    class Config:
        env_file = [".env"]


settings = Settings()
