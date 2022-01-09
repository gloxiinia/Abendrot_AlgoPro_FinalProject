'''
Setting the class for scene 9, or Julian's Cottage, inherited from the scene class.

'''

from scenes.scene import gameObject, Scene

class SceneNine(Scene):
    def __init__(self):
        super().__init__()

        #setting area name
        self.areaName = "Julian's Cottage"

        # setting id
        self.id = "scene9"

        # creating exits
        self.south = "scene10"
        self.west = 'scene8'

        # creating objects
        well = gameObject()
        well.name = 'well'
        well.addAlias('old well')
        well.addAlias('cottage well')
        well.addAlias('waterhole')
        well.detailedDescription = """
        
        """
        self.addObject(well)

        cottage = gameObject()
        cottage.name = 'cottage'
        cottage.addAlias = "julian's cottage"
        cottage.addAlias = "jules' cottage"
        cottage.addAlias = "jules's cottage"
        cottage.detailedDescription = """
        The cottage, seems to embody the word cozy beyond question. From the slow rising wisps of smoke floating
        off from the chimney, to the windows lined with flowering plants, and the fuzzy feeling of whimsiness the
        whole scene gives off, it's not difficult to imagine you're in a fairy tale.
        """
        self.addObject(cottage)

    def getDescription(self):
        description = """
        Jules' cottage. It's quaint, like what you'd see in those storybooks parents read to their kids. 
        """

        return description

    def getExamination(self):
        examination = """
        Once, he'd told you that he decided to up and leave to the countryside on a whim. To be closer with
        nature, he'd said. You were dumbstruck, in disbelief that someone like Julian would just uproot his 
        city life just to satisfy a random urge. When you questioned him, he just chuckled, and didn't say 
        anything more. Said he needed to uphold his reputation of being mysterious and unapproachable. And 
        even after nearly 8 years of knowing him, you still don't know why he did it.
        """
        return examination        
