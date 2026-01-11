# benchmark_ingestor/exceptions.py

class BenchmarkError(Exception):
    pass


class InvalidPayloadError(BenchmarkError):
    pass


class HistoryWriteError(BenchmarkError):
    pass


class StorageError(BenchmarkError):
    pass

class IngestorConfigError(BenchmarkError):
    pass    

# test/test_exceptions.py