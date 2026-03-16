from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # kafka settings
    BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_GROUP_INTEL: str = "group-intel"
    KAFKA_GROUP_ATTACK: str = "group-attack"
    KAFKA_GROUP_DAMAGE: str = "group-damage"
    KAFKA_TOPIC_INTEL : str = "intel"
    KAFKA_TOPIC_ATTACK : str = "attack"
    KAFKA_TOPIC_DAMAGE : str = "damage"
    KAFKA_TOPIC_DLQ : str = "intel_signals_dlq"

    # logger settings 
    LOGGER_NAME: str = "app.log"
    ELASTIC_URL: str = "http://localhost:9200"
    ELASTIC_INDEX_LOG: str = "index_log"

    # sql settings
    NYSQL_HOST: str = "localhost"
    NYSQL_PORT: int = 3306
    NYSQL_USER: str = "root"
    NYSQL_PASSWORD: str = ""
    NYSQL_DB: str = "system_db"

settings = Settings()