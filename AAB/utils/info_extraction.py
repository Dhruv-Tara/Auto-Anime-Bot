# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara

import re

def extract_info(input_string):

    pattern = r"\[SubsPlease\] (.+?)(?: S(\d+))? - (\d+)(?: \((\d+p)\) \[.+?\])?"

    match = re.match(pattern, input_string)

    if match:
        
        title = match.group(1)
        season = match.group(2)
        episode = match.group(3)
        quality = match.group(4)


        if episode and season:
            result = f"{title} Season {season} Episode {episode}"
        elif episode:
            result = f"{title}"
        elif season:
            result = f"{title} Season {season}"
        else:
            result = title

        if not season :

            return {"main_res" : result,"search_que" : title,'episode' : episode}
        else :
            return {"main_res" : result,"search_que" : f"{title} Season {season}",'episode' : episode}
        
    else:

        return "No match found."
    
