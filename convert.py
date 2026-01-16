def convert(celcius):
    fahrenticies = (celcius * 9 / 5) + 32
    return f" fahrenticies {fahrenticies}"

if __name__ == "__main__":
    c = int(input("Enter Celcius : "))
    print(convert(c))
