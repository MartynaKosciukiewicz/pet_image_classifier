#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Martyna Kosciukiewicz
# DATE CREATED: 1/03/2021                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
##

# Imports python modules
from os import listdir

filename_list = listdir("pet_images/")

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
     
    #Create empty dictionary named results_dic
    results_dic = dict()

    #Determine number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    pet_labels = [] #create an empty pet_labels list

    #Loop to construct pet_name list
    for idx in range(0, len(filename_list), 1): 
        filename = filename_list[idx] #getting the filename from the list at that index
        filename_lower = filename.lower() #converting the filename to lowercase
        pet_label_list = filename_lower.split("_") #split the filename into a list of words at underscore
        pet_label = "" #initialize variable
        for word in pet_label_list: #loop to check if name is alpha characters only
            if word.isalpha():
                pet_label += word + " " #if it is, add word to pet_label
        pet_label = pet_label.strip() #Strip off starting/trailing whitespace characters 
        pet_labels.append(pet_label) #add pet_label to pet_labels list

    # Loop to construct results_dict with filenames and pet labels
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx] not in results_dic:
             results_dic[filename_list[idx]] = [pet_labels[idx]]
        else:
             print("** Warning: Key=", filename_list[idx], 
                   "already exists in results_dic with value =", 
                   results_dic[filename_list[idx]])

    #Iterating through a dictionary printing all keys & their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename =", key, "   Pet Label =", results_dic[key][0])

    # Replace None with results_dic dictionary that you created with this function
    return results_dic
