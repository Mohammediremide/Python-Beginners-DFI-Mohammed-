#location of the bus stops
Iyana_paja = 200
Ikeja = 400
Ayobo = 500
Egbeda = 600
Apapa = 700

print("1.iyana paja\n2. ikeja\n3. Ayobo\n4. Egbeda\n5. Apapa")
print("where will you like to go")

reply=str(input())

if reply =="1" or reply == "i":
    print(f"Your tfare is {Iyana_paja}")
elif reply =="2":
    print(f"Your tfare is {Ikeja}")
elif reply =="3":
    print(f"Your tfare is {Ayobo}")
elif reply =="4":
    print(f"Your tfare is {Egbeda}")
elif reply =="5":
    print(f"Your tfare is {Apapa}")
else:
    print("invalid request")