from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

_ENV_FILE = Path(__file__).resolve().parent.parent.parent / ".env"

load_dotenv(_ENV_FILE)

_BASE_CONFIG = SettingsConfigDict(
    env_file=str(_ENV_FILE),
    env_file_encoding="utf-8",
    extra="ignore",
)


class DeepSeekSettings(BaseSettings):
    model_config = SettingsConfigDict(**_BASE_CONFIG, env_prefix="DEEPSEEK_")

    api_key: str = ""
    base_url_openai: str = ""
    base_url_anthropic: str = ""
    model: str = ""


class MiniMaxSettings(BaseSettings):
    model_config = SettingsConfigDict(**_BASE_CONFIG, env_prefix="MINIMAX_")

    api_key: str = ""
    base_url_openai: str = ""
    base_url_anthropic: str = ""
    model: str = ""


class DashScopeSettings(BaseSettings):
    model_config = SettingsConfigDict(**_BASE_CONFIG, env_prefix="DASHSCOPE_")

    api_key: str = ""
    base_url: str = ""
    model: str = ""


class MimoSettings(BaseSettings):
    model_config = SettingsConfigDict(**_BASE_CONFIG, env_prefix="MIMO_")

    api_key: str = ""
    base_url_openai: str = ""
    base_url_anthropic: str = ""
    model: str = ""


deepseek_settings = DeepSeekSettings()
minimax_settings = MiniMaxSettings()
dashscope_settings = DashScopeSettings()
mimo_settings = MimoSettings()
