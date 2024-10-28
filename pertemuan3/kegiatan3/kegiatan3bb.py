def standarnih(weight, height):
    height2 = height / 100
    standarnih = weight / height2 ** 2
    return standarnih

weight = int(input(" Masukkan berat badanmu (Kg): "))
height = int(input(" Masukkan tinggi badanmu (Cm): "))

standarnih = standarnih(weight, height)
print(f"Nilai BMI kamu adalah : {standarnih}")

if standarnih < 18.5:
    print("u sangat kurus aaaa")
elif standarnih >= 18.5 and standarnih < 25:
    print("Alhamdulillah u ideallll")
else:
    print("haia banyakin olahlaga oo, u gemuk sangaattt")
