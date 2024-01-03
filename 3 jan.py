#!/usr/bin/env python
# coding: utf-8

# In[1]:


# polymorphism( define methods in the child class that have the same name as the methods in the parent class.)
#overriding(parent and child class can have same name,same method,same parameters)
class animal:
    def speak(self):
        print("the animal make sound")
        
class Dog(animal):
    def speak(self):
        print('the dog barks')
        
class cat(animal):
    def speak(self):
        print('the cat meows')
        


# In[3]:


a=animal()
a.speak()
a=Dog()
a.speak()
a=cat()
a.speak()


# In[4]:


#method overloading(parent and child class have same name,same method but different parameters)
class test:
    def add(self,a,b,c=0):
        self.a=a
        self.b=b
        self.c=c
        return self.a+self.b+self.c
    


# In[7]:


obj=test()
obj.add(45,89)


# In[8]:


obj.add(4,5,6)


# In[11]:


class subject:
    def marks(self):
        self.s1=int(input("enter 1st subject marks:"))
        self.s2=int(input("enter 2nd subject marks:"))
        self.s3=int(input("enter 3rd subject marks:"))
        self.s4=int(input("enter 4th subject marks:"))
        self.s5=int(input("enter 5th subject marks:"))
    def disp_marks(self):
        print("subject 1:",self.s1)
        print("subject 2:",self.s2)
        print("subject 3:",self.s3)
        print("subject 4:",self.s4)
        print("subject 5:",self.s5)


# In[12]:


class result(subject):
    def total(self):
        self.total_marks=self.s1+self.s2+self.s3+self.s4+self.s5
    def percent(self):
        self.percent_marks=(self.total_marks/500)*100
    def disp_result(self):
        print("total:",self.total_marks)
        print("percent :",self.percent_marks)
        if(self.percent_marks>=85):
            print("distinction")
        elif(self.percent_marks<85 and self.percent_marks>=60):
            print("first class")
        elif(self.percent_marks<60 and self.percent_marks>=50):
            print("second class")
        elif(self.percent_marks<50 and self.percent_marks>=40):
            print("pass class")
        else:
            print("fail")


# In[13]:


result.obj=result()
result.obj.marks()
result.obj.total()
result.obj.percent()
result.obj.disp_marks()
result.obj.disp_result()





# In[ ]:




