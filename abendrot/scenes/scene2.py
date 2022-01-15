'''
Setting the class for scene 2, or the Vagabond's Folly, inherited from the scene class.

'''


from scenes.scene import Scene, gameObject, Npc


class SceneTwo(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Vagabond's Folly"

        # setting id
        self.id = "scene2"

        # creating exits
        self.north = "scene1"
        self.east = 'scene3'
        

        # creating objects
        bar = gameObject()
        bar.name = 'bar'
        bar.addAlias('counter')
        bar.detailedDescription = """
        The main attraction of the Vagabond's Folly. No less rowdy than usual. Michel is
        serving a variety of drinks to the patrons, the patrons accept, and after a cheer--
        They drink.
        """
        self.addObject(bar)

        ballad = gameObject()
        ballad.name = 'ballad'
        ballad.addAlias('tale')
        ballad.addAlias('story')
        ballad.addAlias('tune')
        ballad.addAlias('song')
        ballad.detailedDescription = """
        The ballad tells of the story of a fisherman from the islands of Iaseon, who by saving a 
        turtle, gains him the gratitude from Otohime, the undersea princess. After a while spent in 
        the sea palace,  the man is homesick and longs to return to his village. Otohime reluctantly 
        lets him go with a parting gift, in the form of a box called the tamatebako, whose lid the man 
        was told to never open under any condition. It ends on a rather depressing note, with the 
        fisherman arriving in his hometown and it is revealed that, due to time passing, all the people 
        he knew, his mother, his father, had perished. Forgetting the princess; warning, he lifted the 
        box's lid, and after a puff of smoke, turned him into an elderly man.
        """
        self.addObject(ballad)

        # creating npcs
        
        #### MICHEL ####
        michel = Npc()
        michel.name = 'michel'
        michel.addNPCalias('michel kopp')
        michel.addNPCalias('kopp')
        michel.NPCprofile = """
        Good old Michel Kopp, owner and full-time barkeep at the Vagabond's Folly. In the short time 
        since its founding 30 rough years ago, he's managed to make a name for himself and this bar. 
        Starting out as a small, cozy tavern, then periodically becoming this grand affair, with 
        reconstructions and added rooms and new facilities. As for the man himself...he hails from 
        Hull, a mining town in the mainland of Caelis. Frankly, Michel never had the stomach nor strength 
        for mining and all the dirty work that came with it, so he turned to businesses, and finally 
        settled on opening up a bar in ol' Sonnenau.
        """
        self.addNPC(michel)

        #MICHEL DIALOGUE CHOICE 1

        michelBlurb = """
        Seeing you, Michel wraps up the small talk with the already woozy patrons at the bar and by the
        time you approach, he’s ready with his usual line of  “What can I get you?”
        """
        michel.addNPCblurb(michelBlurb)
        
        michelDialogue1 = """
        “I thought day-drinking wasn't your MO, but I guess everyone’s got their days.”

        “Is it really day-drinking if the sun’s practically gone already?”

        “Fair enough,” he says with a small laugh.
        """
        michel.addNPCdialogueText(michelDialogue1) 
        '''
          .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.      .--.      .-'.      .--.       .--.   
        :::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\:::::::::.\:::  
               `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `--'      `--'      `.-'      `-.-'      `-  
        '''
        #MICHEL DIALOGUE CHOICE 2
        michelDialogue2 = """
        “Oho, feeling adventurous today aren’t you?”

        “It comes with the job.”

        A laugh, no–a cackle bursts out of Michel. How does he seemingly find the most low-bar jokes funny? 
        Maybe there’s something to be said about jobs and personalities.

        As you ponder on, Michel collects the needed ingredients for your order. At one point, he even goes 
        to the pantry to take a fruit that looks like an orange, but has more of a pale yellow coloring. 
        Mixing in the whiskey and pouring drops of… soy sauce? And finally garnishing with a star anise. 
        You just hope he didn’t add any other ‘surprise’ ingredients.

        He pushes the glass towards you with a grin on his face. “Drink up.”

        “Should I be worried?”

        “It’s completely safe, I swear.”

        “Really? Last time you said that I remember Felix throwing up for about 6 hours before Julian came back.”

        “That was…a more experimental concoction,” he says, with nary a look of remorse, you can even hear a bit of 
        pride from how he says the sentence. “Besides, didn’t you say ‘surprise me’?”

        You sigh. “I guess I kinda dug my own grave then huh?”

        Michel just shrugs, and with a triumphant grin, motions toward the lowball glass containing the cocktail.

        Whether it was bravery or surrender, you take a generous sip of the cocktail. Sour. It’s sour, and you manage
        to not spit it out and avoid full indecorum, but you fail to contain the way your face twists as the sour 
        taste digs its claws on your tongue. Though… the aftertaste isn’t quite so bad. You dare say it’s decent. 
        You’ll most likely never order it again, but compared to the Felix incident, this is definitely the lesser of two evils.
        """
        
        michel.addNPCdialogueText(michelDialogue2) 

        #MICHEL DIALOGUE CHOICE 3
        michelDialogue3 = """
        “Ah, I see. Alright then, One pick-me-up, coming up.” 

        With a sympathizing look, Michel swiftly picks out a couple of ingredients, Bergamot, gin, and lavender. 
        An interesting blend, but not one you’ve tried before. Michel brews the tea, adds the gin, and finishes by 
        dipping a lavender into the glass. 
        
        “Hope this cheers you up, uh...cheers.” Michel takes a swig out of a flask.

        “Cheers.” 
        
        Maybe it’s just the caffeine, but downing that drink has made the fatigue lessen, if only marginally.
        """
        michel.addNPCdialogueText(michelDialogue2)

        michel.addNPCdialogueResponse('“The usual.”')
        michel.addNPCdialogueResponse("“Give me something new, I feel like I need a bit of a surprise right now.”")
        michel.addNPCdialogueResponse("“A pick-me-up.”")
        


        #### PETRA ####
        petra = Npc()
        petra.name = "petra"
        petra.NPCprofile = """
        If you need an outfit tailor-made in perfection, bring the right materials and go over to
        Petra's. As Sonnenau's resident seamstress, she can stitch the scarves, sweaters, socks 
        (and other types of clothing) of your dreams. This is on account of her weaving magic into 
        all her designs and handiwork.
         
        Though, don't say that to her face, it's a... touchy subject for her. 
        """
        
        self.addNPC(petra)

        #PETRA DIALOGUE CHOICE 1

        petraBlurb = """
        Seeing you, Petra waves you over with an almost manic joy. Judging by the slightly slurred 
        speech and her general air of floatiness, she’s probably had a couple of drinks, maybe more honestly.
        """
        petra.addNPCblurb(petraBlurb)

        petraDialogue1 = """
        Though she slightly slurs the words, it’s still understandable. 

        """
        petra.addNPCdialogueText(petraDialogue1)

        petra.addNPCdialogueResponse("“Work done for today?”")


        #### FERDINAND ####
        bard = Npc()
        bard.name = 'ferdinand'
        bard.addNPCalias('bard')
        bard.addNPCalias('the bard')
        bard.addNPCalias('balladeer')
        bard.addNPCalias('troubadour')
        bard.addNPCalias('ferdie')
        bard.addNPCalias('von albrecht')
        bard.NPCprofile = """
        Ferdinand von Albrecht, known to his many, many friends as Ferdie. Care-free and with lute in hand,
        he is a bard. Or, as he'd put it: "A maestro travelling the land, in search of inspiration for his magnum opus." 
        
        But yes, he's a bard. 
        
        Rumors on the grapevine about him are as exaggerated and fantastical as the songs and stories 
        he regales his audience. One claims that the von Albrecht family disowned him for involvement 
        with revolutionaries back in Eschenroden. Another alleges that his von Albrecht name is just a 
        front, that he's the last remaining member of a ruined clan, back from the olden days. 

        Whether these rumors hold any water, it's hard to tell, what with Ferdinand's insistence on 
        the fog of mystery, dismissing the rumors with indifference and added with the lack of 
        information that gets in or out of Eschenroden.
        """
        self.addNPC(bard)

        #FERDINAND DIALOGUE CHOICE 1

        bardBlurb = """
        His performance finished and on break, you find yourself walking towards the bard. You’ve heard talk 
        about a new balladeer that came to town a couple weeks ago. 
        
        Maybe it’s time to find out more about this mysterious person.
        
        He sees you come close and his lips quirk into an easygoing smile. 
        
        “To what do I owe the pleasure?”, the bard teases, a playful lilt to his already melodic voice. 
        """
        bard.addNPCblurb(bardBlurb)
        
        bardDialogue1 = """
        Chuckling, he replies, “Well, do you see any other bards or troubadours about, friend?”

        “I guess not, aha.”

        “In any case, yes, I am in fact the bard in question.” He places a hand on his chest, and with a flourish, 
        takes your hand and kisses it.

        And who said chivalry was dead?

        “Wow. Uh…” 

        Again, the bard crows in that melodic voice of his. “Starstruck? Please, don't be. Relax, I was just 
        being polite," he says, lips quirked up into a sophisticated smile that feels practiced to a fault.

        Your brain can’t catch a break. 

        Finally getting ahold of yourself, you reply, "Right. I'm uh.. playername."

        "Glad to make your acquaintance, playername. Ferdinand von Albrecht, in the flesh." He bows, regal and proper. 
        "But you can call me Ferdie, if you'd like."

        Calling a stranger by a nickname feels far too intimate for a first meeting but, he did say you could. 
        But, not today.

        "So, uh, Ferdinand. What do you think of Sonnenau?"

        "It's been wonderful, so far. The people are nice, and open. But, surely you have some more… colorful 
        questions you'd like to ask? Pertaining my origins perhaps?"

        Now his smile contorts into a smirk, like a cat who got the cream, self-satisfied and teasing.

        "Well, when you put it like that…"

        "Truly, I don't mind. People are going to talk either way." Slouching further into his seat, he really 
        does look like a cat, with his languid movements and coy mien.

        "So, what would you like to know? I’m in a charitable modd, so pick your poison. I know how eager the 
        rumor mill is to eat up anything and everything that is remotely scandalous."

        "Are they true?"
        “You’re going to have to elaborate more on that. These rumors can go from claiming I’m a land-born siren–” 

        “To their credit, your voice is bewitching, to say the least.”

        “You’re too kind, really. But yes, seeing as they name me a siren in one and a wronged noble from a bygone 
        age in another you *will* need to clarify, dear.”

        Thinking it over, you decide to start small.

        "You're really from Eschenroden?"

        “Oh, Eschenroden. It’s been a while since I’ve talked about it, but yes”–he nods–“ I do come from Eschenroden.”

        “Why leave?”

        “I felt that I could do no service to my homeland and with all the growing unrest… I took the opportunity to 
        extricate myself from the drama.”

        “So it’s true, then? Eschenroden really is in the middle of a revolution?”

        “I wouldn’t call it *in the middle* of one, rather… the foundation for one is being laid, and I’d prefer to 
        not be embroiled in any farcical attempts the government calls politics.”

        "Would that have anything to do with your house?"

        “Ah, right. My house.”

        “Truth be told… No.”

        “My parents didn’t disown me, I had no dealings with the revolutionists, yet… I felt as though I lacked something.”

        “Wanderlust took over and one day, I… I just followed the urge and left.”

        “The von Albrechts are a rather small, but impactful family, so, much to my chagrin, rumors flocked to 
        me like moths to a flame.”

        “But I don’t blame the people, they need a bit of entertainment now and then. And who am I to decline such a calling?”

        I had nothing to say to that. 
        
        But he urges me on, “This is all water under the bridge for me, please, I learned that it’s much more liberating 
        to talk it out with someone, anyone, so don’t hesitate to ask more.”

        “I see. I guess I have one last question. Why come to Sonnenau?”

        “That’s a particularly easy one to answer. It's history.”

        “Once, I’d visited Sonnenau with my family, and its past enchanted me.”

        He picks up his lute, starting to strum a gentle tune, singing in a slow, melancholic tone.

        The song regales the story of which the Sehnsucht Bucht got its name:

        Named after a tale in which it was said that long ago, when people first settled and the name Sonnenau was 
        newborn and just starting to be memorized, there was a man who came from the southern islands. Painter, he was.
        Born noble, but as 3rd in the line of succession, he was free to do whatever he wanted. Due to circumstance, the 
        accounts vary, but most cite familial obligations, he was forced to leave his lover and move to where Sonnenau now 
        stands. And so, faced with a possible lifelong separation, he drew two paintings, one of himself, and the other 
        of his lover, respectively given to the person not depicted in them.

        And with that, the song ends.

        “No ending?”

        “I want to encourage my listeners to come up with their own interpretation. Oh, and that's my cue. This was fun,
        let's talk again, playername." 
        He waves a quick goodbye and returns to the stage.
        """

        bard.addNPCdialogueText(bardDialogue1)
        bard.addNPCdialogueResponse("“Are you the newcomer everyone’s been talking about?”")



    def getDescription(self):
        description = """
        Ah, the sweet, tangy smell of alcohol and desperation. Nothing else really comes close to 
        the rush of when you enter Sonnenau's famous (or infamous depending on who you ask) tavern. 
        'Come in all ye weary travelers, beers, ales and cheap wine by the dozen!' is plastered right
        above the doorway of the... establishment. Entering, you can see some familiar faces, but it's
        difficult to focus when the bard's tunes combined with the raucous crowd is earsplitting. It's 
        a wonder how you can ever sleep, living next to a perpetual noise complaint.
        """

        return description 
    
    def getExamination(self):
        examination = """
        Fighting through a possible ruptured eardrum, you manage to zero in on those familiar faces. 
        You can see Michel, the barkeep, tending to some clearly hammered patrons at the bar. Petra's 
        here too, she doesn't indulge, but once in a while everybody's gotta let loose a bit right? 
        For one reason or another, the lull of the bard's tune catches your attention too. Its a 
        simple, jaunty sea shanty, the lyrics talking about how the sea can be a cruel mistress, but 
        also how behind its siren song lies a treasure trove of riches and opportunities. Looking 
        around the tavern, you see 
        """

        return examination
    

        