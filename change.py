#Things in my supermarket
phone = 100000
Wifi = 200000
Television = 300000

print("WELCOME WHAT WILL YOU LIKE TO BUY")
print("1.phone\n2.Wifi\n3.Television")
reply=str(input())
if reply == "1" or reply =="phone":
    print(f"phone is {phone}")
    purchase = phone
    change = input
    change = purchase - 100000
    print(f"We will minus ur purchase to give you ur change which is {change}")
    total_purchase = purchase - change
    print(f"Your total cost is ${total_purchase}")
elif reply == "2" or reply =="Wifi":
    print(f"Wifi is {Wifi}")
    purchase = Wifi
    change = purchase - 100000
    print(f"We will minus ur purchase to give you ur change which is {change}")
    total_purchase = purchase - 100000
    print(f"Your total cost is ${Wifi}")
elif reply == "3" or reply =="Television":
    print(f"Television is {Television}")
    purchase = Television
    change = purchase - 100000
    print(f"We will minus ur purchase to give you ur change which is {change}")
    total_purchase = purchase - 100000
    print(f"Your total cost is ${Television}")
else:
    print("invalid request")    
print("Thank you for buying from us pls patronize us")    