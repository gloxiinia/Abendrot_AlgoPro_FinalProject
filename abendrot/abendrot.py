#importing the needed modules



from core.parsertext import parse
from core.functions import tryScenechange, examineObject, getHelp, moveHandler, examineNpc, printDialoguechoices
from core.functions import centerText, typeWriter, printBorder, printMap, getPlayername, tryForNPCdialogue, printEndcredits
from art import *

import random
import sys, os

#importing the individual scenes from the scenes folder
import scenes.scene as char
import scenes.scene1 as s1
import scenes.scene2 as s2
import scenes.scene3 as s3
import scenes.scene4 as s4
import scenes.scene5 as s5
import scenes.scene6 as s6
import scenes.scene7 as s7
import scenes.scene8 as s8
import scenes.scene9 as s9
import scenes.scene10 as s10
import scenes.scene11 as s11


#creating a list for the scenes in the game
scenes = []
scene_1 = s1.SceneOne()
scenes.append(scene_1)
scenes.append(s2.SceneTwo())
scenes.append(s3.SceneThree())
scenes.append(s4.SceneFour())
scenes.append(s5.SceneFive())
scenes.append(s6.SceneSix())
scenes.append(s7.SceneSeven())
scenes.append(s8.SceneEight())
scenes.append(s9.SceneNine())
scenes.append(s10.SceneTen())
scenes.append(s11.SceneEleven())

os.system("MODE 130, 150")
#setting the initial active scene as the first scene
activeScene = scene_1

#creating the player
myPlayer = char.Player()


#function for prompting the player with an input as an action
def promptAction():
    isGameover = False
    global activeScene
    #creating a list of acceptable actions for the player to do
    acceptActions = ['look', 'lookat', 'lookaround' 'inspect', 'check', 'examine', 'move', 'walk', 'go',
                    'travel', 'quit', 'talk', 'chat', 'ask', 'question', 'map', 'help']
    examineActions = ['look', 'lookat', 'inspect', 'check', 'examine']
    moveActions = ['move', 'walk', 'travel', 'go']
    talkActions = ['talk', 'chat']

    #list of valid move directions
    moveDirections = ['north', 'up', 'south', 'down', 'east', 'right', 'west', 'left']

    #list of the character names
    charList = ['mama', 'petra', 'michel', 'julian', 'korvin', 'emil', 'felix', 'ferdinand', 'ingrid', 'nico']

    #while loop to check if user input is valid
    while isGameover == False:
        #prompting for user input, what action they want to do
        playerAction = input('\nSo, what do you wanna do?\n> ')
        parsedAction = parse(playerAction)

        #if statement to check if the parsed action is valid
        if parsedAction[0] not in acceptActions:
            invalidActionlist = ["\nSorry, no dice, you can't do that, try again.", "\nBuddy, I can't understand that, try again.",
            "\nCould you try again? I can't seem to recognize that command.", "\nTut mir leid, Vöglein, unfortunately you can't do that."]
            print(random.choice(invalidActionlist))
            break

        #elif statement to print out the help screen
        elif parsedAction[0] == 'help':
            getHelp()
            break
            
        #elif statement for if user wants to quit the game
        elif parsedAction[0] == 'quit':
            print('\nAight, it was fun. Goodbye, for now.')
            sys.exit()

        #elif statement for printing the map
        elif parsedAction[0] == 'map' or parsedAction[0] in examineActions and parsedAction[1] == 'map':
            printMap(myPlayer)
            break

        #elif statement for if user wants to inspect or look at something
        elif parsedAction[0] in examineActions :
            if parsedAction[1] in charList:
                output = examineNpc(activeScene, parsedAction[1])
            
            else:
                output = examineObject(activeScene, parsedAction[1])
            print(output)
            break
        
        #elif statement for if user wants to move
        elif parsedAction[0] in moveActions :
            if parsedAction[1] not in moveDirections:
                invalidMovedirectionsList = ["Hmm? I didn't catch that, go where? Try again, please.", "Where did you wanna go? Could you try again?",
                "I didn't recognize that direction, sorry.", "Try again please, I couldn't understand which direction you meant."]
                print('\n' + random.choice(invalidMovedirectionsList))
                break
            else:
                result = tryScenechange(activeScene, scenes, parsedAction[1])
                activeScene = result[0]
                output = result[1]
                moveHandler(activeScene, output)
                break

        #elif statement for if the user wants to talk to an NPC
        elif parsedAction[0] in talkActions:
            printDialoguechoices(activeScene, parsedAction[1])
            output = tryForNPCdialogue(activeScene, parsedAction[1], myPlayer)
            dialogue = output
            dialogue = dialogue.replace('playername', myPlayer.name)
            typeWriter(dialogue, 0.05)
            break
        if myPlayer.gameOver is True:
            isGameover = True
            break
        
#GAME FUNCTIONALITY
def gameLoop():
    while myPlayer.gameOver == False:
        promptAction()
    
    if myPlayer.gameOver is True:
        printEndcredits()
        sys.exit

#defining the title screen function that will determine the desired user selection
def titleScreenoptions():
    #list of title options in the main menu
    titleOptions = ['play', 'help', 'quit', 'credits', 'credit', 'about']
    #while loop for input validation
    while True:
        #asking for user input
        userOption = input('> ')
        userOption = userOption.strip().lower()
        #checking if user input is a valid option
        if userOption not in titleOptions:
            print('Please enter a valid option from the menu.')
            continue
        #stops the loop if no exceptions or invalid values are found
        else:
            break
    #input validation with elif statements
    if userOption == 'play':
        #calls the startgame function to start the game
        gameSetup() #placeholder function, if implemented, will run the game's code

    elif userOption == 'help':
        #calls the helpMenu function to show the help menu
        helpScreen()

    elif userOption == 'credits' or userOption == 'credit':
        #calls the creditScreen function to show the credits screen
        creditScreen()
    
    elif userOption == 'about':
        #calls the aboutScreen function to show the about screen
        aboutScreen()

    elif userOption == 'quit':
        #quits the program
        sys.exit() 


#declaring a function that will print the title screen
def printTitle():
    #using os functions to clear the console
    os.system('cls')
    #calling the printBorder function
    printBorder()
    #declaring the converted ascii art title to the titleArt variable
    titleArt=text2art("Abendrot", font='fraktur')
    #printing the title art
    centerText(titleArt)
    #declaring the sunset ascii art as the sunset variable
    sunset = '''
                                  ^^                   @@@@@@@@@
                             ^^       ^^            @@@@@@@@@@@@@@@
                                                  @@@@@@@@@@@@@@@@@@              ^^
                                                 @@@@@@@@@@@@@@@@@@@@
                       ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
                       ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
                         ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
                         ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
                       ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
                        ~             ~        ~      ~      ~~   ~             ~
            '''
    #printing the sunset art
    print(sunset)
    #closing the title screen art section by calling another printBorder
    printBorder()
    #printing the welcome text and options for the player
    typeWriter('                                     Welcome to Abendrot, a text-based experimental game.' +'\n'*4)
    titleText = """
    >     PLAY    <\n
    >     HELP    <\n
    >    CREDITS  <\n
    >     ABOUT   <\n
    >     QUIT    <
    """             
    centerText(titleText)                            
    titleScreenoptions()

#declaring a function that will print the help screen containing the command list/tutorial
def helpScreen():
    printBorder()
    helpText ="""                       
    This is the essential information needed to play the game.\n\n\n
    >                       Type your commands in the console to do them                       <\n
    >           Use "map" or examine commands + "map" to bring up the map of Sonnenau          <\n
    >                    Use "look at" or "examine" to inspect an something                    <\n
    >       Use examine words and 'around' to get a more detailed description of the area      <\n    
    >            Use "talk to" or "chat with" to start a conversation with someone             <\n
    >                   Use 'leave' or 'escape' to exit from a conversation                    <\n
    >        Use "up", "down", "left", "right" or use cardinal directions to move around       <\n
    >                           Don\'t forget to have fun! ૮ ˶ᵔ ᵕ ᵔ˶ ა                          <
    """
    centerText(helpText)
    titleScreenoptions()

#declaring a function that will print the screen containing the background behind the game
def aboutScreen():
    printBorder()
    aboutText = """                 
    This is just extra insight behind the game.\n\n\n
    Abendrot is mostly about telling a story. There's no real end goal, I just wanted to create a 
    simple text-adventure game that felt more like an experience, where you just wander around the 
    world, talk to people, interact, and learn more about things. It is definitely lacking in several 
    technical departments, but I hope it manages to entertain or amuse at the very least.
    """
    centerText(aboutText)
    titleScreenoptions()

#declaring a function that will print the credits screen
def creditScreen():
    printBorder()
    creditText = """
    These are the credits\n\n\n
    >                     Story idea and characters by Rachel Anastasia Wijaya                 <\n
    >                          ASCII art from: https://asciiart.website/                       <\n
    >                        Inspirations, tutorials, and code help from:                      <\n
    >               1. https://www.youtube.com/channel/UC5akxkiQHpxCzPZWskdBbQQ                <\n
    >                     2. https://github.com/MyreMylar/christmas_adventure                  <\n
    >              3. https://www.youtube.com/channel/UCnxsHQQIHpJw1ivDgaKp6pA                 <\n

    I am also deeply grateful to my dear friend, who will remain anonymous, 
    who helped me solidify the concept, characters, and dialogue. :D
    """
    centerText(creditText)
    titleScreenoptions()



            
def gameSetup():
    os.system('cls')
    playerName = getPlayername(myPlayer)
    #INTRODUCTION TO THE GAME
    typeWriter(f"\nYou must have many questions, {playerName}. I'm afraid I hold none of the answers you seek.\n", 0.1) 
    typeWriter("You might find them on this journey. Or perhaps not.\n")
    typeWriter("Nothing in life ever seems to come clear-cut nor unmuddled.\n")
    typeWriter("Philosophical questions and theories stimulate the mind and push us to venture beyond.\nEven if it often leads to existential crises.\n")
    typeWriter("In Sonnenau, perhaps mimesis could be attributed to old tales and legends its folk cling to dearly.\n")
    typeWriter('So come, then, Vöglein. See what you can learn in Sonnenau, from its denizens or even from nature itself.\n')
    typeWriter('Or just, wander around.\nWhatever floats your metaphorical boat, little one.\n')
    typeWriter('Tschüss und viel Glück, Vöglein...\t\t\t\t\t', 0.3)
    
    #clearing the console to signify the start of the game
    os.system('cls')
    printBorder()
    introArt=text2art("Begin...", font='georgia11')
    introBlurb = """
    You're an adventurer, hailing from Sonnenau, a coastal town tens of miles away from the mainland
    of Caelis. While being ecnomically reliant on the ocean and the nautical, Sonnenau also prides 
    itself of being the second largest hub between Caelis and Iaseon, where merchant boats dock and
    trade; passenger ships transport and ferry people, tourists, adventurers, all sorts; and where the
    annual Festival of the Seafarers is held. You're home now. Just woken up from a (deserved) 
    long-night's rest after a fairly taxing quest from Emil, the town's one and only loremaster. Emil
    probably won't mind, if you wait a while, but it might be a good idea to hand over the fruits of 
    your labor and hear the sweet, sweet clink of coins in your purse. 
    """
    centerText(introArt)
    centerText(introBlurb)
    printBorder()
    gameLoop()

printTitle()

