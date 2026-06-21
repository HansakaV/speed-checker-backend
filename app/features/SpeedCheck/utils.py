def dummy_data_generator(size_in_mb: int):
    chunk_1mb = b"\x00" * (1024 * 1024)
    for _ in range(size_in_mb):
        yield chunk_1mb
