prices = [8000, 12000, 18000, 25000, 9000, 30000]
filtered_prices = filter(lambda x: x >= 15000, prices)
discounted_prices = list(map(lambda x: x - 3000, filtered_prices))

print(discounted_prices)