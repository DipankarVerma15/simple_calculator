#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b,


# In[3]:


dipu=True
while dipu:
    
    print('''
            1.add 
            2.subtract
            3.divide
            4.multiply
            5.to stop the calculator''')
    choose=input('choose between 1 to 5:')
    if choose in ('1','2','3','4'):
        if choose=='1':
            apple=0
            z=1
            while z!=0:
                print('type 0 to stop adding')
                z=int(input('enter the no you wanna add:'))
                apple+=z
                print(apple)
        elif choose=='2':
            print('type - to continue subtructing:')
            p='-'
            differ=0
            while p=='-':
                f=int(input('enter the no you want to enter:'))
                differ+=f
                p=input('enter the oppre')
                
            
            print(subtract(a,b))
        elif choose=='3':
            a=int(input('enter the first no:'))
            b=int(input('enter the second no:'))
            print(divide(a,b))
        elif choose=='4':
            a=int(input('enter the first no:'))
            b=int(input('enter the second no:'))
            print(multiply(a,b))
    else:
        dipu=False
        
            
    


# In[ ]:




