#!/usr/bin/env python
# coding: utf-8

# In[5]:


class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
        
    #insertion
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                
    #search
    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")
                
                
root=BST(10)
list1=[2,34,1,55,7,8]
for i in list1:
    root.insert(i)


# In[6]:


root.search(34)


# In[7]:


root.search(50)


# In[10]:


print(root.lchild.key)


# In[ ]:




