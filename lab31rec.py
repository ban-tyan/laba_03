def flatten(obj):
    result = []
    for i in obj:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
obj = [1, 2, [3, 4, [5, [6, []]]]]
flattened_obj = flatten(obj)

def find(obj, k):
    flattened_obj = flatten(obj)
    try:
        return flattened_obj.index(k)
    except ValueError:
        return None

obj = [1, 2, [3, "spam", [4, [6, []]]]]
print(find(obj, 5))
print(find(obj, 'spam'))


