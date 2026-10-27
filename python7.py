
stock = int(input("Enter available stock: "))
order = int(input("Enter order quantity: "))
dispatch = int(input("Enter dispatched quantity: "))
returned = int(input("Enter returned quantity: "))

if (min(stock, order, dispatch, returned) < 0 or
    dispatch > order or dispatch > stock or returned > dispatch):
    print("Invalid records")
else:
    pending = order - dispatch
    stock = stock - dispatch + returned

    print("Outstanding orders:", pending)
    print("Updated stock:", stock)
    print("Successfully delivered:", dispatch - returned)
