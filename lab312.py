def flatten(obj):
    result = []
    stack = [obj]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])
        else:
            result.append(current)
    return result

def find(obj, k):
    flattened_obj = flatten(obj)
    try:
        return flattened_obj.index(k)
    except ValueError:
        return None

obj = [1, 2, [3, 4, ['spam', [6, []]]]]
print(find(obj, 5))
print(find(obj, 'spam'))
