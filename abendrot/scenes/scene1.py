'''
Setting the class for scene 1, or the Player's Home, inherited from the scene class.

'''

from scenes.scene import Scene, gameObject

class SceneOne(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Home"

        # setting id
        self.id = "scene1"

        # creating exits
        self.south = "scene2"

        # creating objects
        bookcase = gameObject()
        bookcase.name = "bookcase"
        bookcase.addAlias("bookshelf")
        bookcase.addAlias('books')
        bookcase.detailedDescription = """
        Browsing through the collection, you can see a couple of titles and scrolls that
        catch your eye. One is a copy of Misfortune Without a Goal, an autobiographical about
        one Valter von Kempf, a self-supposed renowned philosopher from Ocrus. The other is a
        copy of ancient scroll you managed to recover from a ruin in the city of Osse, up north,
        across the channel of Sonnenau. After donating it to Emil, he deciphered and graciously
        copied the text for your keeping. Deciphered, the title amounts to "Owls of the Light". 
        """
        self.addObject(bookcase)

        book1 = gameObject()
        book1.name = "misfortune without a goal"
        book1.addAlias("misfortune book")
        book1.addAlias("philosophy book")
        book1.addAlias("autobiography book")
   
        book1.detailedDescription = """
        It regales how on his journeys, like the title implies, misfortunes befall him. But through
        these experiences, he managed to come to an epiphany, one that became the basis for his
        thesis, titled: " The Phantoms of Nihilism, Magic, and Its Implications". Not a quick read,
        but when you managed to push through, it left you an empty, perpetual machine of existencial
        crisis and doubt for a week. So, it's effective, to say the least.        
        """
        self.addObject(book1)

        book2 = gameObject()
        book2.name = "owls of the light"
        book2.addAlias('scroll')
        book2.addAlias('ancient scroll')
        book2.addAlias('owl scroll')
        book2.addAlias("owl book")
        book2.addAlias("old scroll")
 
        book2.detailedDescription = """
        Below, it writes of how milennia ago, owls thrived and nested within the tree boughs 
        of Osse. Growing up to 3 metres tall, they grew in tandem with Osse's people, even going out
        in the day to help them when needed, in return the citizens would offer extra food and help 
        the owls defend their territory. While the owls seemed capable enough on their own and it was 
        mostly a ceremonial affair, nevertheless, the arrangement strengthened the bond between the 
        two parties.
        """
        self.addObject(book2)

        rucksack = gameObject()
        rucksack.name = 'rucksack'
        rucksack.addAlias('backpack')
        rucksack.addAlias('bag')
        rucksack.addAlias('knapsack')
 
        rucksack.detailedDescription = """
        Your trusty leather rucksack. It's rough and worn and some of the stiching have come loose, 
        but after a good decade, it still holds up pretty well considering where that bag has been.
        Note to self, never agree to a deal that involves the words 'waterfall' and 'rapids'. Unless
        a thief snuck in and stole it, inside is yet another scroll Emil has sent you to find. This
        time it was the jungles of Euzes, quite the trek south from Sonnenau, so pay better be worth it.
        Emil tried to offer 5 silver coins for a quest that would take you to Isaeon and back. To put
        it mildly, you refused.
        """

        self.addObject(rucksack)

        kitchen = gameObject()
        kitchen.name = 'kitchen'
        kitchen.addAlias('counter')
        kitchen.addAlias('kitchen counter')
        kitchen.detailedDescription = """
        Ah your kitchen. Though it's not up to sous chef standards, it's adequate for what it is.
        It's survived your many attempts at cooking, nights of drunken bliss, and the occasional ink
        spillage from late-night text decrypting.
        """
        self.addObject(kitchen)

        bed = gameObject()
        bed.name = 'bed'
        bed.addAlias('mattress')
        bed.addAlias('cot')
        bed.addAlias('bunk')
        bed.detailedDescription = """
        As far as beds go, this one is comfortable enough, you'd say. It's not as fancy as those
        mattresses imbued with magic that makes it as soft and light like a cloud, but it works.
        Temperatures here get cold enough, so you never bought a blanket or a comforter.
        """
        self.addObject(bed)

    def getDescription(self):
        description = """
        Home. Nothing much to say about it. It's a nice, if small, apartment you were lucky 
        enough to get for a good price. Mama wanted you to stay with her in the countryside 
        till things in the city died down, but you said no. Deals like these are hard to come 
        by and you'd rather not miss out on a chance to find your own footing in the world. 
        It might not be much, but after every quest you finish, the soft, russet tones of home
        will always be there to comfort you. Even if most of the time you end up passing out 
        on the floor.
        """        
        return description

    def getExamination(self):
        examination = """
        Looking around, you see a couple of things. Mainly the large bookcase you had custom-made
        from the finest oak, filled to the brim with texts, journals, and writings that you've 
        managed to uncover during your travels. Beside it, there's a kitchen counter, innocuous, 
        except for the dusty rucksack laid on top of it. And, your bed. Not the best quality but 
        hey, you don't have chronic back pain so that's a plus. Maybe. 
        """
        return examination





