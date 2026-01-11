# benchmark_ingestor/core/storage.py   
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class StorageBackend(ABC):
    """
    StorageBackend is an abstract base class that define the contract minimum for any sotorage.
    The core only uses this methods, it not matter the provider is AWS/GCP/Azure/OCI or local filesystem.
    
    """

    @abstractmethod
    def put_json(self, key:str, data:dict[str, Any], cache_control:Optional[str]= None) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_json(self, key:str) -> Dict[str, Any]:
        raise NotImplementedError
    
    def exists(self, key:str) -> bool:
        """
        Optional method. By default try to read.
        Providers can override it to provide a more efficient implementation.
        """
        try:
            self.get_json(key)
            return True
        except Exception:
            return False