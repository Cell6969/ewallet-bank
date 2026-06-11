from pydantic_settings import BaseSettings,SettingsConfigDict

_base_config = SettingsConfigDict(
    env_file='./.env', env_ignore_empty=True, extra="ignore"
)

class AppSettings(BaseSettings):
    APP_NAME:str
    APP_DOMAIN:str
    APP_ENV:str
    APP_KEY:str

    model_config = _base_config

class DatabaseSettings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_NAME:str
    DB_USER:str
    DB_PASSWORD:str

    model_config = _base_config

    @property
    def get_db_connection(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

# Initialize 
app_settings = AppSettings()
db_settings = DatabaseSettings()