# 2. Cheapest Flights
s = int(input("Input number of cities: "))
start = int(input("Input start city: "))
destination = int(input("Input destination city: "))
k = int(input("Input maximum number of stops: "))
number_array = int(input("Input number of available flights: "))
list_of_flights = []
for i in range(number_array):
    print(f'Flight {i + 1}:')
    # cities = input('From - to:')
    cfrom = int(input("From: "))
    cto = int(input('To: '))
    # c_list = cities.split()
    # cfrom = c_list[0]
    # cto = c_list[1]
    price = int(input('Price: '))
    list_of_flights.append([cfrom, cto, price])
# print(list_of_flights)

prices = [0]
for i in range(s - 1):
    prices.append(float('inf'))
# print(prices)
for city_visited in range(k + 1):
    aux_list = list(prices)
    for city_from, city_to, price_flight in list_of_flights:
        fl_price = prices[city_from] + price_flight
        if fl_price < aux_list[city_to]:
            aux_list[city_to] = fl_price
            # print(aux_list)
    prices = aux_list
# print(prices)
if prices[destination] != float("inf"):
    print(f"Price: {prices[destination]}")
else:
    print("No route!")