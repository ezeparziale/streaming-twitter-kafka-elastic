from pydantic import BaseSettings
class Settings(BaseSettings):

    # API KEYS DE TWIITER
    TWITTER_API_KEY: str
    TWITTER_API_SECRET_KEY: str
    TWITTER_ACCESS_TOKEN: str
    TWITTER_ACCESS_TOKEN_SECRET: str

    # KAFKA
    SERVER_KAFKA: str = "localhost:9092"
    TOPIC_NAME: str = "twitter"  # NOMBRE DEL TOPIC DE KAFKA

    # ELASTIC
    ELASTIC_SERVER: str = 'localhost:9200'
    ELASTICSEARCH_USERNAME: str
    ELASTICSEARCH_PASSWORD: str

    # CONFIGURACION PARA BUSQUEDA DE TUITS
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
