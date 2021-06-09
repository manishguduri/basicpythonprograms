#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Eligible to vote

age=int(input())
if(age>=0):
 if(age>=18):
    print("Eligible to vote")
 elif(age>=0 and age<18):
    print("Not Eligible to vote")
else:
    print("Wrong input")
    


# In[2]:


#positive or negative

num=int(input())
if(num>0):
    print(num,"is Positive")
elif(num==0):
    print(num,"is zero")
else:
    print(num,"is negative")


# In[3]:


#Even and divisible by 4 or not

num=int(input())
if(num%2==0):
    if(num%4==0):
        print(num,"is even and divisible by 4")
    else:
        print(num,"is even but not divisible by 4")
else:
    print(num,"is odd number")
    


# In[4]:


#Grade with percentage

per=float(input())
if(per>=90):
    print("Distinction")
elif(per>=50):
    print("Pass")
else:
    print("Fail")


# In[1]:


#Leap year or not 

year=int(input())
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year," is leap a year")
        else:
            print(year," is not a leap year")
    else:
        print(year," is a leap year")
else:
    print(year," is not a leap year")
    


# In[ ]:




