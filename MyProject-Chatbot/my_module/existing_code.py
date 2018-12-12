"""A collection of functions copied from Assignment 3"""


import string
import random
import nltk
        
def is_question(input_string):
    
    """check if the user input is a string"""
    
    if '?' in input_string:
        output = True
        
    else:
        output = False
        
    return output 


def remove_punctuation(input_string):
    
    """remove any punctuation in the user input"""
    
    out_string = ""
    
    for item in input_string:
        
        if item not in string.punctuation: 
            out_string = out_string + item
            
    return out_string


def prepare_text(input_string):
    
    """makes every word in the user input lower case, remove any puncuation, and then split the sentences into a invidual strings of word"""
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string) 
    out_list = temp_string.split()
    
    return out_list


def respond_echo(input_string,number_of_echoes,spacer):
    
    """returns a string that has been repeated a specified number of times, with a given separator. """
    
    if input_string is not None:
        echo_output = (input_string + spacer)*number_of_echoes
        
    else:
        echo_output = None
        
    return echo_output  


def selector(input_list,check_list,return_list):
    
    """randomly selects an output for the chatbot, based on the input it got. """
    
    output = None
    
    for element in input_list:
        
        if element in check_list:
            output = random.choice(return_list)
            break
            
    return output


def string_concatenator(string1,string2,separator):
    
    """concatenates two strings, combining them with a specified separator. """
    
    output = string1 + separator + string2
    
    return output


def list_to_string(input_list,separator):
    
    """turns a list of strings back into one single concatenated string."""
    
    output = input_list[0]
    
    for item in input_list[1:]:
        output = string_concatenator(output,item,separator)  
        
    return output 


def end_chat(input_list):
    
    """ends the chat with our chatbot."""
    
    if 'quit' in input_list:
        return True
    
    else:
        return False
    
    
def is_in_list(list_one, list_two):
    
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        
        if element in list_two:
            return True
        
    return False


def find_in_list(list_one, list_two):
    
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        
        if element in list_two:
            return element
        
    return None