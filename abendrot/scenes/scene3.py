'''
Setting the class for scene 3, or the Sonnenau Plaza, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene, Npc

class SceneThree(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Sonnenau Plaza"

        # setting id
        self.id = "scene3"

        # creating exits
        self.south = "scene4"
        self.west = 'scene2'

        # creating objects
        fountain = gameObject()
        fountain.name = 'fountain'
        fountain.addAlias('fount')
        fountain.detailedDescription = """
        The Sonnenau Plaza fountain. It sits in the middle of the plaza and serves as a place
        for people to throw their coins down the drain. In return, they receive the unfounded
        notion that whatever they wished for will come true and of course, served with a side of
        what they call 'the cold embrace of disappointment'.
        """
        self.addObject(fountain)

        # creating npcs
        ingrid = Npc()
        ingrid.name = 'ingrid'
        ingrid.addNPCalias('inna')
        ingrid.addNPCalias('ingrid and korvin') 
        ingrid.addNPCalias('korvin and ingrid')
        ingrid.NPCprofile = """
        Ingrid Leitz. Known amongst the adventurers as "Aren" or the eagle, she made a name for 
        herself when she took up a request to uncover the ancient city of Osse, which at that point,
        was still thought to be lost to time, destroyed through war and natural phenomena. Suffice it
        to say, Ingrid is not one to back down from a challenge, especially one that could be her big 
        debut in the adventuring scene. And after months of leading her crew and exploring the forests
        where Osse was speculated to be in, she'd finally succeeded. 
        """
        self.addNPC(ingrid)

        korvin = Npc()
        korvin.name = 'korvin'
        korvin.NPCprofile = """
        Korvin, no last name. Moved to Sonnenau because of rough times. He doesn't divulge much about his
        past, never talks about his family either. Just said he left because shit hit the fan back in 
        Mugen no Tochi. Iaseon politics and whatnot. It was difficult, in the early days, but he finally
        found his footing by opening up a general store. Cheap prices (how does he do it?) and with an
        almost excessive amount of variety to boot. And with that, his store's basically become the go-to 
        supplier for any adventurer and expedition crew. 
        
        Plus, he feigns ignorance, but friends get a bit of a discount.

        So, through his supplying of provisions and equipment, he met Ingrid. His now partner for 8 years.
        No plans for marriage, but they're happy enough together.
        """
        self.addNPC(korvin)

        #INGRID AND KORVIN DIALOGUE
        ingridBlurb = """
        The couple don’t seem to notice you at all, it seems like they’re deeply embroiled in an argument 
        about whether the Traitor of the Stars trilogy ended well or poorly. Wow. 

        Well, at least it’s a harmless quarrel… right?
        """
        ingrid.addNPCblurb(ingridBlurb)
        ingrid.dialogueText1 = """
        They ignore your greeting.

        “I told you so many times already, Inna,” Korvin says, inflections more evident as his Iaseon accent 
        bleeds into his voice. Ingrid says nothing for a moment, arms still crossed and looking at anywhere but Korvin.

        Then she retorts, “That ending is perfect, K. 
        The way Matthieu gets his comeuppance for all the shit he did in book 1,” ending with a scoff. 

        Korvin is rubbing circles on his temples. Taking a deep breath, he says, 
        “Then what was book 2 for then? All that time spent with him, seeing him grow and mature and actually do good now? 
        For what?” 
        
        He looks so forlorn over this fact that it’s hard not to pity him.

        “Realism. That’s what.”

        “But it’s fantasy Inna. Fan-ta-sy.”

        “Yeah, but—“

        “Ugh, this is why you should just stick to your adventurer guides or whatnot.”

        “Fine, I will. Just don’t mope when you can’t find anyone else to listen to your fanboying.”

        “FELIX LISTENS,” Korvin shouts out, earning them a few turned heads and glares.

        Both of them don’t seem to care though, with Ingrid barreling on.

        “Felix doesn’t count, they practically live and breathe books, there’s nothing they won’t 
        listen to if it involves the word ‘book’ or ‘literature’.”

        …

        Oh boy.

        Better leave this conversation be.
        """
        ingrid.addNPCdialogueText(ingrid.dialogueText1)
        ingrid.addNPCdialogueResponse("“Hey guys. What's up?”")

        

    def getDescription(self):
        description = """
        Sonnenau's town centre, it's no surprise that it's packed full with merchants, vendors, 
        adventurers, and a myriad of other eccentric people from all walks of life. Here is where 
        the people of Sonnenau celebrate festivities and grand things. Perhaps it's the new moon, 
        or maybe the seasonal constellations have deigned to grace the citizens with their celestial 
        glory and light. Scorpius and Orion's eternal game of hide and seek, Corvus' idle complacency 
        which it paid the price with its snow-white feathers, or Aquila, as a means entangled in the 
        love life of gods' and goddesses of primordial legend. 

        Whichever event, you can bet that it'll be held in the plaza.
        """

        return description
    
    def getExamination(self):
        examination = """
        The Sonnenau plaza is just as it always is. Loud and busy, the place where Sonnenau's citizens
        and visitors converge. The fountain's still the same as ever, water bubbling and dancing as 
        people mill about. Though, on its edge, you can see Korvin and Ingrid chatting. 

        You're not close enough to make out what they're talking about clearly.
        """

        return examination
        
