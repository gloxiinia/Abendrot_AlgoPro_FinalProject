'''
Setting the class for scene 7, or the Forest Entrance, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene

class SceneSeven(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Forest Entrance"

        # setting id
        self.id = "scene7"

        # creating exits
        self.east = 'scene8'
        self.west = 'scene4'

        # creating objects
        gate = gameObject()
        gate.name = 'gate'
        gate.addAlias('gates')
        gate.addAlias('old gate')
        gate.addAlias('old gates')
        gate.addAlias('entrance')
        gate.detailedDescription = """
        These gates must be as old as Sonnenau is. It still looks functional, but just barely.
        The rust still shows, the vegetation practically strangling the grills and lattices.
        """
        self.addObject(gate)

        plaque = gameObject()
        plaque.name = 'plaque'
        plaque.detailedDescription = """
        There's text written on the plaque, two rows. The first row reads: "Hain der Waldkäuze",
        and the second: "Where the tawny owls make their homes, apart from their other brethren."
        Huh, intriguing.
        """
        self.addObject(plaque)

    def getDescription(self):
        description = """
        The entrance to the Hain der Waldkäuze. The final frontier between the woods and the 
        town of Sonnenau."""

        return description

    def getExamination(self):
        examination = """
        A time-worn plaque engraved with a figure of a tawny owl can be seen near the gates. 
        Moss, vines, and all sorts of plants wrap around the dilapidated steel gates. There's
        no one here.
        """
        return examination
                
