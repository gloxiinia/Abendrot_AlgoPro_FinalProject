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
        harbor.aliases.append('docks')
        harbor.aliases.append('bay')
        harbor.aliases.append('dock')
        harbor.aliases.append('waterfront')
        harbor.aliases.append('marina')
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
            
"""
Need more be said about the Sehnsucht Bucht? Even its name evokes the romantic, if melancholy, 
        notion of saudade. Myths, legends, and tragedies recorded and passed down through the generations. 
        The makers, or perhaps witnesses to these accounts share them with themselves, then to their 
        children, then to their own offspring, perpetuating a mimetic loop of endless collaborative ideas. 
        A little flair added here, a new player in the story added there, a change of motive. Hell, maybe 
        a different ending entirely.
        Sometimes, don't you wonder, if a tale has been repeated on and on, spread in various forms and 
        shapes, appended with details that differ from its initial telling...

        Is it still what it was originally?

"""