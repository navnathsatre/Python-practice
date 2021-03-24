#!/usr/bin/env python
# coding: utf-8

# ### Tuples
# * Ordered Collection of items/elements
# * IMMUTABLE
# * Syntax : ( )

# In[1]:


players = ("Rohit", "Virat", "Rahane")


# In[2]:


print(players)


# In[3]:


type(players)


# #### To access any element, use [ ] - Square or Subscript Operator

# In[4]:


players[0]


# In[5]:


len(players)


# In[6]:


players[-1]


# In[7]:


players[:2]


# In[ ]:





# In[8]:


players.count("Virat")


# In[9]:


players.index("Virat")


# In[ ]:





# In[10]:


t = (100, [1, 2, 3], "March", 2021)


# In[11]:


t


# In[ ]:





# In[12]:


players


# In[13]:


players[0] = "Rohit Sharma"


# In[ ]:





# In[14]:


t


# In[15]:


t[1]


# In[16]:


t[1].append(4)


# In[17]:


t


# In[18]:


t[0] = "hundred"


# In[19]:


t[1] = "18"


# In[20]:


t[1].append(5)


# In[22]:


t


# In[ ]:





# In[ ]:





# ### =, Shallow Copy & Deep Copy

# In[88]:


team_a = ["Dhawan", "Rahane", "Ashwin"]


# In[89]:


team_b = team_a


# In[91]:


team_b


# In[92]:


id(team_a)


# In[93]:


id(team_b)


# In[94]:


team_a.append("Axar")


# In[95]:


team_a


# In[96]:


team_b


# In[97]:


team_b.append("Hardik")


# In[98]:


team_b


# In[99]:


team_a


# In[ ]:





# ### Shallow Copy
# * list
# * [:]
# * copy

# In[100]:


team_c = team_a[:]  ## Shallow Copy


# In[101]:


team_a


# In[102]:


team_b


# In[103]:


team_c


# In[104]:


id(team_a)


# In[105]:


id(team_b)


# In[106]:


id(team_c)


# In[ ]:





# In[109]:


team_a.append("Pant")


# In[110]:


team_a


# In[111]:


team_b


# In[112]:


team_c


# In[113]:


team_a


# In[114]:


id(team_a)


# In[115]:


id(team_b)


# In[116]:


id(team_c)


# In[117]:


team_a[0] = "Shikhar"


# In[118]:


team_a


# In[119]:


team_b


# In[120]:


team_c


# In[121]:


team_d = list(team_a)  ## Shallow Copy


# In[123]:


team_d


# In[130]:


id(team_a), id(team_b)


# In[128]:


id(team_c)


# In[129]:


id(team_d)


# In[131]:


team_a.append("Kuldeep")


# In[132]:


team_a


# In[133]:


team_b


# In[134]:


team_d


# In[ ]:





# In[136]:


team_e = team_a.copy() # Shallow Copy


# In[137]:


id(team_e)


# In[138]:


team_a


# In[139]:


team_e


# In[140]:


team_a.append("Jadeja")


# In[141]:


team_a


# In[144]:


team_b


# In[145]:


team_e


# In[ ]:





# In[146]:


list_1 = [100, [1, 2, 3], 200, 300]


# In[147]:


list_2 = list_1.copy()


# In[148]:


list_1


# In[150]:


list_2


# In[151]:


id(list_1)


# In[152]:


id(list_2)


# In[153]:


list_1.append(400)


# In[154]:


list_1


# In[155]:


list_2


# In[156]:


list_1[1]


# In[157]:


list_1[1].append(4)


# In[158]:


list_1


# In[159]:


list_2


# In[160]:


list_1[1].append(5)


# In[161]:


list_1


# In[162]:


list_2


# In[ ]:





# In[163]:


list_1[1] = "18Mar2021"


# In[164]:


list_1


# In[165]:


list_2


# In[ ]:





# ### Deep Copy

# In[166]:


import copy


# In[167]:


dc_1 = ['a', 'b', [100, 200, 300], 'c']


# In[168]:


dc_2 = copy.deepcopy(dc_1)


# In[169]:


dc_1


# In[170]:


dc_2


# In[171]:


dc_1.append('d')


# In[172]:


dc_1


# In[173]:


dc_2


# In[174]:


dc_1[2].append(400)


# In[175]:


dc_1


# In[176]:


dc_2


# In[ ]:





# In[ ]:





# In[180]:


v = "Virat", 31, "RCB" # Packing


# In[181]:


print(v)


# In[182]:


type(v)


# In[ ]:





# In[183]:


n, a, t = "Rohit", 33, "MI"


# In[184]:


n


# In[185]:


a


# In[186]:


t


# In[187]:


type(n)


# In[188]:


type(a)


# In[189]:


type(t)


# In[ ]:





# In[ ]:





# ### Practice Questions

# In[190]:


a,b,c=1,2,3


# In[191]:


a,b,c


# In[192]:


print(a,b,c)


# In[ ]:





# In[193]:


c = ["India", "USA", "Srilanka"]


# In[194]:


t_c = tuple(c)


# In[195]:


t_c


# In[196]:


lst_from_t = list(t_c)


# In[197]:


lst_from_t


# In[ ]:





# In[198]:


t = ()


# In[199]:


t


# In[200]:


type(t)


# In[ ]:





# In[201]:


t1 = ("18Mar2021")


# In[202]:


t1


# In[203]:


type(t1)


# In[ ]:





# In[204]:


t2 = ("18Mar",)


# In[205]:


t2


# In[206]:


type(t2)


# In[207]:


t2


# In[208]:


t2 * 5


# In[209]:


t2[1]


# In[210]:


t2


# In[211]:


len(t2)


# In[ ]:





# In[212]:


t3 = "OneElement",


# In[213]:


t3


# In[214]:


type(t3)


# In[ ]:




