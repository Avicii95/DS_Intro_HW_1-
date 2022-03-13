def my_func(*args):
    try:
        x1 = float(args[0])
        x2 = float(args[1])
        x3 = float(args[2])

        x = ((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3)

        if x1 + x2 + x3 == 0:
            print("not a number - denominator equals zero")

        else:
            print(x)

    except:
        print("not a number - denominator equals zero")


my_func(-1, -2, 3)
