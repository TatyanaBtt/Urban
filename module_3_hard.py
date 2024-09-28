def calculate_structure_sum(data):
    total_sum_length = 0

    for item in data:
        if isinstance(item, int):
            total_sum_length += item
        if isinstance(item, str):
            total_sum_length += len(item)
        if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            total_sum_length += calculate_structure_sum(item)
        if isinstance(item, dict):
            for values in item.values():
                if isinstance(values, int):
                    total_sum_length += values
                if isinstance(values, str):
                    total_sum_length += len(values)
                if isinstance(values, list) or isinstance(values, tuple) or isinstance(values, set):
                    total_sum_length += calculate_structure_sum(values)
            for key in item.keys():
                if isinstance(key, int):
                    total_sum_length += key
                if isinstance(key, str):
                    total_sum_length += len(key)
                if isinstance(key, list) or isinstance(key, tuple) or isinstance(key, set):
                    total_sum_length += calculate_structure_sum(key)
    return total_sum_length
data_structure = [
  [1, {1, (52, 'World')}, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)



