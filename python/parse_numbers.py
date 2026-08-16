#pa


values = ["10", "invalid", "20", ""]




def parse_numbers(values):
    numbers=[]

    for value in values:
        try:
            numbers.append(int(value))

        except ValueError:
            continue
            





    return numbers



print(parse_numbers(values))