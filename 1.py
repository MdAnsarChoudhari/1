import sys

if(len(sys.argv))==2:
    script_name=sys.argv[0]
    celcius=float(sys.argv[1])

    fahrenheit=(celcius*9/5)+32
    print(f"{celcius} degree Celsius is equal to {fahrenheit} degree Fahrenheit")
else:
    script_name=sys.argv[0]
    celcius=25.0
    fahrenheit=(celcius*9/5)+32
    print(f"{celcius} degree Celsius is equal to {fahrenheit} degree Fahrenheit")