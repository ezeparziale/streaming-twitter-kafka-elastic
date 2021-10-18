import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'kibana.env')
load_dotenv(dotenv_path)

dotenv_path = join(dirname(__file__), 'twitter_api.env')
load_dotenv(dotenv_path)

# API KEYS DE TWIITER
API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET_KEY = os.environ.get("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# KAFKA
SERVER_KAFKA = 'localhost:9092'
TOPIC_NAME = 'twitter' # NOMBRE DEL TOPIC DE KAFKA

# ELASTIC
ELASTIC_SERVER = 'localhost:9200'
ELASTIC_USER = os.environ.get("ELASTICSEARCH_USERNAME")
ELASTIC_PASS = os.environ.get("ELASTICSEARCH_PASSWORD")

# CONFIGURACION PARA BUSQUEDA DE TUITS
TRACKS = ['#argentina','argentina','seleccion','messi','escaloneta','afa']
LOCATION = [-126.2,-56.0,22.3,58.9]
LANGUAGES = ['en','es']