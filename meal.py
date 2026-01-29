
def main():

    while True:
        bill = get_bill(input("Enter bill : "))
        tip = input("Enter tip : ")
        tip_cal = tip
        tip_cal = get_tip(tip_cal)
        tip_cal = bill * tip_cal
        total = bill + tip_cal
        print("------reciept------")
        print(f"Bill Amount : {bill:.2f}")
        print(f"Tip ({tip})   : {tip_cal:.2f}")
        print(F"Total       : {total}")
        print("-------------------")


def get_bill(n):
    n = n.strip()
    n = n.removeprefix("$")
    n = n.removeprefix("Rs")
    n = n.replace(",", "")
    n = float(n)
    if n < 0:
        print("Negative numbers are not allowed.")

    return n


def get_tip(x):
    x = x.strip()
    if x.endswith("%"):
        x = x.removesuffix("%")
        x = float(x)
        x = x / 100
    else:
        x = float(x)
        if x > 1:
            x = x / 100

    return x


main()
