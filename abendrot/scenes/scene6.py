'''
Setting the class for scene 6, or the Sehsucht Bucht, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene

class SceneSix(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Sehnsucht Bucht"

        # setting id
        self.id = "scene6"

        # creating exits
        self.north = "scene5"
        self.east = 'scene11'

        # creating objects
        harbor = gameObject()
        harbor.name = 'harbor'
        harbor.addAlias('docks')
        harbor.addAlias('bay')
        harbor.addAlias('dock')
        harbor.addAlias('waterfront')
        harbor.addAlias('marina')
        harbor.detailedDescription = """
        The harbor is where the magic happens for most people. Stepping off the gangway of any ship, finally
        setting foot in Sonnenau's docks and getting a glimpse of the statues in the distant entryway.
        """
        self.addObject(harbor)

        sunset = gameObject()
        sunset.name = 'sunset'
        sunset.addAlias('settingsun')
        sunset.addAlias('redsun')
        sunset.detailedDescription = """
        People like to wax poetic about the beauty and transient feeling viewing a sunset can give you.
        While you're sure most books exaggerate and dramatize these scenes with flowery words , at its core, it 
        still shows how much of a struggle it is to be able to reflect what a person can feel in the moment into 
        the written word and not make it end up as a word salad for synonyms of 'beautiful'.  But yes, to cut the
        pondering short, it's beautiful.
        """
        self.addObject(sunset)



    def getDescription(self):
        description = """
        The Bay of Longing, or the Sehnsucht Bucht as the locals call it. Housing the harbor from 
        which ships and vessels come and go from Sonnenau, it holds a special, not to mention important 
        place in Sonnenau citizens' hearts (and source of income).
        """
        return description

    def getExamination(self):
        examination = """
        You're standing in the marina, looking towards the horizon. There, the sun is descending into the
        ocean depths, gracing those who are lucky enough with a spectacle of colors. Orange, red, pink, purple
        blend with each other to create scenery as bewitching as a siren's lull. Like accents on a living 
        tapestry woven by nature, fishing and commercial boats come and go from the docks at random intervals.
        """
        return examination
