
#####################
#####==IMPORTS==#####
#####################

import os
import numpy as np
#from psychopy import core, visual, event, data, logging
from numpy.random import shuffle, randint, choice 
import string
from operator import itemgetter

def instImport(path):
    """
    instImport is a function for importing instruction text to be used in the experiment and does the required processing
        required inputs:
                        path: path of input file (as .txt)
        outputs: 
                        Variable with processed data as a list

    """
    # probably also write checks that the path points to a .txt and the outputName is a string

    with open(path, 'r') as f: #open file as object 
        processed_text = f.readlines()
    return processed_text

def equationMaker(congruency=None, beat_type=None, structure=None, n=None, perms=None, catch = False):
    """
    Function to create equation stimuli, like in Landy & Goldstone, e.g. "b + d * f + y"
        required inputs:
                        congruency: 'congruent' or 'incongruent'
                        beat_type : 'binary_beat' or 'ternary_beat'
                        structure : '+*+' or '*+*'
                        n         : how many equations to generate
        outputs: 
                        a list of trial dictionaries of the length specified by n

    """
    output_list = []
    alphabet = list(string.ascii_lowercase)
    letters_to_remove = ['i', 'l', 'o'] # because of similarity with other symbols
    alphabet = [letter for letter in alphabet if letter not in letters_to_remove] # final letter list

    op = list(structure) # list of operands
    #op = [x if x != "*" else "times" for x in op] # use this line for experimenting with speech stims

    eq_per_perm = int(n / len(perms)) # number of equations per permutation
    #assert eq_per_perm.is_integer(), "length of perms must be evenly divisble into n"
    
    perms = perms * eq_per_perm
    shuffle(perms)

    for eq in range(n):
        l = list(choice(alphabet, size=5, replace=False))
        equation = [l[0],op[0],l[1],op[1],l[2],op[2],l[3]] 
        
        p = itemgetter(*perms[eq][0])(l) # creates permutation of letter ordering for this iteration
        probe = [p[0],op[0],p[1],op[1],p[2],op[2],p[3]] 
        if catch:
            cat_idx = 2 * randint(0,3) # chooses one of the 4 letter indices
            probe[cat_idx] = l[4] # replace with other random letter not in stimulus
            trial_type = 'catch'
        else:
            trial_type = 'main'
        probe = ' '.join(probe)

        # add info on 'validity' and 'sensitivity' based on permutation used
        if perms[eq][1] <= 4:
            sensitivity = 'insensitive'
        else:
            sensitivity = 'sensitive'
        
        if structure == '+*+':
            if ( (perms[eq][1] <= 2) or (5 <= perms[eq][1] <= 6) ):
                validity = 'True'
            else:
                validity = 'False'
        elif structure == '*+*':
            if ( (perms[eq][1] <= 2) or (7 <= perms[eq][1] <= 8) ):
                validity = 'True'
            else:
                validity = 'False'
        elif structure == '+++':
            sensitivity = 'neutral'
            if catch:
                validity = 'False'
            else:
                validity = 'True'

        # assemble trial dictionary
        trial_dict = {'stim':equation, 'beat_type':beat_type, 
                    'congruency':congruency, 'structure': structure, 'stim_number': eq + 1, 'probe': probe,
                     'validity': validity, 'sensitivity': sensitivity, 'trial_type':trial_type}
        output_list.append(trial_dict)

    return output_list

def customHanning(M, floor):
    """ 
    this is a function to create a custom hanning window with a non-zero floor, specified by the variable 'floor'
    for example M = 0.2 means creating a hanning window with values between .2 and 1
    """
    a = 0.5 + 0.5*floor
    b = 0.5 - 0.5*floor
    M = int(M)
    custom_hanning_window = [a - b*np.cos(2 * x * np.pi /(M-1)) for x in range(M)]

    return custom_hanning_window

def check_lists_same_len(list_of_lists, message):
    it = iter(list_of_lists)
    the_len = len(next(it))
    if not all(len(l) == the_len for l in it):
        raise ValueError(message)
    return None

def trialCreator(condition_list, num_to_keep=None):
    ##### check same num of sentences for 1. sentences, and 2. probes #####
    #check_lists_same_len(condition_list, 'Not all conditions have same number of sentences!') 
    #check_lists_same_len(probe_condition_list, 'Not all conditions have the same number of probes!')
    all_trials = []
    for i in condition_list:
        all_trials += i

    shuffle(all_trials)

    if num_to_keep:
        all_trials = all_trials[:num_to_keep]

    for idx, trial in enumerate(all_trials):
        trial['stim_number'] = idx + 1


    return all_trials
