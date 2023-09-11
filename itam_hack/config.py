from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    postgres_url: str
    secret_key: str
    hash_algorithm: str = 'HS256'


settings = Settings()
