import os
from dataclasses import dataclass
from typing import Optional
from pathlib import Path

@dataclass
class Settings:
    """Production configuration settings."""
    
    # LLM Configuration
    use_openai: bool = False
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4-turbo-preview"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "ollama/mistral"
    temperature: float = 0.7
    
    # API Keys for Tools
    tavily_api_key: Optional[str] = None
    brave_api_key: Optional[str] = None
    serper_api_key: Optional[str] = None
    
    # Database Configuration
    database_url: str = "crewai_production.db"
    vector_store_path: str = "vector_store"
    
    # System Configuration
    max_iterations: int = 5
    verbose: bool = True
    log_level: str = "INFO"
    
    # Performance Configuration
    max_concurrent_crews: int = 3
    memory_limit_mb: int = 2048
    
    # File Upload Configuration
    upload_dir: str = "uploads"
    max_file_size_mb: int = 50
    allowed_extensions: list = None
    
    def __post_init__(self):
        """Initialize default values and create directories."""
        if self.allowed_extensions is None:
            self.allowed_extensions = ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.csv']
        
        # Create necessary directories
        for directory in [self.upload_dir, self.vector_store_path, "logs", "data"]:
            Path(directory).mkdir(exist_ok=True)
    
    @classmethod
    def from_env(cls) -> 'Settings':
        """Load settings from environment variables."""
        return cls(
            use_openai=os.getenv('USE_OPENAI', 'false').lower() == 'true',
            openai_api_key=os.getenv('OPENAI_API_KEY'),
            openai_model=os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview'),
            ollama_base_url=os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434'),
            ollama_model=os.getenv('OLLAMA_MODEL', 'ollama/mistral'),
            temperature=float(os.getenv('TEMPERATURE', '0.7')),
            tavily_api_key=os.getenv('TAVILY_API_KEY'),
            brave_api_key=os.getenv('BRAVE_API_KEY'),
            serper_api_key=os.getenv('SERPER_API_KEY'),
            database_url=os.getenv('DATABASE_URL', 'crewai_production.db'),
            vector_store_path=os.getenv('VECTOR_STORE_PATH', 'vector_store'),
            max_iterations=int(os.getenv('MAX_ITERATIONS', '5')),
            verbose=os.getenv('VERBOSE', 'true').lower() == 'true',
            log_level=os.getenv('LOG_LEVEL', 'INFO'),
            max_concurrent_crews=int(os.getenv('MAX_CONCURRENT_CREWS', '3')),
            memory_limit_mb=int(os.getenv('MEMORY_LIMIT_MB', '2048')),
            upload_dir=os.getenv('UPLOAD_DIR', 'uploads'),
            max_file_size_mb=int(os.getenv('MAX_FILE_SIZE_MB', '50'))
        )