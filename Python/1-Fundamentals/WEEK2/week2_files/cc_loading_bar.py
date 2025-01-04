for amount_loaded in range(0, 105, 5):
    if amount_loaded == 25:
        print("1/4 of the way there")
        continue
    elif amount_loaded == 50:
        print("1/2 of the way there")
        continue
    elif amount_loaded == 75:
        print("3/4 of the way there")
        continue
    elif amount_loaded == 100:
        print("Loading complete!")
        continue
    print(amount_loaded)