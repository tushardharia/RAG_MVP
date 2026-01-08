from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    # API Keys
    GEMINI_API_KEY: str
    OPENAI_API_KEY: str = ""  # Optional, only needed if using OpenAI chat service
    
    # File Paths
    PDF_FILE_PATH: str  # Required: Path to the PDF file to process
    DATA_DIR: str = "data"
    PDF_DIR: str = "data/pdf"
    
    # Storage Configuration
    CHROMA_STORAGE_PATH: str = "chroma_persistent_storage"
    CHROMA_COLLECTION_NAME: str = "document_collection"
    
    # Model Configuration
    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"
    GEMINI_MODEL_NAME: str = "gemini-3-flash-preview"
    OPENAI_MODEL_NAME: str = "gpt-3.5-turbo"
    
    # Qdrant Configuration (optional)
    QDRANT_URL: str = "http://localhost:6333"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    
    def get_pdf_path(self) -> Path:
        """Get the PDF file path as a Path object."""
        return Path(self.PDF_FILE_PATH)
    
    def get_chroma_storage_path(self) -> Path:
        """Get the Chroma storage path as a Path object."""
        return Path(self.CHROMA_STORAGE_PATH)


settings = Settings()