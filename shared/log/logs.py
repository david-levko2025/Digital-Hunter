import logging
from elasticsearch import Elasticsearch
from datetime import datetime

from core.config import settings

class Logger:
    _logger = None

    @classmethod
    def get_logger(
        cls, name = settings.LOGGER_NAME,
        es_host = settings.ELASTIC_URL,
        index = settings.ELASTIC_INDEX_LOG,
        level = logging.DEBUG
    ):
        if cls._logger:
            return cls._logger
        
        logger = logging.getLogger(name)
        logger.setLevel(level)