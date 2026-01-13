from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass(frozen=True)
class Settings:
    mysql_host: str
    mysql_port: int
    mysql_database: str
    mysql_user: str
    mysql_password: str

    @property
    def database_url(self) -> str:
        # This is the “dynamic string” part (clean and centralized)
        return (
            f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}"
        )

def get_settings() -> Settings:
    load_dotenv()  # reads .env into environment variables
    return Settings(
        mysql_host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        mysql_port=int(os.getenv("MYSQL_PORT", "3306")),
        mysql_database=os.getenv("MYSQL_DATABASE", "appdb"),
        mysql_user=os.getenv("MYSQL_USER", "appuser"),
        mysql_password=os.getenv("MYSQL_PASSWORD", "apppass"),
    )