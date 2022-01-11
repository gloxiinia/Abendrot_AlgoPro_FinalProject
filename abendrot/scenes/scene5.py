'''
Setting the class for scene 5, or the Sonnenau Entrance, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene, Npc

class SceneFive(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Sonnenau Entrance"

        # setting id
        self.id = "scene5"

        # creating exits
        self.north = "scene4"
        self.south = "scene6"

        # creating objects
        statue = gameObject()
        statue.name = 'statue'
        statue.addAlias('sol statue')
        statue.addAlias('statue of sol and mani')
        statue.addAlias('mani statue')
        statue.addAlias('sol and mani statue')
        statue.detailedDescription = """
        They say Sol and Mani first emerged onto the land as the cosmos was still in its infancy, they 
        didn’t know what their powers were or what role they were meant to play in the new world.

        After the gods had created the sky, they made the Sun from molten sparks that had flown out 
        of the fiery realm of Muspelheim, and they set it in the sky to illuminate the world. For some 
        reason the gods became angry at Sol and Mani, or at their father, Mundilfari, and they took the 
        two to guide the Sun and Moon in their paths.

        Sol was forced to drive the Sun’s chariot and to guide its two horses, Arvak and Alsvinn. Sol had 
        to travel at great speed, pursued by a wolf named Skoll who would eventually devour her.

        The boy, Mani, was forced to guide the course of the Moon. He also controlled its waxing and waning. 
        Mani, too, had to travel swiftly, because the moon hound, Hati Hrodvitnisson, followed in pursuit.

        """
        self.addObject(statue)

        portullis = gameObject()
        portullis.name = 'portullis'
        portullis.addAlias('gate')
        portullis.addAlias('gates')
        portullis.addAlias('grille')
        portullis.detailedDescription ="""
        The steel is still oiled and the wood taken care of. Though, they're rarely lowered nowadays.
        Years upon years of treatises have all but made the continent of Feoyioran a safe place. 
        For the most part. Beneath the honeyed words and cloying affirmations of peace and security, 
        most folks know better.
        """
        self.addObject(portullis)

        # creating npcs
        #### FELIX ####
        felix = Npc()
        felix.name = 'felix'
        felix.addNPCalias('felix hoffmann')
        felix.NPCprofile = """
        Felix Hoffmann. Born in Sonnenau, but currently pursuing an education at the Ocrus Academia.
        Majoring in Astromancy, they're well versed in the stars, their magic, and what stories they tell
        with their constellations. They're a bit of a bibliophile. 
        
        Okay, maybe not 'a bit', just slightly less than Emil.

        They've returned to Sonnenau for their year-end break. A brief respite from the countless and 
        non-stop work environment at the academy.
        """
        self.addNPC(felix)

        #FELIX DIALOGUE 1
        felixBlurb = """
        Felix seems intent on their book. Even as you near them, he doesn't even bat an eye in your direction,
        glued firmly to the thrilling words written on his book.
        """

        felix.addNPCblurb(felixBlurb)

        felixDialogue1 = """
        It takes a couple tries, but on the fifth or so time you call their name they finally 
        deign you worthy of their presence.

        "You better have a good reason for interrupting my free time," they say, waving the book--a 
        Romance title, In the Fields of the Red Camellias--in a dramatic, annoyed flourish.

        Prickly as ever, then. Never change Felix, never change.

        "Where's Jules?"

        "Probably where he always is, wait, why are you asking me?"

        "I dunno, making small talk?"

        That earns you a scoff.

        "C'mon don't be like that, aren't I your one and only reading buddy?"

        That earns you an exasperated sigh.
        You can already feel Felix rolling their eyes before they even do so.

        "Don't call me buddy, ever again. Please. Eugh." You can already feel Felix rolling their eyes 
        before they even do so. "Besides, Emil listens to me too." 

        "At least when it's not about romance novels," they add, under their breath.

        "Now excuse me, if you're done distracting me from my reading, with your inane questions," and 
        without another word, they turn back to their book.

        Well, that's that you guess.
        """

        felix.addNPCdialogueText(felixDialogue1)
        felix.addNPCdialogueResponse("“Feliiiix.”")
    
    def getDescription(self):
        description = """
        Before entering the coastal town of Sonnenau, visitors are greeted with a statue of Sól and 
        Máni, in their chariots, regal against the backdrop of the Sehnsucht Bucht, or Bay of Longing.
        Walking further in, they'd see the portcullis signifying entry into Sonnenau proper. The walls 
        still stand, even after countless years have passed. Used back then to protect against possible 
        assaults to the city. But that was then, and this is now.
        """

        return description

    def getExamination(self):
        examination = """
        Looking around, other than the eye-catching statue, you can see someone loitering near the rear 
        portcullis. Ah. It's Felix. They're nose deep in a book, though they still have enough sensibility 
        to wave at any odd passerby that greet them.
        """
        return examination
        
