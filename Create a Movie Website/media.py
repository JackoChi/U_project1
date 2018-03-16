import webbrowser
class Movie():
    '''The class called Movie will help us to creat multiple instance'''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        '''This function allows us creat instance including title, poster and trailer.'''
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''Function helps us to open the movie trailer through webbrower when clik on it.'''
        webbrowser.open(self.trailer_youtube_url)
