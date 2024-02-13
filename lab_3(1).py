
def find(obj, value):
    if obj == value:
        return obj
    elif isinstance(obj, list):
        for item in obj:
            result = find(item, value)
            if result is not None:
                return result
    elif isinstance(obj, dict):
        for key, val in obj.items():
            result = find(val, value)
            if result is not None:
                return result
    return None
# Пример использования функции
obj = [1, 2, [3, 4, [5, [6, ["spam"]]]]]
print(find(obj, 6)) 
print(find(obj, 'spam'))


def find(obj, value):
    stack = [obj]
    while stack:
        current = stack.pop()
        if current == value:
            return current
        if isinstance(current, list):
            stack.extend(current)
    return None
obj = [1, 2, [3, 4, [5, [6, []]]]]
print(find(obj, 4))
print(find(obj, "spam")) 
