# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara
# Using Anilist for anime info


import requests

url = "https://graphql.anilist.co"

anime_query = '''
   query ($search: String) { 
      Media (type: ANIME,search: $search) { 
        title {
          english
        }
          status
          coverImage{
          extraLarge
          }
      }
    }
'''




def anime(anime_name):
    

    variables = {'search': anime_name}
    
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    
    
    if json == None :
        
        return


    if json:
        
        return {
            "image" : json['data']["Media"]['coverImage']['extraLarge'],
            "name" : json['data']["Media"]["title"]["english"],
            "status" : json['data']["Media"]["status"]
        }
    

