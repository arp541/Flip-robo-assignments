#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# #3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[4]:


#send get request to the webpage server to get the source code of the page
page = requests.get ('https://www.imdb.com/list/ls009997493/?sort=user_rating,desc&st_dt=&mode=simple&page=1&ref_=ttls_vw_smp')
page

soup = BeautifulSoup(page.content)
soup


# In[6]:


#Scarping movie name
name = soup.find ('div', class_='col-title')
name

name = []
for i in soup.find_all('div', class_='col-title'):
    name.append(i.text.replace("\n",""))
name


# In[7]:


#scraping rating
rating = soup.find("div", class_="col-imdb-rating")
rating


# In[8]:


rating = []
for i in soup.find_all("div", class_="col-imdb-rating"):
    rating.append(i.text.replace("\n","").strip("     "))
rating


# In[9]:


#scraping yearofrelease
yearofrelease = []
for i in soup.find_all("span", class_="lister-item-year text-muted unbold"):
    yearofrelease.append(i.text.replace("\n",""))
yearofrelease


# In[11]:


ds = pd.DataFrame({'Name':name, 'Rating':rating, 'Year_ofrelease':yearofrelease})
ds


# In[ ]:




