#!/Users/Stilts/PsychoPyBuild/bin/python 
# -*- coding: utf-8 -*-

#####################
#####==IMPORTS==#####
#####################

import csv, os
import customFunctions as fun # my own function for preprocessing the text
from random import shuffle

#############################
#####==BASIC VARIABLES==#####
#############################

FGC = (1, 1, 1) #white
BGC = (0, 0, 0) #grey
TEXTSIZE = 62 #text size for stim (not instructions)
TEXTCORDS = (0, 0) #Centre of screen
beat_freq = .4 #1/3  #0.417 #2.4Hz
frameInterval = 0.0166667 #framerate.... CHECK THIS
sound_delay = .08 # 0.003 for processing command + .102 for soundcard/driver processing and sound coming out of earphones
trial_duration = 10 # seconds
probe_duration = 5 # seconds

trials_per_condition = 24

assort_trials = 8

_thisDir = os.path.abspath(os.path.dirname(__file__)) #change to local directory
os.chdir(_thisDir)

#####################
#####==STIMULI==#####
#####################

# defining the permutations to be used for the stimuli probes
permutations = [((0,1,2,3),1), 
         ((3,2,1,0), 2),
         ((1,2,0,3), 3),
         ((2,0,3,1), 4),
         ((0,2,1,3), 5),
         ((3,1,2,0), 6),
         ((2,3,0,1), 7),
         ((1,0,3,2), 8)]

###===INSTRUCTIONS===###
part1Intro = fun.instImport('Stimuli/Instructions/Part1.txt')
#part2Intro = fun.instImport('Stimuli/Instructions/Part2.txt')
#part3Intro = fun.instImport('Stimuli/Instructions/Part3.txt')
bottom_text = fun.instImport('Stimuli/Instructions/bottom_text.txt')

###===STIMULI===###
# '+ * +' trials
ptp_cong = fun.equationMaker('congruent', 'binary', '+*+',trials_per_condition, permutations)
ptp_incong = fun.equationMaker('incongruent', 'binary', '+*+',trials_per_condition, permutations)
ptp_cong2 = fun.equationMaker('congruent', 'binary2', '+*+',trials_per_condition, permutations)
ptp_incong2 = fun.equationMaker('incongruent', 'binary2', '+*+',trials_per_condition, permutations)
ptp_neut = fun.equationMaker('neutral', 'nonaccent', '+*+',trials_per_condition, permutations)

# '* + *' trials
tpt_cong = fun.equationMaker('congruent', 'binary', '*+*',trials_per_condition, permutations)
tpt_incong = fun.equationMaker('incongruent', 'binary', '*+*',trials_per_condition, permutations)
tpt_cong2 = fun.equationMaker('congruent', 'binary2', '*+*',trials_per_condition, permutations)
tpt_incong2 = fun.equationMaker('incongruent', 'binary2', '*+*',trials_per_condition, permutations)
tpt_neut = fun.equationMaker('neutral', 'nonaccent', '*+*',trials_per_condition, permutations)

# catch trials
cat_ptp_cong = fun.equationMaker('congruent', 'binary', '+*+',assort_trials, permutations, catch = True)
cat_ptp_incong = fun.equationMaker('incongruent', 'binary', '+*+',assort_trials, permutations, catch = True)
cat_ptp_cong2 = fun.equationMaker('congruent', 'binary2', '+*+',assort_trials, permutations, catch = True)
cat_ptp_incong2 = fun.equationMaker('incongruent', 'binary2', '+*+',assort_trials, permutations, catch = True)
cat_ptp_neut = fun.equationMaker('neutral', 'nonaccent', '+*+',assort_trials, permutations, catch = True)

# catch
cat_tpt_cong = fun.equationMaker('congruent', 'binary', '*+*',assort_trials, permutations, catch = True)
cat_tpt_incong = fun.equationMaker('incongruent', 'binary', '*+*',assort_trials, permutations, catch = True)
cat_tpt_cong2 = fun.equationMaker('congruent', 'binary2', '*+*',assort_trials, permutations, catch = True)
cat_tpt_incong2 = fun.equationMaker('incongruent', 'binary2', '*+*',assort_trials, permutations, catch = True)
cat_tpt_neut = fun.equationMaker('neutral', 'nonaccent', '*+*',assort_trials, permutations, catch = True)

# assorted '* * +' trials 
ttp_cong = fun.equationMaker('congruent', 'binary', '**+',assort_trials, permutations) #8
ttp_incong = fun.equationMaker('incongruent', 'binary', '**+',assort_trials, permutations) #16
ttp_cong2 = fun.equationMaker('congruent', 'binary2', '**+',assort_trials, permutations) # 24
ttp_incong2 = fun.equationMaker('incongruent', 'binary2', '**+',assort_trials, permutations) # 32
"""
# assorted '* + /' trials 
tpd_cong = fun.equationMaker('congruent', 'binary', '*+/',assort_trials, permutations) #8
tpd_incong = fun.equationMaker('incongruent', 'binary', '*+/',assort_trials, permutations) #16
tpd_cong2 = fun.equationMaker('congruent', 'binary2', '*+/',assort_trials, permutations) # 24
tpd_incong2 = fun.equationMaker('incongruent', 'binary2', '*+/',assort_trials, permutations) # 32
"""
###===QUESTIONAIRE===###
#gsi_part1 = fun.instImport('Stimuli/Questionnaire/GSI_1-31.txt')
#gsi_part2 = fun.instImport('Stimuli/Questionnaire/GSI_32-38.txt')
#gsi_part2_scales = [['0','1', '2', '3', '4-5', '6-9', '10+'],
#                    ['0', '0.5', '1', '1.5', '2', '3-4', '5+'],
#                    ['0', '1', '2', '3', '4-6', '7-10', '11+'], 
#                    ['0', '0.5', '1', '2', '3', '4-6', '7+'], 
#                    ['0', '0.5', '1', '2', '3-5', '6-9', '10+'], 
#                    ['0', '1', '2', '3', '4', '5', '6+'],
#                    ['0-15mins', '15-30mins', '30-60mins', '60-90mins', '2hrs', '2-3hrs', '4+hours']]
