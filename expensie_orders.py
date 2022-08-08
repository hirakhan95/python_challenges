# def expensive_orders(orders, cost):
#     expensive_stuff = ()
#     for k, v in enumerate(orders):
#         if v[1] > cost:
#             expensive_stuff += v
#     return expensive_stuff

# def expensive_orders(orders, cost):
#     expensive_stuff = {}
#     for k in orders:
#         if orders[k] > cost:
#             expensive_stuff[k] = orders[k]
#     return expensive_stuff

def expensive_orders(orders, cost):
    expensive_stuff = {}
    for k, v in orders.items():
        if v > cost:
            expensive_stuff[k] = v
    return expensive_stuff


print(expensive_orders({"a": 3000, "b": 200, "c": 1050}, 1000))
#{"a": 3000, "c": 1050}