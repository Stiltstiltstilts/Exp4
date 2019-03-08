#!/Users/Stilts/PsychoPyBuild/bin/python

################################################
################# Imports ######################
################################################
from psychopy import core, visual, logging, gui, event, prefs, data, monitors
import pyo
prefs.general['audioLib'] = ['pyo']
prefs.general['audioDriver'] = ['ASIO']
from psychopy import sound
from numpy.random import random, randint, normal, shuffle
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import pygame.midi
import os
import sys
import numpy as np
from constants import *
from customFunctions import trialCreator

GlobalClock = core.Clock()  # Track time since experiment starts

################################################
############### Basic checks ###################
################################################
# check relative paths correct
_thisDir = os.path.abspath(os.path.dirname(__file__))
os.chdir(_thisDir)

################################################
####### Collect experiment session info ########
################################################
# Exp name
expName = 'Algebraic Beats'
# Define experiment info
expInfo = {'session':'001', 'participant':'001',
    'handedness':'', 'gender':'', 'native language': '', 'age': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName,)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()

# Create filename for data file (absolute path + name)
filename = _thisDir + os.sep + 'data/{0}'.format(expInfo['participant'])

################################################
################ Setup logfile #################
################################################
# save a log file for detailed verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

################################################
################# Variables ####################
################################################
####====Auditory Stimuli====####
binary_beat = sound.Sound('Stimuli/Tones/binary_beat.wav') 
ternary_beat = sound.Sound('Stimuli/Tones/ternary_beat.wav') 
unaccented_beat = sound.Sound('Stimuli/Tones/unaccented_beat.wav') 
binary2_beat = sound.Sound('Stimuli/Tones/binary_beat_8ve.wav')

# setup window
mon = monitors.Monitor(name = 'OptiPlex 7440',
                        width = 1920,
                        distance = 80)
mon.setWidth(80)
mon.setSizePix([1920, 1080])

win = visual.Window(fullscr=True,
                size = [1920, 1080],
                monitor = mon,
                units = 'deg',
                allowGUI = False)

trialClock = core.Clock()

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess 60Hz

with open('data/{}participant_info.txt'.format(expInfo['participant']), 'w') as log_file:
    log_file.write('Session\t' +
                    'Participant\t' +
                    'Handedness\t' +
                    'Gender\t' +
                    'Native_language\t' +
                    'Age\t' +
                    'frameRate\t' + '\n')
 
    log_file.write('\t'.join([str(expInfo['session']),
                            str(expInfo['participant']),
                            str(expInfo['handedness']),
                            str(expInfo['gender']),
                            str(expInfo['native language']),
                            str(expInfo['age']),
                            str(expInfo['frameRate'])]) + '\n')
    log_file.flush()

################################################
########## Trial list construction #############
################################################

# Main sentences
conditions = [ptp_cong, ptp_incong, ptp_cong2, ptp_incong2,
              tpt_cong, tpt_incong, tpt_cong2, tpt_incong2,
              ppp_cong, ppp_incong, ppp_cong2, ppp_incong2,]

catch_conditions = [cat_ptp_cong, cat_ptp_incong, cat_ptp_cong2, cat_ptp_incong2,
                    cat_tpt_cong, cat_tpt_incong, cat_tpt_cong2, cat_tpt_incong2, 
                    cat_ppp_cong, cat_ppp_incong, cat_ppp_cong2, cat_ppp_incong2,]                   

# Combining main and assorted trials into one list
trials = trialCreator(conditions)
catch_trials = trialCreator(catch_conditions)
trials = trials + catch_trials
shuffle(trials)
shuffle(trials)
all_trials = data.TrialHandler(trialList = trials[:], nReps = 1, method = 'random', extraInfo = expInfo, name = 'all_trials')
thisTrial = all_trials.trialList[0]  # so we can initialise stimuli with some values

################################################
############## Run experiment ##################
################################################
try: 
    # ==== SETUP TRIAL OBJECTS ==== #
    message1 = visual.TextStim(win, pos=[0,+3], color=FGC, alignHoriz='center', name='topMsg', text="placeholder") 
    message2 = visual.TextStim(win, pos=[0,-3], color=FGC, alignHoriz='center', name='bottomMsg', text="placeholder") 
    fixation = visual.TextStim(win,  pos=[0,0], color=FGC, alignHoriz='center', text="+")
    endMessage = visual.TextStim(win,  pos=[0,0], color=FGC, alignHoriz='center', text="The end! Thank you for participating :)")
    space_cont = visual.TextStim(win, pos=[0,0], color=FGC, text="Press space to continue")
    too_slow = visual.TextStim(win, pos=[0,0], color=FGC, text="Too slow: respond quicker next time")
    feedback = visual.TextStim(win, pos=[0,0], color=FGC, text="placeholder")
    introText = visual.TextStim(win, pos=[0,0], color=FGC, text="Placeholder")
    probe_text = visual.TextStim(win, pos=[0,0], color=FGC, height = 2, alignHoriz='center', name='top_probe', text="placeholder")
    break_text = visual.TextStim(win, pos=[0,0], color=FGC, text="Have a break and stretch for 15 seconds!")
    trial_text = visual.TextStim(win, pos=[0,0], color=FGC, text="Placeholer")
    word_stim_list = []
    for i in range(8): # setting up text_stimuli objects... 15 is the most words in the sent_stims
            exec( '{} = visual.TextStim(win, pos=[0,0], color=FGC, height = 2, text="placeholder")'.format('word' + '_' + str(i+1)) ) # create text objects
            exec( 'word_stim_list.extend([{}])'.format(str('word' + '_' + str(i+1))) ) # putting them in word_stim_list
    GSI = visual.RatingScale(win, name='GSI', marker='triangle',
                             textSize = 0.4, showValue = False, acceptText = 'confirm',
                              size=1.5, pos=[0.0, -0.4], 
                              choices=['Completely\n Disagree', 'Strongly\n Disagree',
                                         'Disagree', 'Neither Agree\n or Disagree', 'Agree',
                                          'Strongly\n Agree', 'Completely\n Agree'],
                             tickHeight=-1)
    response_keys = visual.TextStim(win, pos=[0,-5], height = .5, color=FGC, text="respond:'y' 'n' or 'd'")

    pygame.midi.init() # initialising midi

    # ==== OTHER TRIAL VARIABLES ==== #
    clock = core.Clock()
    trial_num = 0

    
    ################################################
    ############## START EXPERIMENT ################
    ################################################

    win.mouseVisible = False

    # ===== INSTRUCTIONS 1 ====== #
    counter = 0
    while counter < len(part1Intro):
        message1.setText(part1Intro[counter])
        if counter == 0:
            message2.setText(bottom_text[0])
        elif counter in range(1, (len(part1Intro) - 1)):
            message2.setText(bottom_text[1])
        else: 
            message2.setText(bottom_text[2])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions%d'%(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace' and counter > 0:
            counter -= 1
        else:
            counter += 1

    # ===== LOG FILE ====== #
    with open('data/{}trial_log.txt'.format(expInfo['participant']), 'w') as log_file:
        log_file.write('Trial\t' + 
                       'Beat\t' + 
                       'Equation\t' + 
                       'Structure\t' + 
                       'Congruency\t' + 
                       'Validity\t' +
                       'Sensitivity\t' +      
                       'Probe\t' + 
                       'Response\t' + 
                       'Accuracy\t' + 
                       'RT\t' + 
                       'trial_type' + '\n')
    log_file.close()

    # File for tapping info in main trials
    with open('data/{}tapping_log.txt'.format(expInfo['participant']), 'w') as tap_file:
        tap_file.write('Trial\t' + 
                        'Beat\t' +
                        'Equation\t' +    
                        'Congruency\t' +
                        'Structure\t' +
                        'Accuracy\t' +
                        'button\t' +
                        'timestamp' + '\n')
    tap_file.close()

        trial_num = 0

        # ===== TRIALS ====== #
        for thisTrial in all_trials:  
            drum_pad = pygame.midi.Input(pygame.midi.get_default_input_id())
            trial_num += 1

            # Check for break trial
            if trial_num % break_frequency == 0:
                break_text.draw()
                win.flip()
                core.wait(break_duration)

                ####====Space to continue====####
                event.clearEvents(eventType='keyboard')
                space_cont.draw()
                win.flip()
                thisKey = event.waitKeys(keyList=['space'])
                while not 'space' in thisKey:
                    thisKey = event.waitKeys(keyList=['space'])

            ####====ABBREVIATE PARAMETER NAMES====####
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            probe_resp = event.BuilderKeyResponse()

            ####====SETUP TRIAL COMPONENTS LIST====####
            # initialize trial components list
            trialComponents = []
            # add auditory stimuli component
            if (beat_type == 'binary' and congruency == 'congruent'):
                beat_stim   = binary_beat
                word_offset = 8 * beat_freq
            elif (beat_type == 'binary' and congruency == 'incongruent'):
                beat_stim   = binary_beat
                word_offset = 7 * beat_freq
            elif (beat_type == 'unaccented' and congruency == 'congruent'):
                beat_stim   = unaccented_beat
                word_offset = 8 * beat_freq
            
            if structure == '+*+':
                if (beat_type == 'binary2' and congruency == 'congruent'):
                    beat_stim   = binary2_beat
                    word_offset = 12 * beat_freq
                elif (beat_type == 'binary2' and congruency == 'incongruent'):
                    beat_stim   = binary2_beat
                    word_offset = 10 * beat_freq
            elif structure == '*+*':
                if (beat_type == 'binary2' and congruency == 'congruent'):
                    beat_stim   = binary2_beat
                    word_offset = 10 * beat_freq
                elif (beat_type == 'binary2' and congruency == 'incongruent'):
                    beat_stim   = binary2_beat
                    word_offset = 12 * beat_freq
            elif structure == '+++':
                if (beat_type == 'binary2' and congruency == 'congruent'):
                    beat_stim   = binary2_beat
                    word_offset = 10 * beat_freq
                elif (beat_type == 'binary2' and congruency == 'incongruent'):
                    beat_stim   = binary2_beat
                    word_offset = 12 * beat_freq

            trialComponents.extend([beat_stim]) # add beat stim to trialComponents list

            # add text stimuli components
            for i in range(len(stim)): # for i in range(len(trial['sent_stim'])):
                exec('trialComponents.extend([{}])'.format('word' + '_' + str(i+1)))
                word_stim_list[i].setText(stim[i])
            
            # set probe text for the trial
            probe_text.setText(probe)

            ####====BASIC ROUTINE CHECKS====####
            continueRoutine = True
            # keep track of which components have finished
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # display trial structure
            trial_text.setText(structure)
            trial_text.draw()
            win.flip()
            core.wait(.5)

            t = 0
            frameN = -1
            beatDuration = len(stim)*beat_freq + word_offset
            trialClock.reset()  # clock

            ####====START MAIN TRIAL ROUTINE====####
            while continueRoutine: 
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                ##### 1. start/stop beat_stim  #####
                if t >= 0.0 + sound_delay and beat_stim.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    beat_stim.tStart = t
                    beat_stim.frameNStart = frameN  # exact frame index
                    start_time = pygame.midi.time() # keep track of sound start time to adjust taps later
                    beat_stim.play()  # start the sound (it finishes automatically)
                    fixation.setAutoDraw(True)
                if beat_stim.status == STARTED and t >= beatDuration:
                    beat_stim.stop()

                ##### 2. check for midi input  #####
                if drum_pad.poll():
                    tap_data.append(drum_pad.read(1))

                ##### 3.  iterate through sentence text stimuli #####   
                for word_index in range(len(stim)):
                    if t >= word_index * beat_freq + word_offset and word_stim_list[word_index].status == NOT_STARTED:
                        fixation.setAutoDraw(False)
                        # keep track of start time/frame for later
                        word_stim_list[word_index].tStart = t
                        word_stim_list[word_index].frameNStart = frameN  # exact frame index
                        word_stim_list[word_index].setAutoDraw(True)
                    frameRemains = (beat_freq * word_index) + beat_freq + word_offset - win.monitorFramePeriod * 0.75  # most of one frame period left
                    if word_stim_list[word_index].status == STARTED and t >= frameRemains:
                        word_stim_list[word_index].setAutoDraw(False)

                ##### 4.  check if all components have finished #####
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                ##### 5.  refresh the screen #####
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            ####====Ending Trial Routine====####
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            beat_stim.stop()  # ensure sound has stopped at end of routine

            win.flip()
            drum_pad.close()
            core.wait(probe_delay) 

            ####====Probe====####
            # 3.  display probe text e.g. "The boy helped the girl?" #####
            probe_text.tStart = t
            probe_text.setAutoDraw(True)
            response_keys.setAutoDraw(True)

            ####====check for response====##### 
            probe_resp.tStart = t
            win.callOnFlip(probe_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
            thing = True
            while thing: 
                win.flip()
                theseKeys = event.getKeys(keyList=['y', 'n', 'd'])
                if len(theseKeys) > 0:  # at least one key was pressed
                    probe_text.setAutoDraw(False)
                    response_keys.setAutoDraw(False)
                    probe_resp.keys = theseKeys[-1]  # just the last key pressed
                    probe_resp.rt = probe_resp.clock.getTime()
                    # was this 'correct'?
                    if probe_resp.keys == 'y' and (validity == 'True' and trial_type == 'main'):
                        probe_resp.corr = 1
                        feedback.setText("correct")
                        feedback.draw()
                    elif probe_resp.keys == 'n' and (validity == 'False' or trial_type == 'catch'):
                        probe_resp.corr = 1
                        feedback.setText("correct")
                        feedback.draw()
                    elif probe_resp.keys == 'd':
                        probe_resp.corr = 0
                        feedback.setText("(don't know)")
                        feedback.draw()
                    else:
                        probe_resp.corr = 0
                        feedback.setText("incorrect")
                        feedback.draw()

                    #======WRITE DATA TO FILE======#    
                    log_file.write('\t'.join([str(trial_num),
                                str(beat_type),
                                str(stim),
                                str(structure),
                                str(congruency),
                                str(validity),
                                str(sensitivity),
                                str(probe),
                                str(probe_resp.keys),
                                str(probe_resp.corr),
                                str(probe_resp.rt),
                                str(trial_type)]) + '\n')
                    
                    log_file.flush()

                    with open('data/{}tapping_log.txt'.format(expInfo['participant']), 'a') as tap_file:
                        for tap in tap_data:
                            tap_file.write('\t'.join([str(trial_num),
                                    str(beat_type),
                                    str(stim),
                                    str(congruency),
                                    str(structure),
                                    str(probe_resp.corr),
                                    str(tap[0][0]),
                                    str(tap[0][1] - start_time)]) + '\n')
                    tap_file.close()
                    
                    probe_text.setAutoDraw(False)
                    thing = False
            win.flip()
            core.wait(1)

            ####====Check if response is too slow====####
            if probe_resp.rt > probe_duration:
                too_slow.draw()
                win.flip()
                core.wait(2) 
            
            ####====Space to continue====####
            event.clearEvents(eventType='keyboard')
            space_cont.draw()
            win.flip()
            thisKey = event.waitKeys(keyList=['space'])
            while not 'space' in thisKey:
                thisKey = event.waitKeys(keyList=['space'])

            #thisExp.nextEntry()
            core.wait(.5)

        logging.flush()
    """
    ################################################
    ############## GSI QUESTIONNAIRE ################
    ################################################
    # ===== INSTRUCTIONS 3 ====== #
    counter = 0
    while counter < len(part3Intro):
        message1.setText(part3Intro[counter])
        if counter == 0:
            message2.setText(bottom_text[0])
        elif counter in range(1, (len(part3Intro) - 1)):
            message2.setText(bottom_text[1])
        else: 
            message2.setText(bottom_text[2])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions%d'%(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace':
            counter -= 1
        else:
            counter += 1

    with open('data/{}questionnaire_log.txt'.format(expInfo['participant']), 'w') as log_file:
        log_file.write('Question_num\t' +
                       'Question\t' +
                       'Response' + '\n')

        quest_num = 1 # initialising counter 
        for question in gsi_part1:
            message1.setText(question)
            while GSI.noResponse: 
                message1.draw()
                GSI.draw()
                win.flip()
            response = GSI.getRating()
            #======WRITE DATA TO FILE======#    
            log_file.write('\t'.join([str(quest_num),
                            str( question.replace('\n','') ),
                            str( response.replace('\n','') )]) + '\n')
            
            log_file.flush()
            GSI.noResponse = True
            GSI.response = None
            quest_num += 1
            core.wait(.2)
        
        quest_num = 1 # initialising counter 
        for question in gsi_part2:
            message1.setText(question)
            GSI = visual.RatingScale(win, name='GSI', marker='triangle',
                             textSize = 0.4, showValue = False, acceptText = 'confirm',
                              size=1.5, pos=[0.0, -0.4], 
                              choices= gsi_part2_scales[quest_num - 1],
                             tickHeight=-1)
            while GSI.noResponse: 
                message1.draw()
                GSI.draw()
                win.flip()
            response = GSI.getRating()
            #======WRITE DATA TO FILE======#    
            log_file.write('\t'.join([str((quest_num + 31)),
                            str( question.replace('\n','') ),
                            str( response.replace('\n','') )]) + '\n')
            
            log_file.flush()
            GSI.noResponse = True
            GSI.response = None
            quest_num += 1
            core.wait(.2)
        """
    endMessage.draw()
    win.flip()
    core.wait(5)
finally:
    pygame.midi.quit()
    win.close()
    core.quit()
