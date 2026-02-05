#!/usr/bin/env python
# coding: utf-8

# # TASK 1: Product collections

# In[13]:



#Task1.1 - create a list of 6 products
products=["Rose","Dairy Milk Silk","Birthday photo frame","Dora keychain","Teddy bear","Little buddha"]
print("Initial Product List:",products)

#Task 1.2 - create a tuple for 1 product holding product name , price and category
sample_product=('Dairy Milk Silk','50','Choclates')
print("\nInitial SampleProduct List:",sample_product)

#Task 1.3- print 2nd and last product from the list
print("\nsecond product from our product list is:",products[1])
print("\nlast product from the product list is:",products[-1])

#Task 1.4 - append 2 product names 
new_products=["Kitkat","Tulips"]
products.extend(new_products)
print("\nUpdated product list is:",products)

#extra task - convert tuple to list , change the price and convert back to tuple
sample_product=list(sample_product)
sample_product[1]="48"
sample_product=tuple(sample_product)
print("\nUpdated sample product:",sample_product)


# # Task2: categories

# In[61]:


#task2.1-create a set with ctaegory names
categories_set={'flower','choclate','frames','keychain','soft toys','gifts under 100','choclate','flower'}
print("Categories of products are:",categories_set)

#task 2.2 - add a new category and also show duplicates are ignored 
categories_set.add("fancy items")
categories_set.add("frames") #duplicate
print("\nCategories of products now are:",categories_set)

#task2.3 - check if a category exist or not 
print("\nChecking if frames is one of the product categories:","frames" in categories_set)

#Extra Task: - total number of unique category
print("\nTotal number of unique categories are:",len(categories_set))


# # Task3:Product Pricing

# In[48]:


#Task3.1 - dict having key as product and value as price
price_dict={"Dairy Milk Silk":48, "Rose":20 , "Teddy bear":92.75 , "Birthday photo frame":250 , "Little buddha":50 , "Dora keychain":32.5}
print("Initial Dict:",price_dict)

#Task3.2 - adding a new key to dict 
price_dict["Kitkat"]=30
print("\nDictionary after adding a product:",price_dict)

#Updating price of Rose from 20 to 40 rs
price_dict["Rose"]=40
print("\nDictionary after updating price of Rose:",price_dict)

#delting a product from dict 
try:
    del price_dict["BirthdayFrame"] 
    print("\nDictionary after deleting:",price_dict)
    del price_dict["abc"] # showcasing value doesnt exist case
    print("\nDictionary after deleting:",price_dict)
except:
    print("Key not found in dictionary")

#Task 3.3- finding avg value of all products in dict
values=price_dict.values()
total_sum=sum(values)
values_len=len(values)
average=total_sum/values_len
print("\nAverage price of all products is:",average)

#Extra task:- find product with max and price 
print("\nProduct with max price is:", max(price_dict , key=price_dict.get))
print("\nProduct with min price is:", min(price_dict , key=price_dict.get))


# # Task4:Combined Operations

# In[60]:


#task4.1 - create a list of tuples [(prod1,price,category),(prod2,price,category),....]
#cretaing a map to map products with ctaegory so that we can create a tuple
products = ["Rose","Dairy Milk Silk","Birthday photo frame","Dora keychain","Teddy bear","Little buddha","Kitkat","Munch"]

price_dict = {"Dairy Milk Silk": 48,"Rose": 20,"Teddy bear": 92.75,"Birthday photo Frame": 250,"Little buddha": 50,"Dora keychain": 32.5,"Kitkat":30,"Munch":15}
category_map = {"Rose": "flower","Dairy Milk Silk": "choclate","Birthday photo frame": "frames","Dora keychain": "keychain","Teddy bear": "soft toys","Little buddha": "gifts under 100","Kitkat":"choclate","Munch":"choclate"}
catalog = []

for product in products:
    price = price_dict.get(product)
    category = category_map.get(product)
    catalog.append((product, price, category))

print("Catalog:",catalog)

#task4.2 - create dict{category:[list of products belonging to that category]}

category_to_products={}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("\nDictory mapping category with products are:",category_to_products)

#task4.3 - print products belonging to category with highest products
max_category = max(category_to_products, key=lambda c: len(category_to_products[c]))

print("\nCategory with max products:", max_category)
print("\nNumber of products:", max_count)
print("\nProducts list belongnging to max category are:",category_to_products[max_category])


# In[ ]:




