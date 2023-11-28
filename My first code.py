#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")
#Python Crash Course Ch. 1-3


# In[2]:


message = "Hello Python World"
print(message)


# In[34]:


message = "Hello Python World"
print(message)
message= "Hello Python Crash Course World"
print(message)


# In[5]:


message = "Hello Python World"
print(mesage)
#error Example


# In[6]:


name= "ada lovelace"
print(name.title())


# In[7]:


name= "ada lovelace"
print(name.lower())
print(name.upper())


# In[8]:


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


# In[14]:


print("Languages:\n\tPython\n\tC\n\tJavaScript")


# In[26]:


print('"Hey Mate, There is a large critter in that water."')


# In[28]:


2+5


# In[30]:


3*3


# In[31]:


3**3


# In[57]:


(2+3)*4


# In[33]:


2+3*4


# In[36]:


import this


# In[41]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


# In[43]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])


# In[44]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])


# In[46]:


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


# In[48]:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# In[49]:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


# In[50]:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)


# In[56]:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# In[60]:


motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


# In[62]:


motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# In[64]:


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


# In[65]:


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# In[144]:


guests = ['roosvelt', 'teddy', 'ford', 'eisenhower']
print(guests)

guests.insert(0, 'bush')
guests.insert(3, 'washington')
guests.append('lincoln')
new_guests = [x.capitalize() for x in guests]
print(new_guests)
#my first big "oh that's how it works!"


# In[150]:


cars =['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# In[151]:


cars =['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


# In[155]:


cars =['bmw', 'audi', 'toyota', 'subaru']

print("Here is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
 
print("\nHere is the orginal list again:")
print(cars)


# In[156]:


cars =['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# In[157]:


cars =['bmw', 'audi', 'toyota', 'subaru']
len(cars)


# In[37]:


meat =['beef', 'lamb', 'chicken','pork']
print(meat)

print(sorted(meat))

print(meat)

meat.reverse()
print(sorted(meat))

meat.sort(reverse=True)
print(meat)


print(sorted(meat))

print(sorted(meat))

print(meat)


# In[39]:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])






