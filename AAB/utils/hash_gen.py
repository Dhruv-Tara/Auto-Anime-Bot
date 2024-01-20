# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara

alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
import random

def generate_hash(len : int) -> str :

    hash_string = ""

    for i in range(0,len) :
        
        hash_string += random.choice(alphabet_list)

    return hash_string


