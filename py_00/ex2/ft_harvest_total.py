
def ft_harvest_total():
    i = 0
    res = 0
    while i < 3:
        res += int(input(f"Day {i + 1} harvest: "))
        i += 1
    print (f"Total harvest: {res}")
