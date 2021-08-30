"""Module with abstract ingestor interfact."""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class for file ingestion."""

    allowed_extensions = ['csv', 'docx', 'pdf', 'txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine whether file is ingestible."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quote file."""
        pass
