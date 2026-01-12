import pytest
from benchmark_ingestor.providers.local.storage import LocalStorage

def test_local_storage_put_and_get():
    storage = LocalStorage()
    storage.put_json("a.json", {"x": 1})
    assert storage.get_json("a.json") == {"x": 1}

def test_local_storage_missing_key():
    storage = LocalStorage()
    with pytest.raises(FileNotFoundError):
        storage.get_json("missing.json")