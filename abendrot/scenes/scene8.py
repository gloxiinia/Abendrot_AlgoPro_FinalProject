'''
Setting the class for scene 8, or the Hain der Waldkaeuze, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene, Npc

class SceneEight(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Hain der Waldkäuze"

        # setting id
        self.id = "scene8"

        # creating exits
        self.east = "scene9"
        self.west = 'scene7'

        # creating objects
        trees = gameObject()
        trees.name = 'trees'
        trees.addAlias('forest')
        trees.addAlias('woods')
        trees.addAlias('thicket')
        trees.addAlias('grove')
        trees.detailedDescription = """
        
        """
        self.addObject(trees)

        # creating npcs
        nico = Npc()
        nico.name = 'nico'
        nico.addNPCalias("nicolas")
        nico.NPCprofile = """
        Nico, nico, nico. Esoteric, likes hanging out in the creepy forest, but has charisma and charm
        in droves, so it mostly makes up for the first two points with the last. Has a history with Julian. How far
        back their acquaintance goes, you don't know. Neither have expressed interest in talking about the past,
        far more interested in the present. Whatever happened, it didn't sour their relationship, so you feel it's
        best to leave it at that.
        
        He lives... somewhere in the forest? 
        You're sure he's said where he lives, even taken you and Julian there a couple of times, but everytime you 
        try to remember, you always forget. Julian always seems to know the way though. Maybe they have a sort of
        arrangement you don't know about. Hmph, cryptic bastards.

        Few know about him, seeing as he rarely shows himself in town. Only appearing when every other major festival 
        is being held or when a new year arrives. 
        """
        self.addNPC(nico)

    def getDescription(self):
        description = """
        Though not dangerous, there is a feeling of eeriness that washes over whenever someone 
        enters the Hain der Waldkäuze. 

        But what lies beyond is… well, you'll have to see yourself.
        
        (It's Julian's Cottage.)
        """

        return description

    def getExamination(self):
        examination = """
        Hain der Waldkäuze... Forest of the Tawny owls, elusive creatures that call these woods home. 
        Rarely seen, even at night when they're most active. Their hooting, combined with the 
        ambiance of the dense, near-lightless canopies is enough to give anyone shivers. But, the forest
        itself, looking past the general creepiness, is calm. So, very calm.
        """
        return examination        
