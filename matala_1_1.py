def convert(hours, minutes):
    if hours < 0 or minutes < 0:
        print("Input error!")

    elif hours and minutes > 0:
        print(hours * 60 * 60 + minutes * 60)


convert(1, 3)
