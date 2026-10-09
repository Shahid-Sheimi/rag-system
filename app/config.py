from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Vector DB
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str = ""
    collection: str = "knowledge_base"

    # OpenAI
    openai_api_key: str = ""
    llm_model: str = "gpt-4o"
    embedding_provider: str = "openai"          # openai | local
    embedding_model: str = "text-embedding-3-small"
    embedding_dim: int = 1536
    query_prefix: str = ""                      # only for local bge-style models

    # SQL
    database_url: str = ""
    sql_sources_file: str = "sql_sources.yaml"
    realtime_outbox: bool = False
    outbox_table: str = "dbo.rag_outbox"
    realtime_postgres: bool = False

    # Chunking
    chunk_size: int = 1000
    chunk_overlap: int = 150
    csv_rows_per_chunk: int = 5

    data_dir: str = "data"
    manifest_path: str = "data/manifest.db"


settings = Settings()
FILES_DIR = Path(settings.data_dir) / "files"
FILES_DIR.mkdir(parents=True, exist_ok=True)
SUPPORTED_EXT = {".pdf", ".csv", ".docx", ".txt", ".md"}
