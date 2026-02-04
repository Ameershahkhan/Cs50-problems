while True:
    try:
        fuel = input("Fraction x/y : ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        result = (x/y) * 100

        if result > 100 or result < 0:
            continue
        if result >= 99 and result <= 100:
            print("Fraction : F")
            break
        elif 0 <= result <= 1:
            print("Rraction : E")
            break
        else:
            print(f"Fraction : {result:.0f}%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
