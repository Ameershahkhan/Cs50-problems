groccery = {}
while True:
    try:
        item = input()
        if item in groccery:
            groccery[item] += 1
        else:
            groccery[item] = 1

    except EOFError:
        print()
        break
    except KeyError:
        pass


for items, count in sorted(groccery.items()):
    items = items.upper()
    print(f"{count} {items}")
