from sys import stdout
from random import uniform, choice
from time import sleep
from art import *
from PIL import Image
from playsound import playsound
import os

####MOVEMENT####

#function for returning the scene's designated id from the scenes list
def getScenefromId(ids, scenes):
    for scene in scenes:
        if ids == scene.id:
            return scene
            
#function for attempting to change the scene/location if the player puts in a move command
def tryScenechange(activeScene, scenes, direction):
    changedScene = False
    moveNorth = ["north", "up"]
    moveSouth = ["south", "down"]
    moveEast = ["east", "right"]
    moveWest = ["west", "left"]

    if direction in moveNorth:
        if activeScene.north is not None:
            activeScene = getScenefromId(activeScene.north, scenes)
            changedScene = True
    elif direction in moveSouth:
        if activeScene.south is not None:
            activeScene = getScenefromId(activeScene.south, scenes)
            changedScene = True
    elif direction in moveEast:
        if activeScene.east is not None:
            activeScene = getScenefromId(activeScene.east, scenes)
            changedScene = True
    elif direction in moveWest:
        if activeScene.west is not None:
            activeScene = getScenefromId(activeScene.west, scenes)
            changedScene = True

    if changedScene:
        description = activeScene.getDescription()
    else:
        invalidMoveresponse = ["You can't travel in that direction.", "Whoa, slow down, that way's a no-go.", 
                                "Ach nein, you can't go that way, sorry.",
                                "If I could let you pass I would, but... I can't so, try again, Vöglein."]
        description = choice(invalidMoveresponse)

    return activeScene, description

#function for printing the player's current location
def moveHandler(current_scene, description):
    invalidMoveresponse = ["You can't travel in that direction.", "Whoa, slow down, that way's a no-go.", 
                                "Ach nein, you can't go that way, sorry.",
                                "If I could let you pass I would, but... I can't so, try again, Vöglein."]
    if description in invalidMoveresponse:
        print('\n' + description)
        print('\nYou are still at ' + current_scene.areaName)

    else:
        print('\nYou have moved to ' + current_scene.areaName) 
        printBorder()
        centerText(current_scene.areaName.upper())
        centerText(description)

#### EXAMINING ####
#function to examine an object in a scene
def examineObject(scene, object_name):
    invalidObject = ["\nIt's...something, that's for sure, but you don't know what it is exactly.", 
                    "\nYou're not sure what that is.",
                    "\nIt's nothing much to look at, surely?"]
    description = choice(invalidObject)

    if object_name == 'around' or object_name == '':
            description = scene.getExamination() 
    else:
        for sceneObject in scene.objects:      
            if object_name == sceneObject.name:
                description = sceneObject.detailedDescription

            else:
                for alias in sceneObject.aliases:
                    if object_name == alias:
                        description = sceneObject.detailedDescription
    
    return description

#function to return npc profile for if a player examines an NPC
def examineNpc(scene, npcName):
    invalidNpc = ["\nYou're not sure who that is.", "\nThere's not much to say about this person."]
    description = choice(invalidNpc)
    for sceneNpc in scene.npcs:
        if npcName == sceneNpc.name:
            description = sceneNpc.NPCprofile

        else:
            for alias in sceneNpc.aliases:
                if npcName == alias:
                    description = sceneNpc.NPCprofile
    return description


#function to print the help screen
def getHelp():
    printBorder()
    helpText ="""                       
    This is the essential information needed to play the game.\n\n\n
    >                       Type your commands in the console to do them                       <\n
    >                         Use "map" to bring up the map of Sonnenau                        <\n
    >                    Use "look at" or "examine" to inspect an something                    <\n
    >       Use examine words and 'around' to get a more detailed description of the area      <\n
    >            Use "talk to" or "chat with" to start a conversation with someone             <\n
    >                   Use 'leave' or 'escape' to exit from a conversation                    <\n
    >      Use 'help' to bring up these instructions at any point if you forget something      <\n
    >        Use "up", "down", "left", "right" or use cardinal directions to move around       <\n
    >                           Don\'t forget to have fun! ૮ ˶ᵔ ᵕ ᵔ˶ ა                          <
    """
    centerText(helpText)

####GENERAL FUNCTIONS####

#function for typewriter effect
def typeWriter(text, start=None, stop=None):
    if start is None:
        start = 0.05
    if stop is None:
        stop = 0.1
    for i in range(len(text)):
        stdout.write(text[i])
        stdout.flush()
        sleep(uniform(start, stop))
    return

#function that will print a border for the title, help, credits screens and in general
def printBorder():
    #declaring the border ascii art as the borderArt variable
    borderArt = '''
.--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.      .--.      .-'.      .--.       .--.   
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\:::::::::.\:::
         `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `--'      `--'      `.-'      `-.-'      `-     
'''
    centerText('\n\n'+borderArt + '\n\n')

#function to print end credits
def printEndcredits():
    os.system('cls')
    endCredits = text2art("Thank you\nfor playing\nAbendrot.", font='georgia11')
    centerText(endCredits)
    printBorder()
    filename = open('creditsPicture.txt', 'r')
    print(filename.read())
    filename.close
    playsound('The_Koi_and_the_Dragon.wav')

#function for centering text
def centerText(text):
    for line in text.split("\n"):
        print(line.center(126))

#function for getting list of npc names in a scene
def getNPCnames(activeScene):
    npcList = []
    for npc in activeScene.npcs:
        npcList.append(npc.name)
        npcList.extend(npc.aliases)
    return npcList

#function for getting list of *all* npc names
def getAllnpcNames(scenes):
    allNpclist = []
    for scene in scenes:
        for npc in scene.npcs:
            allNpclist.append(npc.name)
            allNpclist.extend(npc.aliases)
    return allNpclist

#function for a while loop that checks if the user typed their name correctly
def isNameright(scenes, name):
    while True:
        #prompting user input
        checkName = input(f'\n{name}, is that correct?\n> ')
        #checking if user input is a valid option
        if checkName.strip().lower() in ['no', 'n', 'nope', 'wrong']:
            print('\nI see, please reenter your name.')
            name = isNamevalid(scenes, checkName)
            continue
        #stops the loop if no invalid values are found
        elif checkName in ['yes', 'correct', 'y', 'yeah', 'yea', 'yep', 'mhm', 'right']:
            break
        else:
            print('\nI couldn\'t understand that. Try again, little bird.')
            continue
    return name

#function for collecting the player name from input
def getPlayername(scenes, player):
    #COLLECTING PLAYER NAME
    askPlayername = """Ah, I sense that you are new to this world.\nA lost soul wandering the emptiness of the cosmos.
    \n\nDo tell, what is your name, Vöglein?\n"""
    typeWriter(askPlayername)
    playerName = isNamevalid(scenes, askPlayername)
    playerName = isNameright(scenes, playerName)
    typeWriter(f'\n{playerName}... Fascinating.\n',0.3)
    typeWriter('Your name is foreign to my memory, yet the aura you carry within is familiar.\n')
    player.setPlayername(playerName)
    return playerName

#function for a while loop that checks if the user's name is the same as any playerNames in the game
def isNamevalid(scenes, playerName):
    while True:
        playerName = input('> ')
        if playerName.strip().lower() not in getAllnpcNames(scenes):
            break
        else:
            print('\nOh? It seems you\'ve the same name as a Sonnenau resident...\nI apologize, but you must pick a different alias.')
            continue
    return playerName
        
#function for printing a visualized map in an image
def printMap():
    #using the open command to open the picture of the Sonnenau map
    sonnenauMap = Image.open("Sonnenau.jpg")
    sonnenauMap.show()


####DIALOGUE####
#function for printing the available dialogue choices for the player
def printDialoguechoices(scene, npcName):
    for sceneNpc in scene.npcs:
        if not sceneNpc.dialogueResponses:
            break
        elif npcName == sceneNpc.name:
            print(sceneNpc.dialogueBlurbs)
            y = 1
            for x in range(len(sceneNpc.dialogueResponses)):
                print(f'{y}. ' + sceneNpc.dialogueResponses[x])
                y += 1
        else:
            for alias in sceneNpc.aliases:
                if npcName == alias:
                    print(sceneNpc.dialogueBlurbs)
                    y = 1
                    for x in range(len(sceneNpc.dialogueResponses)):
                        print(f'{y}. ' + sceneNpc.dialogueResponses[x])
                    y += 1    


#function to return the dialogue 
def getNpcdialogue(scene, npcName, dialogueId, player):
    dialogue = "\nThat conversation topic isn't available.\n"
    dialogueStarted = False
    for sceneNpc in scene.npcs:
        if npcName == sceneNpc.name:
            dialogue = sceneNpc.dialogueTexts[dialogueId - 1]
            dialogueStarted = True
        else:
            for alias in sceneNpc.aliases:
                if npcName == alias:
                    dialogue = sceneNpc.dialogueTexts[dialogueId - 1]
                    dialogueStarted = True
        
    if dialogueStarted == True:
        for sceneNpc in scene.npcs:
            if npcName == sceneNpc.name and npcName == 'julian':
                player.gameOver = True

            elif npcName == sceneNpc.name:
                sceneNpc.dialogueTexts.pop(dialogueId - 1)
                sceneNpc.dialogueResponses.pop(dialogueId-1)
            else:
                for alias in sceneNpc.aliases:
                    if npcName == alias and npcName == 'jules':
                        player.gameOver = True
                    if npcName == alias:
                        sceneNpc.dialogueTexts.pop(dialogueId -1)
                        sceneNpc.dialogueResponses.pop(dialogueId - 1)                            
    return dialogue


#function for trying to start a conversation with an npc if a player puts in a talk command
def tryForNPCdialogue(scenes, currentScene, npcName, player):
    #if statements to check if the intended npc to be talked with is valid
    dialogue = "\nYou can't talk to that person right now.\n"
    dialogueStarted = False
    for npc in currentScene.npcs:
        if npcName == npc.name:
            if npc.dialogueResponses == []:
                return dialogue
            else:
                break
        else:
            for alias in npc.aliases:
                if npcName == alias:
                    if npc.dialogueResponses == []:
                        return dialogue
                    else:
                        break  

    if npcName == player.name or npcName in ['me', 'myself']:
        dialogue = '\nWell, if you wanna talk with yourself, be my guest...\n' 

    elif npcName == '' or npcName not in getAllnpcNames(scenes):
        invalidTalkList1 = ["I don't know who that is.", "With who? Try again, please.", 
                            "I don't seem to recognize that name.", "Oh I've heard that name... They're not in Sonnenau though."]
        dialogue = '\n' + choice(invalidTalkList1)+ '\n'  

    elif npcName not in getNPCnames(currentScene):
        invalidTalkList2 = ["Sorry, they're not here right now.", "Vöglein, they're not in your general vicinity.",
                            "Aiya, I don't see them anywhere here."]
        dialogue = '\n' +  choice(invalidTalkList2) + '\n'
    

    #else statement for if npc to be talked with is found to be valid
    else:
        dialogueStarted = True
    
    if dialogueStarted:
        dialogue = askFordialogueChoice(currentScene, npcName, player)
        return dialogue
    else:
        return dialogue


#function to ask user input for dialogue choices 
def askFordialogueChoice(scene, npcName, player):
    dialogue = "\nThat conversation topic isn't available. Try another one.\n"
    while True:
        dialogueChoice = input("> ")
        if dialogueChoice == '0':
            typeWriter(dialogue, 0.05)
            continue
        else:
            if dialogueChoice not in ['leave', 'exit', 'esc', 'x']:
                try:
                    dialogueChoice = int(dialogueChoice)
                    dialogue = getNpcdialogue(scene, npcName, dialogueChoice, player)
                except IndexError:
                    typeWriter(dialogue, 0.05)
                    continue
                except ValueError:
                    typeWriter(dialogue, 0.05)                        
                    continue
                else:
                    return dialogue
            else:
                leaveConversation = ["\nYou have left the conversation.\n", 
                                    "\nYou think it over and decide to not go over to talk.\n",
                                    "\nOn second thought, you want to do something else.\n"]
                dialogue = choice(leaveConversation)
                return dialogue
