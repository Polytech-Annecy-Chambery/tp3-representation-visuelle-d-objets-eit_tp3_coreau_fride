# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening
import copy

import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu

def Q1a():
    return Configuration()
    
def Q1b_f():
    return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}). \
        setParameter('xAxisColor', [1, 1, 0]). \
        setParameter('yAxisCo lor', [0,1,1]). \
        display()
        
        
def Q2b():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
            ) 

def Q2c():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True})
            )

def Q3a():
    #construction d'un mur
    return Configuration().add(
            Wall({'position': [1, 1, 0], 'width':7, 'height':2.6, 'orientation': 90})
            )

def Q4a():
    # Construction d'une maison de 4 murs, épaisseur (thickness) choisie par défaut
    wall1 = Wall({'position': [1, 1, 0], 'width':7, 'height':5, 'orientation': 0})
    wall2 = Wall({'position': [1, 1, 0], 'width':7, 'height':5, 'orientation': 90})
    wall3 = Wall({'position': [1, 1, 0], 'width':7, 'height':5, 'orientation': 90})
    wall4 = Wall({'position': [1, 1, 0], 'width':7, 'height':5, 'orientation': 0})  
    house = House({'position': [-3, 1, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    return Configuration().add(house)   
    
def Q5a():  
    # Ecriture avec mélange de variable et de chaînage    
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
    return Configuration().add(opening1).add(opening2)
    
def Q5b():  
    # Ecriture avec mélange de variable et de chaînage   
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    print(section.canCreateOpening(opening1))
    print(section.canCreateOpening(opening2))    
    print(section.canCreateOpening(opening3))
    return Configuration()    
    
def Q5c1(): 
    #creation d'une ouverture de porte     
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    sections = section.createOpening(opening1)
    configuration = Configuration()
    for x in sections:
        configuration.add(x)    
    return configuration     
    
def Q5c2():  
#creation d'une ouverture de fenêtre    
    section = Section({'width':7, 'height':2.6})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    sections = section.createNewSections(opening2)
    configuration = Configuration()
    for section in sections:
        configuration.add(section)    
    return configuration    

def Q5d():      
    wall = Wall({'width':7, 'height':2.6,})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    section = wall.findSection(opening1)
    print(section)
    
def Q6():  
    pass  
 
def main():
    # Enlever un des commentaires pour la question traitée
    
    #configuration = Q1a()
    #configuration = Q1b_f()
    #configuration = Q2b()
    # configuration = Q2c()
    #configuration = Q3a()
    #configuration = Q4a()
    # configuration = Q5a()
    # configuration = Q5b()
    # configuration = Q5c1()
    # configuration = Q5c2() 
    configuration = Q5d()
    # configuration = Q6()
    configuration.display()     
         
# Calls the main function
if __name__ == "__main__":
    main()    
