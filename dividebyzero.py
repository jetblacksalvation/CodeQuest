for input_count in range(int(input())):
    dividend, divisor = (input()+'').split()
    try:
        dividend = float(dividend)
    except:
        print("Invalid Dividend")
    try:
        divisor = float(divisor)
    except:
        print("Invalid Divisor")
    if divisor == 0:
        print("Divide By Zero")

        pass
    else:
        try:
            print(round(float(dividend/divisor),1))
        except:
            pass
    pass
