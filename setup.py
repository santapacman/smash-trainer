# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:00:29 2022
Sets up tech file
@author: TJ
"""
import json
techs = {
    "Jump": {
        "score": 1,
        0: ("Full hop", "Short Hop"),
        "units": (0, .5, 1, 1.5, 2, 2.5, "far"),
        "fall": ("Normal", "Fast"),
        "facing": ("Forward", "Turnaround"),
        },
    "Rapid Turnaround": {
        "score": 1
        },
    "Running Aerial":{
        "score": 1,
        "backCat": ("Jump"),
        "ignore": ("units"),
        "air": ("Neutral", "Forward", "Up", "Back", "Down")
        }
    
    }


try:
    outfile = open("techs.txt")
    outfile.close()
except FileNotFoundError:
    with open("techs.txt", "x") as outfile:
        outfile.write(json.dumps(techs))
        outfile.close()
        

