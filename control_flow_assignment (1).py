#!/usr/bin/env python
# coding: utf-8

# # Task1:Discount Rules

# In[2]:


#Task 1.1 : read an integer order_amount from user 
order_amount=int(input("Enter Order Amount:"))
print("Order Amount:",order_amount)

#Task1.2 :apply discount rules
discount = 0.0
if order_amount >=2000:
    discount=0.15
elif 1500<=order_amount<2000:
    discount=0.10
elif 1000<=order_amount<=1500:
    discount=0.07
else:
    discount=0.0
discount_amount=order_amount*discount
final_amount=order_amount-discount_amount
print("Final Amount post discount is:",final_amount)


#Task1.3: Handling non input integer
input_order_amount=input("\nEnter a value:")
if type(input_order_amount)!=int:
    print("Enter an integer value for your order amount")
    


# # Task2:Process Multiple Orders

# In[15]:


#Task2.1 #for a list of order_amounts appply discount rule from task1
order_amount=[1200,2500,800,1750,3000]
print("Summary Table\n")
print("Order Amount  | Discount %  | Final Amount")
print("-"*50)
total_revenue=0.0
for i in order_amount:
    discount = 0.0
    if i >=2000:
        discount=0.15
    elif 1500<=i<2000:
        discount=0.10
    elif 1000<=i<=1500:
        discount=0.07
    else:
        discount=0.0
    discount_amount=i*discount
    final_amount=i-discount_amount
    total_revenue+=final_amount #for task 2.2
    print("Rs",i , "|", discount, "% | Rs.", final_amount)

#Task2.2 Print total revenue after discounts
print("\nTotal Revenue post applying discount on order amount is:",total_revenue)


    


# # Task3: User Menu

# In[16]:


order_amounts = []  

while True:
    print("\n------ MENU ------")
    print("Press 1 to Add order amount")
    print("Press 2 to Show all orders and total after discount")
    print("Press q to Quit")
    
    choice = input("Enter your choice: ")

    if choice == "q":
        print("Exiting program... Thank you!")
        break     # stops the while loop

    elif choice == "1":
        amount = float(input("Enter order amount: "))
        order_amounts.append(amount)
        print("Order added successfully!")

    elif choice == "2":
        if not order_amounts:
            print("No orders available.")
        else:
            total = 0

            print("\nOrders after discount:")
            for i in order_amounts:
                discount = 0.0

                if i >= 2000:
                    discount = 0.15
                elif 1500 <= i < 2000:
                    discount = 0.10
                elif 1000 <= i <= 1500:
                    discount = 0.07
                else:
                    discount = 0.0

                final_price = i - (i * discount)
                total += final_price

                print("Order_amount:" ,i, "Discount:" , discount,"%", "Final:",final_price)

            print("Total payable amount:", total)

    else:
        print("Invalid option! Please try again.")
        continue    # re-show the menu for task 3.2


# # Task 4:Loop conteol with conditions

# In[17]:


#Task 4.1 and 4.2 -->iterating over daily sales and calculating running totala nd finally dispalying total revenue 

daily_sales = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for sale in daily_sales:
   
    if sale == -1: # If corrupted data then stop processing
        break

    if sale == 0:# If no sales that day, skip it
        continue

    total_sales += sale

print("\nFinal total sales:", total_sales)


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# # Task1:Discount Rules

# In[2]:


#Task 1.1 : read an integer order_amount from user 
order_amount=int(input("Enter Order Amount:"))
print("Order Amount:",order_amount)

#Task1.2 :apply discount rules
discount = 0.0
if order_amount >=2000:
    discount=0.15
elif 1500<=order_amount<2000:
    discount=0.10
elif 1000<=order_amount<=1500:
    discount=0.07
else:
    discount=0.0
discount_amount=order_amount*discount
final_amount=order_amount-discount_amount
print("Final Amount post discount is:",final_amount)


#Task1.3: Handling non input integer
input_order_amount=input("\nEnter a value:")
if type(input_order_amount)!=int:
    print("Enter an integer value for your order amount")
    


# # Task2:Process Multiple Orders

# In[3]:


#Task2.1 #for a list of order_amounts appply discount rule from task1
order_amount=[1200,2500,800,1750,3000]
print("Summary Table\n")
print(f"{'Order Amount':<15} | {'Discount %':<12}| {'Final Amount':<12}")
print("-"*50)
total_revenue=0.0
for i in order_amount:
    discount = 0.0
    if i >=2000:
        discount=0.15
    elif 1500<=i<2000:
        discount=0.10
    elif 1000<=i<=1500:
        discount=0.07
    else:
        discount=0.0
    discount_amount=i*discount
    final_amount=i-discount_amount
    total_revenue+=final_amount #for task 2.2
    print(f"Rs{i:<14.2f}| {discount:>10}% | Rs.{final_amount}")

#Task2.2 Print total revenue after discounts
print("\nTotal Revenue post applying discount on order amount is:",total_revenue)


    


# # Task3: User Menu

# In[6]:


order_amounts = []   # running list to store all orders

while True:
    print("\n------ MENU ------")
    print("Press 1 -> To Add order amount")
    print("Press 2 -> To Show all orders and total after discount")
    print("Press q -> To Quit")
    
    choice = input("Enter your choice: ")

    if choice == "q":
        print("Exiting program... Thank you!")
        break     # stops the while loop

    elif choice == "1":
        amount = float(input("Enter order amount: "))
        order_amounts.append(amount)
        print("Order added successfully!")

    elif choice == "2":
        if not order_amounts:
            print("No orders available.")
        else:
            total = 0

            print("\nOrders after discount:")
            for i in order_amounts:
                discount = 0.0

                if i >= 2000:
                    discount = 0.15
                elif 1500 <= i < 2000:
                    discount = 0.10
                elif 1000 <= i <= 1500:
                    discount = 0.07
                else:
                    discount = 0.0

                final_price = i - (i * discount)
                total += final_price

                print(f"Order_amount: {i}, Discount: {discount}%, Final: {final_price}")

            print("Total payable amount:", total)

    else:
        print("Invalid option! Please try again.")
        continue    # re-show the menu for task 3.2


# # Task 4:Loop conteol with conditions

# In[8]:


#Task 4.1 and 4.2 -->iterating over daily sales and calculating running totala nd finally dispalying total revenue 

daily_sales = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily_sales:

    # If corrupted data found, stop processing
    if sale == -1:
        print("Corrupted data found! Stopping processing.")
        break

    # If no sales that day, skip it
    if sale == 0:
        print("No sales today. Skipping.")
        continue

    # Valid positive sales
    total_sales += sale
    print("Added daily_sale value of:", sale, "Running total is:", total_sales)

print("\nFinal total sales:", total_sales)


# In[ ]:



