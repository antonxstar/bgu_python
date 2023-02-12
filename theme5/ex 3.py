cities = ['Брест', 'Витебск', 'Гродно', 'Гомель', 'Минск', 'Могилёв']
mixed_list = [4, 4.5, 'Ноябрь', True, [1, 3, 4, 5], 'Pizza']
city = cities[2]
two_cities  = cities[3:5]
multiple_cities = [city] * 3 + two_cities
print(city, two_cities, multiple_cities)
# замена одного из элементов списка
cities[1] = 'Новый Витебск'
print(cities)
cities[3:] = []