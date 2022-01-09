'''
Setting the class for scene 11, or the Meeresarm der Begehrlichen, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene, Npc


class SceneEleven(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Meeresarm der Begehrlichen"

        # setting id
        self.id = "scene11"

        # creating exits
        self.north = "scene10"
        self.west = 'scene6'

        # creating objects
        sunset = gameObject()
        sunset.name = 'sunset'
        sunset.addAlias('setting sun')
        sunset.addAlias('red sun')
        sunset.detailedDescription = """
        
        """
        self.addObject(sunset)

        shore = gameObject()
        shore.name = 'shore'
        shore.addAlias('beach')
        shore.addAlias('strand')
        shore.addAlias('sand')
        shore.addAlias('sands')
        shore.addAlias('shoreline')
        shore.addAlias('seashore')
        shore.detailedDescription = """
        
        """
        self.addObject(shore)

        # creating npcs
        #### JULIAN ####
        julian = Npc()
        julian.name = 'julian'
        julian.addNPCalias('jules')
        julian.NPCprofile = """
        
        """
        self.addNPC(julian)

        julianBlurb = """
        You see Julian sitting on the sand, closer to the rippling waves than dry land. He's facing the sunset. 
        But as he hears the soft, but audible crunch of footsteps on sand, he turns.
        """

        julian.addNPCblurb(julianBlurb)

        julianDialogueText1 = """
        His silhouette, against the still lit sky, creates a chiaroscuro as vivid as one would see in an 
        artist's meticulously crafted masterpiece.

        With a smile as bright as the rays that shadow his face, he says:

        "Oh. playername. I've been waiting for you. Come, take a seat."

        """

        julian.addNPCdialogueText(julianDialogueText1)
        julian.addNPCdialogueResponse("“Jules? Hey.”")



        
    def getDescription(self):
        description = """
        The Meeresarm der Begehrlichen, another name for the Inlet of the Desiring. A secluded 
        inlet that connects to the Sehnsucht Bucht to the east. It's just a short stroll from 
        Julian's abode, which is why while not fully private from prying eyes, it's become your 
        go-to place to meet and hang out with Julian. Also, the name certainly invokes some vivid 
        imagery. Surely there's a story behind it?
        """

        return description

    def getExamination(self):
        examination = """
        Somehow, every time you visit this tiny little inlet, it always manages to stun you to 
        silence. You attribute it to a spell the inlet puts visitors under, but Julian--more 
        attuned to magic than you are--denies it. This time is no different. It looks, for lack of 
        a better or more eloquent word, stunning. The way the sun meets with the sea's horizon, 
        reflecting and refracting back and forth like a stroke of a paint brush. 

        The afterglow.

        Oh? You can just roughly make out Julian's figure on the distance.
        """
        return examination