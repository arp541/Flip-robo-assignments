#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# 1) Write a python program to display all the header tags from wikipedia.org.
# 

# In[3]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[4]:


soup = BeautifulSoup(page.content)
soup


# In[7]:


Allheaders = soup.find ('span', class_='mw-headline')
Allheaders.text


# In[8]:


Allheaders = []
for i in soup.find_all('span', class_='mw-headline'):
    Allheaders.append(i.text)
Allheaders    


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[11]:


page = requests.get ('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page

soup = BeautifulSoup(page.content)
soup


# In[16]:


name = soup.find ('h3', class_='lister-item-header').text.replace("\n","")
name


# In[29]:


#name
name = []
for i in soup.find_all('h3', class_='lister-item-header'):
    name.append(i.text.replace("\n",""))
name


# In[64]:


#rating
rating = soup.find_all("div", class_="inline-block ratings-imdb-rating")
rating


# In[65]:


#rating
rating = []
for i in soup.find_all("div", class_="inline-block ratings-imdb-rating"):
    rating.append(i.text.replace("\n",""))
rating
     


# yearofrelease

# In[67]:


yearofrelease = []
for i in soup.find_all("span", class_="lister-item-year text-muted unbold"):
    yearofrelease.append(i.text.replace("\n",""))
yearofrelease


# In[ ]:


data frame


# In[68]:


import pandas as pd


# In[71]:


df = pd.DataFrame({'Names':name, 'Ratings':rating, 'Yearofrelease':yearofrelease})
df


# Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.
# 

# In[72]:


page = requests.get ('https://www.imdb.com/list/ls009997493/?sort=user_rating,desc&st_dt=&mode=simple&page=1&ref_=ttls_vw_smp')
page

soup = BeautifulSoup(page.content)
soup


# In[82]:


name = soup.find ('div', class_='col-title')
name


# In[80]:


name = []
for i in soup.find_all('div', class_='col-title'):
    name.append(i.text.replace("\n",""))
name


# In[87]:


rating = soup.find("div", class_="col-imdb-rating")
rating


# In[91]:


rating = []
for i in soup.find_all("div", class_="col-imdb-rating"):
    rating.append(i.text.replace("\n","").strip("     "))
rating


# yearofrelease 

# In[92]:


yearofrelease = []
for i in soup.find_all("span", class_="lister-item-year text-muted unbold"):
    yearofrelease.append(i.text.replace("\n",""))
yearofrelease


# Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm

# In[101]:


page = requests.get ('https://presidentofindia.nic.in/former-presidents.htm')
page

soup = BeautifulSoup(page.content)
soup


# In[121]:


name = soup.find ('div', class_='presidentListing')
name.text


# In[120]:


#name

name = []
for i in soup.find_all('div', class_='presidentListing'):
    name.append(i.text.replace("\n",""))
name


# In[151]:


#Term of office
termofoffice = soup.find_all('div', class_='presidentListing')
termofoffice


# In[156]:


#termofoffice
termofoffice = []
for i in soup.find_all('div', class_='presidentListing'):
    termofoffice.append(i.text.replace("\n",""))
termofoffice


# In[184]:


page = requests.get ('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page

soup = BeautifulSoup(page.content)
soup


# In[199]:


TOP10ODIteams = soup.find('span', class_='u-show-phablet')
TOP10ODIteams


# In[196]:


TOP10ODIteams = []
for i in soup.find_all('span', class_='u-show-phablet'):
    TOP10ODIteams.append(i.text.replace("\n",""))
TOP10ODIteams[1:10]


# In[198]:


MatchesandPoints= soup.find('td', class_='table-body__cell u-center-text')
Matches


# In[204]:


MatchesandPoints = []
for i in soup.find_all('td', class_='table-body__cell u-center-text'):
    Matches.append(i.text.replace("\n",""))
Matches[0:10]


# In[205]:


ratings = soup.find('td', class_='table-body__cell u-text-right rating')
ratings


# In[206]:


ratings = []
for i in soup.find_all('td', class_='table-body__cell u-text-right rating'):
    ratings.append(i.text.replace("\n",""))
ratings[0:10]


# b) Top 10 men’s ODI Batting players along with the records of their team and rating.
# 

# In[207]:


page = requests.get ('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page

soup = BeautifulSoup(page.content)
soup


# In[216]:


#b) Top 10 ODI Batsmen along with the records of their team and rating.

Top10 = soup.find('tr', class_='table-body')
Top10.text


# In[215]:


Top10 = []
for i in soup.find_all('tr', class_='table-body'):
    Top10.append(i.text.replace("\n",""))
Top10[0:9]


# In[224]:


#c) Top 10 ODI bowlers along with the records of their team and rating.
Top10 = []
for i in soup.find_all('tr', class_='table-body'):
    Top10.append(i.text.replace("\n",""))
Top10[9:18]


# In[244]:


# Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
page = requests.get ('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page

soup = BeautifulSoup(page.content)
soup

TOP10ODIteams = []
for i in soup.find_all('tr', class_='table-body'):
    TOP10ODIteams.append(i.text.replace("\n"," "))
TOP10ODIteams[0:10]


# In[245]:


page = requests.get ('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
page

soup = BeautifulSoup(page.content)
soup


# In[250]:


#b) Top 10 women’s ODI Batting players along with the records of their team and rating.

Top10 = []
for i in soup.find_all('tr', class_='table-body'):
    Top10.append(i.text.replace("\n",""))
Top10 [0:9]


# In[251]:


#c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
Top10 = []
for i in soup.find_all('tr', class_='table-body'):
    Top10.append(i.text.replace("\n",""))
Top10 [18:30]


# In[252]:


#7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :

page = requests.get ('https://www.cnbc.com/world/?region=world')
page

soup = BeautifulSoup(page.content)
soup


# In[258]:


#Headline
Headline = soup.find('div', class_='FeaturedCard-content')
Headline.text


# In[260]:


#Time
Time = []
for i in soup.find_all('span', class_='LatestNews-wrapper'):
    Time.append(i.text.replace("\n",""))
Time


# In[265]:


#News
News = []
for i in soup.find_all('li', class_='LatestNews-item'):
    News.append(i.text.replace("\n"," "))
News


# In[ ]:


# Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details :
i) Paper Title
ii) Authors
iii) Published Date
iv) Paper URL 


# In[266]:


page = requests.get ('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page

soup = BeautifulSoup(page.content)
soup


# In[273]:


#i) Paper Title
PaperTitle = []
for i in soup.find_all('h2', class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg'):
    PaperTitle.append(i.text.replace("\n"," "))
PaperTitle


# In[274]:


#Authors
Authors = []
for i in soup.find_all('span', class_='sc-1w3fpd7-0 dnCnAO'):
    Authors.append(i.text.replace("\n"," "))
Authors


# In[275]:


#iii) PublishedDate
PublishedDate = []
for i in soup.find_all('span', class_='sc-1thf9ly-2 dvggWt'):
    PublishedDate.append(i.text.replace("\n"," "))
PublishedDate


# In[277]:


#iv) PaperURL 
PaperURL = []
for i in soup.find_all('a', class_='sc-5smygv-0 fIXTHm'):
    PaperURL.append(i.get('href'))
PaperURL


# In[ ]:


#9) Write a python program to scrape mentioned details from dineout.co.in :
i) Restaurant name
ii) Cuisine
iii) Location
iv) Ratings
v) Image URL


# In[285]:


page = requests.get ('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page

soup = BeautifulSoup(page.content)
soup


# In[286]:


#i) Restaurantname
Restaurantname = []
for i in soup.find_all('a', class_='restnt-name ellipsis'):
    Restaurantname.append(i.text)
Restaurantname


# In[291]:


#ii) Cuisine
Cuisine = []
for i in soup.find_all('span', class_='double-line-ellipsis'):
    Cuisine.append(i.text.split('|')[1])
Cuisine


# In[293]:


#iii) Location 
Location = []
for i in soup.find_all('div', class_='restnt-loc ellipsis'):
    Location.append(i.text)
Location


# In[295]:


#Ratings
Ratings = []
for i in soup.find_all('div', class_='restnt-rating rating-4'):
    Ratings.append(i.text)
Ratings


# In[296]:


#v) Image URL
imageURL = []
for i in soup.find_all('img', class_='no-img'):
    imageURL.append(i.get('data-src'))
imageURL


# In[ ]:


10) Write a python program to scrape the details of top publications from Google Scholar from
https://scholar.google.com/citations?view_op=top_venues&hl=en
i) Rank
ii) Publication
iii) h5-index
 iv) h5-median


# In[342]:


page = requests.get ('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page

soup = BeautifulSoup(page.content)
soup


# In[348]:


#Rank
rank = []
for i in soup.find_all("th", class_="gsc_mvt_p"):
    rank.append(i.text.replace("\n",""))
rank


# In[349]:


#Publication
Publication = []
for i in soup.find_all('tr', class_='gsc_mvt_t'):
    Publication.append(i.text)
Publication


# In[350]:


#iii) h5-index
h5index = []
for i in soup.find_all('tr', class_='gsc_mvt_n'):
    h5index.append(i.text.replace("\n"," "))
h5index


# In[365]:


# iv) h5-median
h5median = []
for i in soup.find_all('a', class_='gsc_mvt_n'):
    h5median.append(i.text)
h5median


# In[ ]:




