# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:12:26 2022
Defines list of actions for use in Smash Trainer Py app
@author: TJ
"""

import time
import json
import random

def viewTechs(techs):
    for i in techs:
        print(i)

def delTechs(techs):
    name = input("Tech to delete? WARNING: THIS WILL RENDER PROGRESS ON THIS TECH LOST").strip()
    print(name)
    if name in techs:
        techs.pop(name)
        print("Done.")
        return
    print("No tech with that name.")
    
def addTech(techs):
    name = input("Name of tech? ").strip()
    print(name)
    cont = Layer()
    techs[name] = cont
    
  
def spacedRepetition(techs):
    a = []
    b = []
    for i in techs:
        a.append((techs[i]['score']))
        b.append(i)
    m = max(a)
    for i in range(len(a)):
        a[i] = (m-a[i])+1
    
    s = sum(a)
    pick = random.randint(0, s-1)
    i = 0
    while pick > 0 and i < len(a):
        pick -= a[i]
        i+=1
    return b[i-1]
    
def train(techs):
    l = [spacedRepetition(techs)]
    for i in range(9):
        s = spacedRepetition(techs)
        while s == l[-1]:
            s = spacedRepetition(techs)
        l.append(s)
    scrs = []
    for i in range(3):
        for j in range(len(l)):
            if i == 0:
                scrs.append(getScore(l[j]))
            else:
                scrs[j] += getScore(l[j])
    for j in range(len(scrs)):
        scrs[j] = int(scrs[j]/3)
    for j in range(len(scrs)):
        sc = techs[l[j]]["score"]
        sc = ((sc*10) + scrs[j])/11
        techs[l[j]]["score"] = sc
    return techs
    
            
def getScore(inp):
    s = "a"
    while not (s.isnumeric() and int(s)<11 and int(s)>0):
        s = input("%s: "%inp)
        print(s)
    return int(s)
       
def Layer():
    t = {"score" : 1}
    a = input("Add subparams? (y/n) ").strip()
    print(a)
    while a=="y":
        b = input("Subparam name: ").strip()
        newlist = []
        text = input("Subparam types: ('' to stop)").strip()
        print(text)
        while text!="":
            newlist.append(text)
            text = input().strip()
            print(text)
            
        newlist = tuple(newlist)
        t[b] = newlist
        print(t)
        a = input("Another subparam? (y/n) ").strip()
    return t
        

           
def Help():
    print("""Commands:
          '+' Add Exercise
          't' Train
          'v' View Exercises
          'e' Exit
          's' Save
          """)
def saveFile(techs):
    with open("techs.txt", "w") as outfile:
        outfile.write(json.dumps(techs))
        outfile.close()
        print("Done!!!!")

if __name__ == "__main__":
    fn = "techs.txt"
    techsf = open("techs.txt", "r")
    techs = json.load(techsf)
    techsf.close()
    
    
    
    while True:
        command = input("\nCommand ('h' for help): ").strip()
        print(command)
        print()
        match command:
            case "h":
                Help()
            case "+":
                addTech(techs)
            case "-":
                delTechs(techs) 
            case "v":
                viewTechs(techs)
            case "s":
                saveFile(techs)
            case"t":
                techs = train(techs)
                with open(fn, "w") as outfile:
                    outfile.write(json.dumps(techs))
                    outfile.close()
            case "e":
                break
        