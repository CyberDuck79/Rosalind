# Rabbits and Recurrence Relations
def rabbit(n, k):
    a = 1
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a * k + b
            a = b
            b = c
        return b

print(rabbit(30, 3))