# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tweepy

api_key = 'nqBwLQNTSElUYQiq7SlU40lRQ'  # replace API KEY with your api key
api_secret = 'NTOZf5MMA2wkInhEUDJ1Gq40SmvCEUgtB0ycZmjXHaL3fmSsT0'  # replace API SECRET with your api secret
access_token = '167560960-gx9WSTsRjLTIhy9oLZrlrmIxxsbnrySSpYMMPJZ5'  # replace ACCESS TOKEN with your access token
access_token_secret = 'q52CkiSH2XIVdW6dDtTDTSthiJ7KoHPvO46pBDuBec7wz'  # replace ACCESS TOKEN SECRET with your access token secret

search_query = 'техника'
latitude = 55.621134  # latitude of the location
longitude =  38.086583  # longitude of the location
search_range = 30  # range in kilometers

search_area = '{0},{1},{2}km'.format(latitude, longitude, search_range)

authentication = tweepy.OAuthHandler(api_key, api_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication)
search = api.search(q=search_query, geocode=search_area)

for item in search:
    print(item.text)
