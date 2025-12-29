def ft_harvest_total():
    i = 0
    res = 0
    while i < 3:
        res += int(input("Day "+ str(i + 1) +" harvest: "))
        i += 1
    print ("Total harvest: ",res)
ft_harvest_total()