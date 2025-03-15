from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DB_USER: str 
    DB_HOST: str 
    DB_PASSWORD: str 
    DB_PORT: str 
    DB_NAME: str 


    
    @property
    def connection_string(self):
        return (
            f'postgresql+asyncpg://'
            f'{self.DB_USER}:'
            f'{self.DB_PASSWORD}@'
            f'{self.DB_HOST}:{self.DB_PORT}/'
            f'{self.DB_NAME}'
        )


    class Config:
        env_file = ".env"

settings = Settings()