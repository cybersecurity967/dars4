def positive_equal(*sonlar):
    return sum(n for n in sonlar if n > 0)

print(positive_equal(-3, 5, 0, 12, -1))