#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Damilola Adekanmbi 
# DATE CREATED: 21/10/2021                               
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
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
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
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Creates list of files in directory
    # Retrieve the filenames from folder pet_images/
    in_files = listdir(image_dir)

    #Creates an empty list to store the petlabels
    pet_labels = []
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    for name in in_files:
        pet_name_list = name.lower().split('_')
        for idx, item in enumerate(pet_name_list):
            if item.isalpha() == 0:
                pet_name_list.pop(idx)
        label = ' '.join(pet_name_list)
        pet_labels.append(label)
        
        
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
        # If filename doesn't already exist in dictionary add it and it's
        # pet label - otherwise print an error message because indicates 
        # duplicate files (filenames)
        if (in_files[idx] not in results_dic) and (in_files[idx][0] != '.'):
            #sets pet_labels list index to the results_dictionary and adds it to results_dic.
             results_dic[in_files[idx]] = [pet_labels[idx]] 
        else:
             print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


if __name__ == "__main__": 
    from get_input_args import get_input_args
    