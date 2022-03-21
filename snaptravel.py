import json
import bisect

try:
    num_of_hotels = input()
except EOFError as e:
    print('Expected input but none found.')
    exit(1)

hotels = {}

"""
  Construct dictionary of hotels per city:
  {
    'city': [
      {
        'supplier': 'supplier',
        'price': 'price',
      },
      ...
    ],
    ...
  }
"""
for i in range(num_of_hotels):
    try:
        line = raw_input()
    except EOFError as e:
        print('Expected input but none found.')
        exit(1)

    city, supplier, price = line.split(",")
    hotel = {
        "supplier": supplier,
        "price": float(price)
    }
    if city in hotels.keys():
        hotels[city].append(hotel)
    else:
        hotels[city] = [hotel]

try:
    num_of_queries = input()
except EOFError as e:
    print('Expected input but none found.')
    exit(1)

# Handle hotel queries
for i in range(0, num_of_queries):
    try:
        line = raw_input()
    except EOFError as e:
        print('Expected input but none found.')
        exit(1)

    city, days = line.split(",")
    hotels_in_city = hotels.get(city)

    # prices is a sorted list of prices
    prices = []

    for hotel in hotels_in_city:
        price = None
        if hotel.get("supplier") == "A" and int(days) == 1:
            # increase price by 50%
            price = float("{0:.2f}".format(hotel.get("price") * 1.5))

        elif hotel.get("supplier") == "C" and int(days) >= 7:
            # 10% discount
            price = float("{0:.2f}".format(hotel.get("price") * 0.9))

        elif hotel.get("supplier") == "D" and int(days) < 7:
            # increase price by 10%
            price = float("{0:.2f}".format(hotel.get("price") * 1.1))

        elif hotel.get("supplier") != "B" or int(days) >= 3:
            # in this case, no change in price
            # this takes care of the case where the supplier is B and
            # the days until check-in is less than 3, then it is not possible
            # to book the hotel
            price = float("{0:.2f}".format(hotel.get("price")))

        # insert the price in the right order if the hotel is bookable
        if price is not None:
            bisect.insort(prices, price)

    # Print results for all queries
    if len(prices) == 0:
        print("None")
    else:
        print(json.dumps(prices)[1:-1])

# https://codeinterview.io/EOSZVYLQIF