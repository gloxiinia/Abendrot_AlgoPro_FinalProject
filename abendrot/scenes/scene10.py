'''
Setting the class for scene 10, or Julian's Garden, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene, Npc

class SceneTen(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Julian's Garden"

        # setting id
        self.id = "scene10"

        # creating exits
        self.north = 'scene9'
        self.south = "scene11"

        # creating objects
        wisteria = gameObject()
        wisteria.name = 'wisteria'
        wisteria.addAlias('wisteria tree')
        wisteria.addAlias('wisteria tree')
        wisteria.addAlias('big tree')
        wisteria.addAlias('massive tree')
        wisteria.addAlias('huge tree')
        wisteria.addAlias('big wisteria tree')
        wisteria.detailedDescription = """
        First introduced Caelis around a hundred years ago, sought after for it's simple, but 
        effective beauty as ornamental plants. You recall reading a cultivar's guide from Julian 
        once--deciding to help the man out with some of his gardening--that they can latch onto 
        lattices, woodworks, and walls with a vice-like grip. Fast growing, but a late bloomer 
        this one, he'd said, cradling a patch of wisteria flowers in his hand.
        """
        self.addObject(wisteria)

        gazebo = gameObject()
        gazebo.name = 'gazebo'
        gazebo.detailedDescription = """
        A gazebo. It's nothing *too* fancy. Nicely constructed, and oh. Emil is there. His writing
        set is splayed out on the table haphazardly and he seems to be fervently jotting down notes, 
        scripts, and other details. About what, you wonder?
        """
        self.addObject(gazebo)

        # creating npcs
        #### EMIL ####
        emil = Npc()
        emil.name = 'emil'
        emil.addNPCalias('loremaster')
        emil.addNPCalias('lorekeeper')
        emil.addNPCalias('von berger')
        emil.NPCprofile = """
        Emil von Berger, resident loremaster of Sonnenau. Outgoing and quite lax, even considering
        his occupation, preferring a more hands-on and practical approach to documenting the goings-on
        of Sonnenau. This usually results in his poor papers and notes falling victim to the elements:
        rain drops, dirt smears, and the like.

        Nevertheless, he takes pride in his work. You can see it reflected in the documents stored in
        the Sonnenau Library. Each one written with a deep passion and respect for the history, present, 
        and future of Sonnenau.
        """
        self.addNPC(emil)

        #EMIL DIALOGUE 1
        emilBlurb = """
        Even as you step onto the gazebo and take a seat next to him, Emil is still intensely focused on 
        his writing. He sets a frenetic pace, eyes flicking through papers, books and hands in a nonstop 
        rush to write out the words on his mind.
        """
        emil.addNPCblurb(emilBlurb)

        emilDialogue1 = """
        Your greeting finally breaks him out of his trance. Partially. He's facing you, yet his hands are 
        somehow still writing proper words and sentences. How…?

        "Oh! playername! Didn't see you there, what do you need?"

        "Well, I've got the *thing* you hired me to get."

        Emil's hands come to a stop. Apparently that catches his full attention.

        "Well then! Where is it???" Emil's expression has taken on the visage of a dog expectantly awaiting a treat. 
        
        How adorable.

        You take out the scroll from your bag and place it on the table. Emil immediately opens its up clearly 
        disregarding the principle of pay before you frantically unfurl and read over the thousand year old scroll you 
        employed an adventurer to painstakingly find.

        Though, when his eyes get starry-eyed and he looks this delighted… it's difficult to stop him 
        (well, that's if you even wanted to).

        After a good few minutes, he finally remembers your pay. Taking out his coin purse and dropping
        20–count em, yes, 20–gold pieces onto the table. You gladly pick them up and store them into your 
        own coin purse. Ah. Shaking it a bit to confirm, you can audibly hear the jingle of the coins. 

        "Thank you, I'll definitely be commissioning you for more of these fetch quests."

        "I'll be looking forward to that." And the payment, your mind truthfully and dutifully supplies.

        Before you leave, you almost forget to ask.

        "Hey, uh, Emil?" Lucky for you, Emil isn't fully lost to the temptation of deciphering ancient text just yet.

        "Hmm?" He says, looking up from the scroll.

        "Have you seen Julian? He… isn't in his cottage and uh.. since you're in the garden, maybe you've seen him?"

        "Ah, Jules told me he'd be at the Meeresarm."

        "I see." Weird, Julian usually gives you a heads-up before setting up a meeting.

        "Did he not tell you?"

        "No, or... at least I don't remember making any plans with him. Ah, maybe it just slipped my mind."
        
        That's probably it. It's happened before, anyways.

        "In any case, thanks Emil." You make to leave and wave him goodbye.

        Emil ignores it, already too engrossed in his work.

        """

        emil.addNPCdialogueText(emilDialogue1)
        emil.addNPCdialogueResponse("“Emil, it's me.”")

    def getDescription(self):
        description = """
        Jules's garden. He says he grows herbs and medicinal plants here, but sometimes he comes
        over with the occasional decorative and perfume-y flowers. You remember lavenders, roses, 
        and even some wisteria flowers among them. 
        """

        return description

    def getExamination(self):
        examination = """
        Julian might say his cottage is modest, but one look at his garden proves otherwise. This 
        'garden' is practically an orchard, housing flora from all reaches of Feoyioran. Medicinal, 
        horticultural, ornamental, you name it, it's probably there in Jules' garden. Despite the 
        astounding variety, one stands out. The wisterias. Or rather, the massive wisteria tree in 
        the far east of the garden. 
        
        With all his talk of living a frugal life, Julian has managed to craft such an elegantly 
        hidden paradise within his domain. There's a babbling brook, with water as clear as glass 
        and a pearl-white gazebo constructed from painted hardwood stands beneath the boughs of the 
        wisteria tree, flowers draping over and around its roof. 
        """
        return examination
