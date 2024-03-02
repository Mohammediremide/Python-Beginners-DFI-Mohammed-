#Tools in the store
print("Welcome to the mohammed store")
print("What will you like to buy")
biscuit = 250
caprisun = 450
cutlass = 500
scissors = 600

print("1.biscuit\n2.caprisun\n3.cutlass\n4.scissors")
reply=str(input())
if reply  == "1":
   print("How many are you buying")
   quantity = int(input())
   purchase = biscuit
   tip = 0.03 * purchase
   total_purchase = biscuit + tip
   print(f"We charge 0.03 of your purchase which is {tip}")
   total_purchase = biscuit * quantity
   total_cost = total_purchase + tip
   print(f"Your total cost is NGN{total_cost}")
elif reply == "2":
   print("How many are you buying")
   quantity = int(input())
   purchase = caprisun
   tip = 0.03 * purchase
   total_purchase = caprisun + tip
   print(f"We charge 0.03 of your purchase which is {tip}")
   total_purchase = caprisun*quantity
   total_cost = total_purchase + tip
   print(f"Your total cost is NGN{total_cost}")
elif reply == "3":
   print("How many are you buying")
   quantity = int(input())
   purchase = cutlass
   tip = 0.03 * purchase
   total_purchase = cutlass + tip
   print(f"We charge 0.03 of your purchase which is {tip}")
   total_purchase = cutlass * quantity
   total_cost = total_purchase + tip
   print(f"Your total cost is NGN{total_cost}")
elif reply == "4":
   print("How many are you buying")
   quantity = int(input())
   purchase = scissors
   tip = 0.03 * purchase
   total_purchase = scissors + tip
   print(f"We charge 0.03 of your purchase which is {tip}")
   total_purchase = scissors * quantity
   total_cost = total_purchase + tip
   print(f"Your total cost is NGN{total_cost}")
else:
   print("invalid request")

print("Are u making bank or cash payment")
print("1.Bank payment\n2.cash payment")
reply=str(input())
if reply == "1":
   print(f"Please pay NGN{total_cost}")
print("Are u making single or joint payment")
print("1.joint payment\n2.single payment")
reply=str(input())
if reply == "1":
   print("How many people are paying")
   reply=int(input())
   individual_cost = total_cost / reply
   print(f"Your total cost is NGN{total_cost}")
   print(f"{total_cost / reply}")
elif reply == "2":
   print(f"Your total_cost is your is NGN{total_cost} ")
   
else:
   print("invalid request")

if reply == "2":
   print(f"Please pay NGN{total_cost}")
reply=str(input())
if reply == "a":
   print("How many people are paying")
   reply=int(input())
   individual_cost = total_cost / reply
   print(f"Your total cost is NGN{total_cost}")
   print(f"{total_cost / reply}")
elif reply == "b":
   print(f"Your total_cost is your is NGN{total_cost} ")
print("Thank you for shopping with us")

