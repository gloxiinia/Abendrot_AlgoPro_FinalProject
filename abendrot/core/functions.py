from sys import stdout
from random import uniform, choice
from time import sleep
from string import punctuation
from tabulate import tabulate
from art import *


#function for returning the scene id from the scenes list
def getScenefromId(ids, scenes):
    for scene in scenes:
        if ids == scene.id:
            return scene


#function to examine an object in a scene
def examineObject(scene, object_name):
    invalidObject = ["\nIt's...something, that's for sure, but you don't know what it is exactly.", "\nYou're not sure what that is.",
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


#function to print the help screen
def getHelp():
    printBorder()
    helpText ="""                       
    This is the essential information needed to play the game.\n\n\n
    >                       Type your commands in the console to do them                       <\n
    >                         Use "map" to bring up the map of Sonnenau                        <\n
    >                    Use "look at" or "examine" to inspect an something                    <\n
    >            Use "talk to" or "chat with" to start a conversation with someone             <\n
    >        Use "up", "down", "left", "right" or use cardinal directions to move around       <\n
    >                           Don\'t forget to have fun! ૮ ˶ᵔ ᵕ ᵔ˶ ა                          <
    """
    centerText(helpText)


# function for typewriter effect
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

#defining a function that will print a border for the title, help, credits screens and in general
def printBorder():
    #declaring the border ascii art as the borderArt variable
    borderArt = '''
  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.      .--.      .-'.      .--.   
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\  
       `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `--'      `--'      `.-'      `-            
'''
    print('\n\n'+borderArt + '\n\n')


#function for centering text
def centerText(text):
    for line in text.split("\n"):
        print(line.center(104))


#function for getting the scene's designated id from the list of scenes
def getScenefromId(sid, scenes):
    for scene in scenes:
        if sid == scene.id:
            return scene

#function for getting list of npc names in a scene
def getNPCnames(activeScene):
    npcList = []
    for npc in activeScene.npcs:
        npcList.append(npc.name)
        npcList.extend(npc.aliases)
    return npcList

#function for a while loop that checks if the user typed their name correctly
def isNameright(name):
    while True:
        #prompting user input
        checkName = input(f'\n{name}, is that correct?\n> ')
        #checking if user input is a valid option
        if checkName.strip().lower() in ['no', 'n', 'nope', 'wrong']:
            print('\nI see, please reenter your name.')
            name = input('> ')
            continue
        #stops the loop if no invalid values are found
        elif checkName in ['yes', 'correct', 'y', 'yeah', 'yea', 'yep', 'mhm', 'right']:
            break
        else:
            print('\nI couldn\'t understand that. Try again, little bird.')
            continue
    return name

#function for collecting the player name from input
def getPlayername(player):
    #COLLECTING PLAYER NAME
    askPlayername = "Ah, I sense that you are new to this world.\nA lost soul wandering the emptiness of the cosmos.\n\nDo tell, what is your name, Vöglein?\n"
    typeWriter(askPlayername)
    playerName = isNamevalid(askPlayername)
    playerName = isNameright(playerName)
    typeWriter(f'\n{playerName}... Fascinating.\n',0.3)
    typeWriter('Your name is foreign to my memory, yet the aura you carry within is familiar.\n')
    playerName = player.setPlayername(playerName)
    return playerName

#function for a while loop that checks if the user's name is the same as any myPlayers in the game
def isNamevalid(playerName):
    charList = ['mama', 'petra', 'michel', 'julian', 'korvin', 'emil', 'felix', 'ferdinand', 'ingrid', 'nico']
    while True:
        playerName = input('> ')
        if playerName.strip().lower() not in charList:
            break
        else:
            print('\nOh? It seems you\'ve the same name as a Sonnenau resident...\nI apologize, but you must pick a different alias.')
            continue
    return playerName
        
#function for printing a visualized map in table form
def printMap(player):
    #creating a dictionary for the map area
    areaGrid = {
    'a':[f'{player.name}\'s House',"Vagabond's Folly"],
    'b':["", 'Sonnenau Plaza', 'Sol Lane', 'Sonnenau Entrance', 'Sensuchtbucht'],
    'c':['','', 'Forest Entrance'],
    'd':['','','Hain der Waldkäuze'],
    'e':['','',"Julian's Cottage", "Julian's Garden", "Meeresarm der Begehrlichen"]
    }
    #printing the map in table form with tabulate
    print('\n' + tabulate(areaGrid, headers='keys', tablefmt='fancy_grid', showindex=range(1,6)))

#function for attempting to change the scene/location if the player puts in a move command
def tryScenechange(activeScene, scenes, direction):
    changedScene = False
    moveNorth = ("north", "up")
    moveSouth = ("south", "down")
    moveEast = ("east", "right")
    moveWest = ("west", "left")

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
        invalidMoveresponse = ["\nYou can't travel in that direction.", "\nWhoa, slow down, that way's a no-go.", "\nAch nein, you can't go that way, sorry.",
                                "\nIf I could let you pass I would, but... I can't so, try again, Vöglein."]
        description = choice(invalidMoveresponse)

    return activeScene, description

#function for printing the player's current location
def moveHandler(current_scene, description):
    invalidMoveresponse = ["\nYou can't travel in that direction.", "\nWhoa, slow down, that way's a no-go.", "\nAch nein, you can't go that way, sorry.",
                                "\nIf I could let you pass I would, but... I can't so, try again, Vöglein."]
    if description in invalidMoveresponse:
        print('\n' + description)
        print('\nYou are still at ' + current_scene.areaName)

    else:
        print('\nYou have moved to ' + current_scene.areaName) 
        printBorder()
        centerText(current_scene.areaName.upper())
        centerText(description)

#function for trying to start a conversation with an npc if a player puts in a talk command
#def tryForNPCdialogue(activeScene, npcName, playerChoice):
    #conversationStarted = False
    ##print(dialogue[0], dialogue[1])

def playerDialoguechoice(scene, npcName, playerChoice):
    invalidNpc = ["\nYou can't talk to this person.", "\nThey don't seem to be able to talk right now."]
    description = choice(invalidNpc)
    for sceneNpc in scene.npcs:
        if npcName == sceneNpc.name:
            if playerChoice == 1:
                description = sceneNpc.dialogueResponse1
            if playerChoice == 2:
                description = sceneNpc.dialogueResponse2
            if playerChoice == 3:
                description = sceneNpc.dialogueResponse3
        else:
            for alias in sceneNpc.aliases:
                if npcName == alias:
                    if playerChoice == 1:
                        description = sceneNpc.dialogueResponse1
                    if playerChoice == 2:
                        description = sceneNpc.dialogueResponse2
                    if playerChoice == 3:
                        description = sceneNpc.dialogueResponse3                    
    return description

#function for printing the available dialogue choices for the player
def printDialoguechoices(scene, npcName):
    for sceneNpc in scene.npcs:
        if npcName == sceneNpc.name:
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

#function to try for dialogue with an npc
def tryNPCdialogue():
    pass


#function to return the dialogue 
def getNpcdialogue(scene, npcName, dialogueId):
    dialogue = "\nThat conversation topic isn't available.\n"
    dialogueStarted = False
    for sceneNpc in scene.npcs:
        if npcName == sceneNpc.name:
            if dialogueId == 1:
                dialogue = sceneNpc.dialogueTexts[0]
                dialogueStarted = True
            if dialogueId == 2:
                dialogue = sceneNpc.dialogueTexts[1]   
                dialogueStarted = True  
            if dialogueId == 3:
                dialogue = sceneNpc.dialogueTexts[2]
                dialogueStarted = True       
        
        else:
            for alias in sceneNpc.aliases:
                if npcName == alias:
                    if dialogueId == 1:
                        dialogue = sceneNpc.dialogueTexts[0]
                        dialogueStarted = True
                    if dialogueId == 2:
                        dialogue = sceneNpc.dialogueTexts[1]
                        dialogueStarted = True
                    if dialogueId == 3:
                        dialogue = sceneNpc.dialogueTexts[2]
                        dialogueStarted = True
        
    if dialogueStarted == True:
        for sceneNpc in scene.npcs:
            if npcName == sceneNpc.name:
                if dialogueId == 1:
                    sceneNpc.dialogueTexts.pop(0)
                    sceneNpc.dialogueResponses.pop(0)

                if dialogueId == 2:
                    sceneNpc.dialogueTexts.pop(1)
                    sceneNpc.dialogueResponses.pop(1)
    
                if dialogueId == 3:
                    sceneNpc.dialogueTexts.pop(2)
                    sceneNpc.dialogueResponses.pop(2)
            else:
                for alias in sceneNpc.aliases:
                    if npcName == alias:
                        if dialogueId == 1:
                            sceneNpc.dialogueTexts.pop(0)
                            sceneNpc.dialogueResponses.pop(0)                            
                        if dialogueId == 2:
                            sceneNpc.dialogueTexts.pop(1)
                            sceneNpc.dialogueResponses.pop(1)
                        if dialogueId == 3:
                            sceneNpc.dialogueTexts.pop(2)
                            sceneNpc.dialogueResponses.pop(2)
    return dialogue


   

