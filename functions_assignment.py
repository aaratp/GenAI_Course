#!/usr/bin/env python
# coding: utf-8

# # Task 1: Basic Function :price After Discount

# In[1]:


def apply_discount(price,discount_percent=5):
    if discount_percent: #if discount is given
        discount_amount=price *(discount_percent/100)  # calculate disocunt   
        amount= price - discount_amount #calculate discounted price
    else:
        amount= price * 0.05
    print("Price after discount is:",amount)
    
apply_discount(1000,10)
apply_discount(500)


# # task 2: recursive function :factorial Utility

# In[2]:


def factorial(n): #function to find factorial of a number
    if n<0:
        return "Cant calculate factorial for a negative number"      
    elif n ==0 or n==1:
        return 1
    else: 
        return n*factorial(n-1)
            
print("factorial of 5 is:",factorial(5))
print("factorial of 0 is:",factorial(0))
print("factorial of -3 is:",factorial(-3))


# # task 3:Lambda function:Gst calculator

# In[3]:


def gst_calc(price): #function to calculate price with gst
    final_amount=lambda p:p + p*0.18
    return final_amount(price)
print("Amount after adding GST is:",gst_calc(100))


# # task 4:Using Map :apply Gst to list of prices

# In[4]:


prices=[100,250,400,1200,50,2000,850] #apply 18% GSt on each of the prices

prices_with_gst=list(map((lambda p:p + p*0.18),prices))

print("Original price list:",prices)
print("List after adding GST:",prices_with_gst)
      


# # Task 5:using Filter: Filter expensive products

# In[5]:


prices=[100,250,400,1200,50,2000,850] #split using filter lists above 500 and below 500

l1=list(filter(lambda x:x<=500,prices))
l2=list(filter(lambda x:x>500,prices))
print("Prices above 500 are:",l2)
print("prices below 500 are:",l1)


# # Task 6 :Combined functionality

# In[6]:


def process_prices(prices): # method that shall apply disocunt on price lista nd also give a list of prices below rs 300
    discount_amount = lambda x: x + x * 0.10
    discounted_price_list = list(map(discount_amount, prices))
    l1 = list(filter(lambda x: x > 300, discounted_price_list))
    return discounted_price_list, l1


a,b=process_prices([100, 500, 900, 50, 750])
print("Prices post Discount is:",a)
print("Prices within rs300 post applying discount is:",b)


# # task 7: menu using Functions

# In[7]:


def add_price(prices_list, price):
    prices_list.append(price)
    return prices_list

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    total = 0
    for i in prices_list:
        total += i
    return total / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    max_price = prices_list[0]
    for i in prices_list:
        if i > max_price:
            max_price = i
    return max_price


prices_list = [100, 500, 900, 50, 750] 

while True:
    print("\n---- MENU ----")
    print("1 -> Add Price to the list\n")
    print("2 -> Show Average Price\n")
    print("3 -> Show Highest Price\n")
    print("q -> Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        price = float(input("Enter price: ")) 
        add_price(prices_list, price)

    elif choice == "2":
        print("Average Price:", get_average_price(prices_list))

    elif choice == "3":
        print("Highest Price:", get_max_price(prices_list))

    elif choice == "q":
        print("Quit")
        break
    else:
        print("Invalid choice!")


# In[ ]:




