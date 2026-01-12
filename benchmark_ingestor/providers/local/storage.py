from typing import Any, Dict, Optional
from benchmark_ingestor.core.storage import StorageBackend

class LocalStorage(StorageBackend):
    """
    Provider local Storage in memory for testing purposes or local development.

    - Uses to test and local development
    - Not use cloud providers
    - not use filesystem for now
    """

    def __init__(self):
        self._objects: Dict[str, Dict[str, Any]] = {}

    def put_json(self, key:str, data:Dict[str, Any], cache_cotrol:Optional[str]= None,) -> None:
        # cache control is ignored in local storage
        self._objects[key] = data

    def get_json(self, key:str) -> Dict[str, Any]:
        if key not in self._objects:
            raise FileNotFoundError(key)
        return self._objects[key]