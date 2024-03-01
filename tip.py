#Tools In the store
biscuit = 300
caprisun = 400
cutlass = 500   
Scissors = 600

print("Welcome to my store the best store in the world")
print("What will You like to buy")
print("1.biscuit\n2.caprisun\n3.cutlass\n4.Scissors")
reply=str(input())
if reply  == "1" or reply == "biscuit":
    print(f"Biscuit is {biscuit}")
    purchase = biscuit
    tip = 0.08 * purchase
    print(f"We charge 0.03 of your purchase which is {tip}")
    total_purchase = purchase + tip
    print(f"Your total cost is ${total_purchase}")
    input = 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9 and 10
elif reply == "2" or reply == "caprisun":
    print(f"Caprisun is {caprisun}")
    purchase = caprisun
    tip = 0.08 * purchase
    print(f"We charge 0.03 of ypur purchase which is {tip}")
    total_purchase = purchase + tip
    print(f"Your total cost is ${total_purchase}")
elif reply ==  "3" or reply == "cutlass":
    print(f"Cutlass is {cutlass}")
    purchase = cutlass
    tip = 0.08 * purchase
    print(f"We charge 0.03 of your purchase which is {tip}")
    total_purchase = purchase + tip
    print(f"Your total cost is ${total_purchase}")
elif reply == "4" or reply == "scissors": 
    print(f"Scissors is {Scissors}")
    purchase = Scissors
    tip = 0.08 * purchase
    print(f"We charge 0.03 of your purchase which is {tip}")
    total_purchase = purchase + tip
    print(f"Your total cost is ${total_purchase}")
else:
   print("invalid request")

print("Are u Making a joint or single payment ")
print("1.joint payment\n2.single payment")
reply=str(input())
if reply == "1":
    print("How many people are paying")
    reply=int(input())
    ip = 0.08 * purchase
    print(f"We charge 0.03 of ypur purchase which is {tip}")
    total_purchase = purchase + tip
    individual_cost =total_purchase / reply
    print(f"Your total cost is ${total_purchase}")
    print("How much will i pay")
    inpu
    print({total_purchase/input})
elif reply == "2":
    print("How Much will i pay")
    ip = 0.08 * purchase
    print(f"We charge 0.03 of ypur purchase which is {tip}")
    total_purchase = purchase + tip
    print(f"Your total cost is ${total_purchase}")
else:
    print("invalid request")
print("Thank You for shopping with us ")



