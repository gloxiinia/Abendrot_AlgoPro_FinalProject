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
        The trees rise up, up, up until barely any light passes through them. To say they're dense and overgrown would be an understatement.
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

        #### NICO DIALOGUE ####
        nicoBlurb = """
        "Not many venture into the forest nowadays, but you’re a particularly stubborn one, are you not, Vöglein?" 

        He always talks like this. Condescending, holier-than-thou tone, it gets grating sometimes…But, he is a treasure 
        trove of information regarding the forest, especially the ancient stuff. You asked him, how come he knows all 
        that knowledge about the past. The bygone era where nature ran its course, flourishing and in some cases, with 
        the expense of civilization. 

        Like a certain other someone (really, they're practically twins) he just flashed an irritatingly comely 
        smile and left it at that. What is it with people and dancing around questions like it's the plague?

        As elusive as he is, he's here now. And who knows, maybe he's in a more sharing mood.
        """

        nico.addNPCblurb(nicoBlurb)

        nicoDialogue1 = """
        “Mhm. I felt as though you’d be passing by here today.”

        “Really? Now you’re adding future vision to your already extensive list of expertise?”

        Though, less you're pretty sure it's less future vision and more "I'm friends with the two people 
        who live out here in the woods".

        “I’m no sage, but I know of something called foresight, perhaps you should try using that sometimes, little one.”

        The nerve. 

        Julian would probably say something smart right about now, but since he's not here…

        "That's rich coming from someone who always forgets where they put their glasses."

        …

        Even without seeing Nico's deadpan face you know that was a particularly weak jab. 
        It takes a lot to make him express anything other than subtle amusement or calm elegance. The amount of 
        times you've seen him laugh freely can be counted on one hand. Once was when the three of you went to 
        the annual snow festival in Iaseon. He'd looked so enchanted when he saw the ice sculptures and snowmen. 

        "Sorry, that was petty. And stupid."

        "Do not worry, no harm done, playername."

        That's… off. Nico rarely accepts an apology so easily.

        After a short moment of silence, he speaks up.

        "Off to see Julian?"

        That kicks your brain back into gear.

        "Hmm? Oh. Uh, no actually. Emil told me to meet in Jules' garden. I'm handing over his commission for me."
        He hums noncommittally at this. 
        "Well then, I wouldn't want to keep you waiting, Vöglein. Go on, now."

        That's… really off.
        He never lets you go on your way before going on a tirade about an old city or legend.

        But you're not one to look a gift horse in the mouth. You just want to get your payment, clean and simple. 
        Maybe you'll seek him out some other time as recompense, you almost feel bad for not listening to a story of his. 
        Because for as long as they can get, the stories he chooses are always fascinating. 
        
        Maybe it's the way he tells them, as though he's lived through these events himself. 
        But, no, he's from Sonnenau, born and bred, your childhood friend. 
        Unless someone switched places with him… well that's a thought you didn't think you'd be having. 
        That's enough theorizing for today.

        You say your farewells and he waves you off.
        """

        nico.addNPCdialogueText(nicoDialogue1)
        nico.addNPCdialogueResponse("“Finally came out to play, have you?”")
        

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

        But amidst that calm, you swear you can hear rustling in the trees. 
        """
        return examination        
