
# coding: utf-8

# # People in Space Indicator

# Once again we're going to borrow someone's code who has already written functions `get()` and `json()` to get the information that we need.  This is in the `requests` module

# In[3]:

import requests


# Now let's get the data.  It can be found on the website: http://api.open-notify.org/astros.json. Let's take a look:
# 
# <img src="https://www.raspberrypi.org/learning/people-in-space-indicator/images/people-in-space-api-screenshot.png"></img>

# In[4]:

url = "TYPE THE URL HERE"

r = requests.get(url)
r.ok


# ## How many people are in space?

# In[5]:

j = r.json()
j['PUT OBJECT NAME HERE']


# ## `for` loops
# 
# In python you can create loops to repeat a set of steps. In this code we are going to use a `for` loop.  Let's see if we can create a countdown.

# In[6]:

for i in [5,4,3,2,1]:
    print i
print "Blast-off!"


# ## Now use the `for` loop to print all their names

# In[7]:

for i in j['people']:
    print i['TYPE THE OBJECT TO GET NAMES HERE']

