# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara


import requests
from lxml import etree
from AAB import LOG

url = "http://subsplease.org/rss"



def get_anime(hash : str,to_add : int) :

    response = requests.get(url)

    if response.status_code == 200:
        xml_data = response.text
        root = etree.fromstring(xml_data)
        items = root.xpath('//item')

        array = []

        for i in range(0,to_add):

            if hash == items[i].findtext('guid') :
                break

            else :
                
                try :
                    if array[-1]['name'] == items[i].findtext('category').split("-")[0] :

                        array[-1]['magnet'].append(items[i].findtext('link'))
                        array[-1]['hash'].append(items[i].findtext('guid'))
                        array[-1]['quality'].append(items[i].findtext('category').split("-")[-1])
                        array[-1]['title'].append(items[i].findtext('title'))

                    else :

                        array.append({
                            'name' : items[i].findtext('category').split("-")[0],
                            'magnet' : [items[i].findtext('link')],
                            'hash' :  [items[i].findtext('guid')],
                            'quality' : [items[i].findtext('category').split("-")[-1]],
                            'title' : [items[i].findtext('title')]
                        })
                
                except IndexError :
                    array.append({
                            'name' : items[i].findtext('category').split("-")[0],
                            'magnet' : [items[i].findtext('link')],
                            'hash' :  [items[i].findtext('guid')],
                            'quality' : [items[i].findtext('category').split("-")[-1]],
                            'title' : [items[i].findtext('title')]
                        })

        if len(array) == 0 :
            return None
        
        return {'array' : array,'hash' : array[0]['hash'][0]}

    else:
        LOG.error(f"Failed to fetch data. Status code: {response.status_code}")