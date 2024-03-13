import math

__all__ = ["list_functions"]


def chunk(list_entries: list, size: int) -> list[list]:
    list_iterations: int = math.ceil(len(list_entries) / size)
    final_chunk: list = []
    for index in range(list_iterations):
        start_index = index * size
        final_chunk.append(list_entries[start_index: start_index + size])

    return final_chunk


def concat(first_list: list, second_list: list) -> list:
    return first_list + second_list


def compact(list_entries: list):
    filtered_list = []
    for item in list_entries:
        if item:
            filtered_list.append(item)

    return filtered_list


def difference(list_entries: list, list_to_exclude: list):
    final_list = []
    for item in list_entries:
        item_matched = False
        for exclude_item in list_to_exclude:
            if exclude_item == item:
                item_matched = True

        if not item_matched:
            final_list.append(item)

    return final_list


def drop(list_entries: list, offset: int):
    if offset >= len(list_entries):
        return []

    return list_entries[offset: len(list_entries)]


def find(list_entries: list, value: str or int):
    list_length = len(list_entries)

    value_found = False
    for index in range(list_length):
        if value == list_entries[index]:
            value_found = True
            return
        # print(index)

    if value_found:
        print('Value Present in List')
    else:
        print('Value Not Present in List')


def list_functions():
    chunk_result = chunk([1, 2, 3, 4, 5, 6, 7], 3)
    print("Chunk Result = ", chunk_result)

    concat_result = concat([1, 2], [3, 4])
    print("Concat Result = ", concat_result)

    compact_result = compact([0, '1', 2, '', False, 3, {"a": "b"}, True])
    print("Compact Result = ", compact_result)

    difference_result = difference([1, 2, 3, 4], [2, 3])
    print("Difference Result = ", difference_result)

    drop_result = drop([1, 2, 3, 4], 2)
    print("Drop Result = ", drop_result)

    find([1, 2, 3, 4], 2)
