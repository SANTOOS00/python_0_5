
def ft_recursive(days):
    i = 0;
    if (days > 0):
        i += ft_recursive(days - 1)
        print (f"Day {i}")
    return i + 1
def ft_count_harvest_recursive():
    days = int (input("Days until harvest: "))
    ft_recursive(days)
    print ("Harvest time!")
