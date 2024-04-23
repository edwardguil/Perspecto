
class Sage():
    """
    Represents the perspect mode of Perspective Pilot. Responsible for deciding 
    on the relevance of content found by the Pilot, and making comments on the 
    content.
    '''
    """

    def __init__(self, model):
        self.model = model

class Pilot():
    '''
    Represents the Piloting 'mode' of Perspective Pilot. When a Perspective
    Pilot is in Pilot mode, it browses the web, searching for relevant content. 
    '''

    def __init__(self, platform):
        self.platform = platform