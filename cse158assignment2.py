
# coding: utf-8

# # CSE 158 Assignment 2 
# 
# Authors: Lucas Tindall and Kyle Smurlo
# 
# [Render notebook in browser](http://nbviewer.jupyter.org/github/ltindall/cse158_anime_recommender/blob/master/cse158assignment2.ipynb)
# (the plotly plots don't load in github)
# 
# Dataset: [Anime recommendations](https://www.kaggle.com/CooperUnion/anime-recommendations-database)
# 
# 

# ## Imports

# In[17]:

import csv
import random
from collections import defaultdict

import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

import plotly
plotly.tools.set_credentials_file(username='ltindall', api_key='KdrHKAMyc6KdVcSvPMdN')


# ## Get animes from csv

# In[51]:

animes = []
with open('anime.csv', 'rb') as file: 
    reader = csv.DictReader(file, delimiter=',')
    for row in reader: 
        animes.append(row)
        


# In[48]:

# get dictionary of lists of genre ratings 
genreRatings = defaultdict(list)

# for each anime 
for anime in animes: 
    # split all the genres listed for that review 
    for genre in anime['genre'].split(','): 
        # add rating to list for that genre
        if len(anime['rating']) > 0:
            genreRatings[genre.strip()].append(float(anime['rating']))

topGenres = []
for genre in sorted(genreRatings, key=lambda k: len(genreRatings[k]), reverse=True):
    topGenres.append((genre,genreRatings[genre]))


# ## Density plot of top 10 genre ratings 

# In[53]:

# Group data together
hist_data = [genre[1] for genre in topGenres[:10]]
#hist_data = [topGenres[0][1], topGenres[1][1], topGenres[2][1], topGenres[3][1]]

group_labels = [genre[0] for genre in topGenres[:10]]
#group_labels = [topGenres[0][0], topGenres[1][0], topGenres[2][0], topGenres[3][0]]

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)

# Plot!
py.iplot(fig, filename='Density plot of top genres')


# ## Get ratings from csv

# In[16]:

# shuffle ratings since original file is sorted by user id 
'''
with open('rating.csv', 'rb') as file: 
    reader = csv.reader(file)
    header, rows = next(reader), list(reader)
    random.shuffle(rows)
    
with open('ratings_shuffled.csv', 'wb') as file: 
    csv.writer(file).writerows([header] + rows)
'''     


# In[50]:

ratings = []
i = 0
with open('ratings_shuffled.csv', 'rb') as file: 
    reader = csv.DictReader(file, delimiter=',')
    for row in reader: 
        if i >= 2000000: 
            break
        ratings.append(row)
        i = i + 1
        

