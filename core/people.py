from platforms import NavigatorFactory

class Sage():
    '''
    Represents the Sage of Perspect Plane.
    '''
    def __init__(self, model):
        self.model = model


    def rank_posts(self, posts):
        pass


class Pilot():
    '''
    Represents the Pilot of Perspect Plane. 
    '''

    def __init__(self, platform):
        self.navigator = NavigatorFactory.create_navigator(platform)

    def find_posts(self, topic='left wing destroyed'):
        self.navigator.search(topic)
        return self.navigator.get_search_results()
    
    def get_comments(self, post):
        self.navigator.go_to(post)
        return self.navigator.get_comments()
    
    def deliver_response(self, comment, response):
        self.navigator.make_response(comment, response)