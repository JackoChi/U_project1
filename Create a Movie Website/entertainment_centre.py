import media
import fresh_tomatoes

Rudy = media.Movie("Rudy",
                   "https://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",  # noqa
                   "https://www.youtube.com/watch?v=Xm0pTMbDaMI")  # noqa
Rudy.show_trailer()

The_Imitation_Game = media.Movie("The Imitation Game",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/The_Imitation_Game_poster.jpg/250px-The_Imitation_Game_poster.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")  # noqa
The_Imitation_Game.show_trailer()

A_Beautiful_Mind = media.Movie("A Beautiful Mind",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beautiful_Mind_Poster.jpg/220px-A_Beautiful_Mind_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o&t=54s")  # noqa
A_Beautiful_Mind.show_trailer()


movies = [Rudy, The_Imitation_Game, A_Beautiful_Mind]
fresh_tomatoes.open_movies_page(movies)
