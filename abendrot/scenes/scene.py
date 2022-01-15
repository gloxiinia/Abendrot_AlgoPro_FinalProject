#creating the scene class
class Scene:
    #constructor method for the attributes of the scene class
    def __init__(self):
        #attribute to identify the scene/location
        self.id = ""

        #attribute to store a scene/location/area's name
        self.areaName = ""

        #attributes for the scene exits
        self.north = None
        self.south = None
        self.east = None
        self.west = None

        #attributes for the game objects and npcs in a scene/location
        self.objects = []
        self.npcs = []
    
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
    
    #getter method that returns the area name
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


#creating the character class
class Character:
    def __init__(self):
        self.name = ""

#creating the playable character subclass
class Player(Character):
    def __init__(self):
        super().__init__()
        self.gameOver = False
    
    def setPlayername(self, name):
        self.name = name

#creating the npc subclass
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
    


