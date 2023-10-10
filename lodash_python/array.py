import math

__all__ = ["chunk"]


def chunk(list_entries: list, size: int) -> list[list]:
    list_iterations = math.ceil(len(list_entries) / size)
    final_chunk = []
    for index in range(list_iterations):
        start_index = index * size
        final_chunk.append(list_entries[start_index: start_index + size])

    return final_chunk


chunk_result = chunk([1, 2, 3, 4, 5, 6, 7], 3)

print("Chunk Result = ", chunk_result)
