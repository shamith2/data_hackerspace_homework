#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
#

import json
import csv
import numpy as np


def histogram_times(filename):
    list1 = []
    list2 = []
    with open(filename) as f1:
        csv_read = csv.reader(f1)
        airplane_data = list(csv_read)
        for i in range(1,len(airplane_data)):
            if airplane_data[i][1][:2] != "":
                if (airplane_data[i][1][:2] > "00" or airplane_data[i][1][:2] == "00") and (airplane_data[i][1][:2] < "24" or airplane_data[i][1][:2] == "24") and airplane_data[i][1][:2] != "1:" :
                      list2.append(int(airplane_data[i][1][:2]))
        
        for m in range(0,24):
          c = list2.count(m)
          list1.append(c)
          
        return list1
    

    

def weigh_pokemons(filename, weight):
    flist = []
    with open(filename) as f2:
        pokemon_data = json.load(f2)
    for i in range(0,len(pokemon_data["pokemon"])):
        if pokemon_data["pokemon"][i]["weight"] == weight:
          flist.append(pokemon_data["pokemon"][i]["name"])
    if flist != []:
        print(flist)
    else:
        return []
            
        

def single_type_candy_count(filename):
    total = 0
    with open(filename) as f3:
        pokemon_data = json.load(f3)
    for i in pokemon_data["pokemon"]:
        if "type" in i:
            if len(i["type"]) == 1:
               if "candy_count" in i:
                    total += i["candy_count"]
    return total

def reflections_and_projections(points):
    points_matrix = np.array(points)
    
    reflection_matrix = np.array([[1,0],[0,-1]])
    reflection = np.dot(reflection_matrix,points_matrix)
    reflection[1,:] = reflection[1,:] + 2
    return reflection
    
    trig_matrix = np.array([[0,-1],[1,0]])
    rotation = np.dot(trig_matrix,points_matrix)
    return rotation
    
    projection_matrix = np.array([[1,3],[3,9]])
    projection = np.dot(projection_matrix,points_matrix)/10
    return projection

def normalize(image):
    image_matrix = np.array(image)
    max = np.amax(image_matrix)
    min = np.amin(image_matrix)
    new_image_matrix = ((image_matrix-min)*255)/(max-min)
    return new_image_matrix
    

def sigmoid_normalize(image, a):
    image_mat = np.array(image)
    new_img_mat = 1/(255*(1 + np.exp((-1/a)*(image_mat))))
    return new_img_mat
