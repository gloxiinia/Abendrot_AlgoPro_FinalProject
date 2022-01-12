#creating the scene class


class Scene:
    #vconstructor method for the attributes of the scene class
    def __init__(self):

        self.id = ""
        self.areaName = ""

        #attributes for the scene exits
        self.north = None
        self.south = None
        self.east = None
        self.west = None

        self.is_first_visit = True

        #attributes for the game objects and npcs in a scene/location
        self.objects = []
        self.npcs = []
    
    #mutator method to update the examination text
    def setExamination(self, examineText):
        self.examination = examineText
    
    # method to add objects to the objects list
    def addObject(self, object):
        self.objects.append(object)
    
    # method to add npcs to the npcs list
    def addNPC(self, npc):
        self.npcs.append(npc)
    
    #getter method that returns a description in the form of a string
    def getDescription(self):
        return ""

    #getter method that returns an examination in the form of a string
    def getExamination(self):
        return ""
    
    def getAreaname(self):
        return self.areaName


class gameObject:
    def __init__(self):
        self.name = ""
        self.detailedDescription = "It's not much to look at."

        #attribute for other names a game object could be called
        self.aliases = []
    
    #method to add an object's alias to the alias list
    def addAlias(self, objectAlias):
        self.aliases.append(objectAlias)

class Character:
    def __init__(self):
        self.name = ""


class Player(Character):
    def __init__(self):
        super().__init__()
        self.gameOver = False
    
    def setPlayername(self, name):
        self.name = name
    
    def getName(self):
        return self.name


class Npc(Character):
    def __init__(self):
        super().__init__()

        #aliases, like nicknames or other names for an npc
        self.aliases = []

        #blurbs before initiating dialogue with an npc
        self.dialogueBlurbs = ''
        
        #dialogue ids, e.g. the player's dialogue response to the npcs in the form of dialogue
        self.dialogueResponses = []

        #dialogue texts
        self.dialogueTexts = []

        #npc backstory and profile
        self.NPCprofile = ""
    
    #method for adding npc alias to the aliases list
    def addNPCalias(self, npcAlias):
        self.aliases.append(npcAlias)
    
    #method for adding the dialogue blurbs before the dialogue choices
    def addNPCblurb(self, dialogueBlurb):
        self.dialogueBlurbs = dialogueBlurb
    
    #method for adding the dialogue responses the player can choose
    def addNPCdialogueResponse(self, dialogueResponse):
        self.dialogueResponses.append(dialogueResponse)
    
    #method for adding the dialogue texts
    def addNPCdialogueText(self, dialogueText):
        self.dialogueTexts.append(dialogueText)
    



#


