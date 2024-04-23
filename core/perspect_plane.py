from people import Sage, Pilot

class PerspectPlane:
    '''
    Represents a single Perspective Plane. Manned by a Pilot and a Sage.
    The Pilot is responsible for finding posts and comments on the web, while
    the Sage is responsible for deciding on the relevance of the content found
    by the Pilot, and making comments on the content.
    '''
    
    def __init__(self, name:str, platform:str='youtube', model='llam3'):
        self.name = name
        self.platform = platform
        self.pilot = Pilot(platform=platform)
        self.sage = Sage(model=model)

    def run(self):
        while True:
            # Pilot, fly through web and find posts
            posts = self.pilot.find_posts()

            # Sage, determine which posts are most suitable
            suitable_posts = self.sage.rank_posts(posts)

            # If no suitable content found, go back to searching
            if not suitable_posts:
                continue

            # Else, dive into each post handle it
            for post in suitable_posts:
                # For a post, get the comments
                comments = self.pilot.get_comments(post)

                # Perspect, decide on relevance of comments
                relevant_comments = self.sage.rank_comments(comments)

                # If no relevant comments found, go to next post
                if not relevant_comments:
                    continue

                # Else, pick the most relevant comments and respond to it
                for comment in relevant_comments:
                    # For a comment, generate a response
                    response = self.sage.generate_response(comment)

                    # Pilot, deliver the response
                    self.pilot.deliver_response(response)