from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # kafka settings
    BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_GROUP_ID: str = ""
    KAFKA_TOPIC_INTEL : str = "intel"
    KAFKA_TOPIC_ATTACK : str = "attack"
    KAFKA_TOPIC_DAMAGE : str = "damage"

    # logger settings 
    LOGGER_NAME: str = "app.log"
    ELASTIC_URL: str = "http://localhost:9200"
    ELASTIC_INDEX_LOG: str = "index_log"

settings = Settings()