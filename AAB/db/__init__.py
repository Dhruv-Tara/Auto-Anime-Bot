# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from AAB import Vars,LOG

mongo_client = MongoClient(Vars["database_url"],server_api=ServerApi('1'))
database = mongo_client.get_database('AAB')
last_added = database.get_collection('last_added')
new_db = database.get_collection('new_db')
remain = database.get_collection('remain')
worker = database.get_collection('worker')
files = database.get_collection('files')


def get_last_hash() :
    data = last_added.find_one({'_id':1})
    
    if data == None :
        return None
    return data['hash']


def add_hash(hash) :

    last_hash = get_last_hash()

    if last_hash == None :

        last_added.insert_one({"_id" : 1,'hash' : hash})
        return
    
    else :
        last_added.update_one({'_id' : 1},{"$set" : {'hash' : hash}},upsert= True)
        return
    


def is_new_db() :
    data = new_db.find_one({'_id' : 1})

    if data == None :
        new_db.insert_one({'_id' : 1})
        return True
    
    else :
        return False
    


def add_remain_amime(remaining : list) :

    remain_data = remain.find_one({'_id' : 1})
    
    if remain_data == None :

        remain.insert_one({'_id' : 1, 'list' : remaining})
        return
    else :

        main_list = remain_data['list']
        for i in remaining :
            main_list.append(i)

        remain.update_one({'_id' : 1},{'$set' : {'list' : main_list}},upsert= True)
        return
    


def get_remain_anime() -> list :

    doc = remain.find_one({'_id' : 1})
    return doc['list']


def update_remain_anime(list_of_anime : list) -> None :

    remain.update_one({"_id" : 1},{"$set" : {'list' : list_of_anime}},upsert= True)
    return





def is_working() -> bool :

    doc = worker.find_one({'_id' : 1})

    if doc == None :

        worker.insert_one({'_id' : 1, 'working' : False})
        return False

    else :
        return doc['working']


def update_worker(param : bool) -> None :

    is_working()

    worker.update_one({'_id' : 1},{"$set" : {'working' : param}},upsert= True)
    return



def add_file(name : str,hash : str, message_id : int)-> None :
    
    check = files.find_one({"_id" : 1})

    if check == None :
        files.insert_one({"_id" : 1})
        files.insert_one({"name" : name,'hash' : hash,"message_id" : message_id})
        return
    else :
        files.insert_one({"name" : name,'hash' : hash,"message_id" : message_id})
        return


def get_file_by_hash(hash : str) -> [None,dict] :

    doc = files.find_one({"hash" : hash})
    
    if doc == None :
        return None
    
    else :
        return doc


def rev_and_del(lst : list) -> list :

    try :

        lst.reverse()
        lst.pop()
        lst.reverse()
        return lst
    except Exception :
        return
    

def remove_anime_from_remain()-> None :

    data = get_remain_anime()

    if len(data[0]['quality']) >= 1 :

        try :

            new_list = rev_and_del(data)
            update_remain_anime(new_list)

        except Exception :
            pass
        return
    
    else :

        main_dict = data[0]
        name = main_dict['name']

        magnet = main_dict['magnet']
        hash_ = main_dict['hash']
        quality = main_dict['quality']
        title = main_dict['title']

        try :

            new_mag = rev_and_del(magnet)
            new_hash = rev_and_del(hash_)
            new_quality = rev_and_del(quality)
            new_title = rev_and_del(title)

            new_data = rev_and_del(data)

            new_data.reverse()
            new_data.append({
                            'name' : name,
                            'magnet' : new_mag,
                            'hash' : new_hash,
                            'quality' : new_quality,
                            'title' : new_title
                        })
            new_data.reverse()

            update_remain_anime(new_data)

            return
        
        except Exception as eor :
            
            LOG.error(eor)


# End of DataBase file