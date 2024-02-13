u = 1
v = 1

def calculate_recursive(u, v, k):
    if k == 1:
        return u, v
    
    a_prev, b_prev = calculate_recursive(u, v, k-1)
    
    a = 2*b_prev + a_prev
    b = (2*b_prev)**2 + b_prev
    
    return a, b

def calculate(u, v, k):
    a = [u]
    b = [v]
    
    for i in range(1, k+1):
        a.append(2*b[i-1] + a[i-1])
        b.append((2*b[i-1])**2 + b[i-1])

    
    return a[k-1], b[k-1]  # Поправили индексы на k-1

k = int(input("k = "))

result_recursive = calculate_recursive(u, v, k)
result = calculate(u, v, k)
print("С рекурсией:")
print("a[{}] = {}".format(k, result_recursive[0]))
print("b[{}] = {}".format(k, result_recursive[1]))

print("Без рекурсии:")
print("a[{}] = {}".format(k, result[0]))
print("b[{}] = {}".format(k, result[1]))