coffee_shops = ['starbucks', 'dunkin', 'peets', 'philz', 'blue bottle', 'intelligentsia']

# append
coffee_shops.append('lavazza')
print(coffee_shops)

# insert
coffee_shops.insert(2, 'coffee bean')
print(coffee_shops)

# remove
coffee_shops.remove('dunkin')
print(coffee_shops)

# del
del coffee_shops[0]
print(coffee_shops)

del coffee_shops[-1]
print(coffee_shops)

# len
print(len(coffee_shops))

# sort
coffee_shops.sort()
print(coffee_shops)
