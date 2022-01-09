'''
Setting the class for scene 4, or Sol Lane, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene

class SceneFour(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Sol Lane"

        # setting id
        self.id = "scene4"

        # creating exits
        self.north = 'scene3'
        self.south = "scene5"
        self.east = 'scene7'

        # creating objects
        fruitStall = gameObject()
        fruitStall.name = 'fruit stall'
        fruitStall.aliases.append('fruit shop')
        fruitStall.aliases.append('fruit store')
        fruitStall.aliases.append('fruit vendor')
        fruitStall.aliases.append("liesl's fruits")
        fruitStall.detailedDescription = """
        There doesn't sseem to be anyone behind the counter here, a shame. It's fairly innocuous, 
        just selling your run-of-the-mill apples, bananas, grapes, and oh, peaches too. Neat. 
        The tiny sign reads: 'Liesl's Fruits'. How inventive.   
        """
        self.addObject(fruitStall)

        antiqueStall = gameObject()
        antiqueStall.name = 'antique stall'
        antiqueStall.aliases.append('antiques shop')
        antiqueStall.aliases.append('antique shop')
        antiqueStall.aliases.append('antiques stall')
        antiqueStall.aliases.append('antique store')
        antiqueStall.aliases.append('antiques store')

        antiqueStall.detailedDescription = """
        If the rusted-to-all-hell weapons proudly displayed front and center didn't convince you, 
        certainly the various artifacts and knick-knacks on the table lends credence to that 
        notion. No signs, plaques or anything to denote the shop's name. There's noone tending to 
        this shop. Must be on break then.
        """
        self.addObject(antiqueStall)
    
    def getDescription(self):
        description = """
        If the plaza was the heart of Sonnenau, Sol Lane could be seen as the town's lungs, no doubt 
        as busy and integral, breathing life towards Sonnenau's longevity. The fountain lies in the 
        middle of it all, built when Sonnenau was still a foundling of a city. The street is lined 
        with stands and stalls, selling items ranging from simple provisions, to weapons forged to 
        slay and strike down the toughest foes. Of course, everything comes with a price here, but
        the merchants aim to sell their wares at the end of the day, which means haggling before 
        buying is highly encouraged.
        """
        return description

    def getExamination(self):
        examination = """
        To your right, you see a fruit stall. To your left, another stall, but it's quite tough to 
        discern what exactly its wares are. It looks like an antiques shop? 
        """
        return examination

        
