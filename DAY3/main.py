# discount = 0.10
# def apply_discount(price):
# # Bug lurking here...
# discounted_price = price - (price * discount)
# return discounted_price
# print("Welcome to the Cafe!")
# user_input = input("Enter your total bill: ")
# # Bug lurking here...if user_input > 100:
# final_price = apply_discount(user_input)
# print(f"You get a discount! Pay: {final_price} ETB")
# else:
# print(f"No discount. Pay: {user_input} ETB")

item=[("Coffee Beans", 500), ("Honey", 800), ("Spices",
300)];


for item,price in item:
#    print(f"{item}: {price} ETB");
   avaliable_items = input("Enter the item you want to buy: ");
   if not avaliable_items:
      print("Item not available");
      break;
   inital_price = float(input("Enter the price of the item: "));
   print(price); 
   def evaluate_offer(base_price, user_offer):
        if user_offer >= base_price:
         return True;
        elif user_offer == base_price*0.85:
         return True;
        else:
         print(f"Too low! My counter-offer is {base_price*0.90} ETB")
        return False;
        
   evaluate_offer(item[price], inital_price)  
   