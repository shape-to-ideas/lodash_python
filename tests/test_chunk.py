from lodash_python.list_data import chunk


def test_chunk():
    chunk_size = 2
    chunk_result = chunk([1, 2, 3, 4, 5, 6], chunk_size)
    first_chunk = chunk_result[0]
    assert len(first_chunk) == chunk_size
