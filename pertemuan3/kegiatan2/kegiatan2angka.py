number1 = int(input("lebokno ongko pertamamu : "))
number2 = int(input("lebokno ongko keloromu : "))
number3 = int(input("lebokno ongko ketelumu : "))

if number1 > number2 and number1 > number3 :
    print(f"WAAHHHH ongko paling gede kui {number1}")
elif number2 > number1 and number2 > number3 :
    print(f"WAAHHHH ongko paling gede kui {number2}")
else: 
    print(f"WAAHHHH ongko paling gede kui {number3}")