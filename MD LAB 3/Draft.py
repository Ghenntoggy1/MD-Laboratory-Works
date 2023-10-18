def findCheapestPrice(n, flights, src, dst, k):
    prices = [float("inf") for _ in range(n)]
    prices[src] = 0
    route = [src]
    # print(prices)

    for _ in range(k + 1):
        temp_prices = list(prices)
        # print(temp_prices)
        for source, dest, price in flights:
            flight_price = prices[source] + price
            if flight_price < temp_prices[dest]:
                route.append(source)
                temp_prices[dest] = flight_price
        prices = temp_prices
        print(temp_prices)

    if prices[dst] != float("inf"):
        route.append(dst)
        print(f"Route: {route}")
        return prices[dst]
    else:
        return -1


print(findCheapestPrice(9, [[0, 1, 4], [0, 7, 8], [1, 2, 8], [2, 3, 7], [3, 4, 9], [1, 7, 11], [7, 8, 7], [7, 6, 1], [8, 6, 6], [2, 8, 2], [2, 5, 4], [6, 5, 2], [5, 3, 14], [5, 4, 10]], 0, 7, 1))
