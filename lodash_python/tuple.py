import math


def tuple_chunk(tuple_entries: tuple, size: int):
    tuple_iterations: int = math.ceil(len(tuple_entries) / size)
    final_chunk: tuple = ()
    for index in range(tuple_iterations):
        start_index = index * size
        print(tuple_entries[start_index: start_index + size])
        final_chunk = final_chunk + tuple_entries[start_index: start_index + size]

    return final_chunk


tuple_chunk_result = tuple_chunk((1, 2, 3, 4, 5, 6, 7), 2)
print("Tuple Chunk Result = ", tuple_chunk_result)
