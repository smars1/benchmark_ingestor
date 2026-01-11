import pytest

from benchmark_ingestor.exceptions import (
    BenchmarkError,
    InvalidPayloadError,
    HistoryWriteError,
    StorageError,
    IngestorConfigError,
)

def test_history_write_error_is_benchmark_error():
    assert issubclass(HistoryWriteError, BenchmarkError)

def test_storage_error_is_benchmark_error():
    assert issubclass(StorageError, BenchmarkError)

def test_ingestor_config_error_is_benchmark_error():
    assert issubclass(IngestorConfigError, BenchmarkError)

def test_raise_and_catch_invalid_payload_error():
    with pytest.raises(InvalidPayloadError):
        raise InvalidPayloadError("Invalid payload")
