from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOOTSTRAP_SERVERS: str = "localgosr:9092"
    
    LOGGER_NAME: str = "app.log"
    ELASTIC_URL: str = "http://localhost:9200"
    ELASTIC_INDEX_LOG: str = "index_log"

settings = Settings()