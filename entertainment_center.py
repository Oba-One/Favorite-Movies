"""Stores detail of movies and display them on static website"""
import fresh_tomatoes
import media


def main():
    """Creates 9 movie objects, with title =, storyline, poster image, video trailer link, & release date"""
    toy_story = media.Movie(
        "Toy Story",
        "A story of a kid and his toys that come to life.",
        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
        "https://www.youtube.com/watch?v=vwyZH85NQC4",
        "November 1995")
    pirates_of_the_carribean = media.Movie(
        "Pirates Of The Carribean: Dead Man Chest",
        "A story of pirates and one who rules the sea called Davy Jones.",
        "https://upload.wikimedia.org/wikipedia/en/thumb/2/2d/Pirates_of_the_caribbean_2_poster_b.jpg/220px-Pirates_of_the_caribbean_2_poster_b.jpg",
        "https://www.youtube.com/watch?v=ozk0-RHXtFw",
        "June 2006")
    dark_knight = media.Movie(
        "Dark Knight",
        "The story of Batman and anarchist The Joker.",
        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
        "https://www.youtube.com/watch?v=EXeTwQWrcwY",
        "July 2008")
    home_alone = media.Movie(
        "Home Alone",
        "A clever boy gets left alone at home during Christmas.",
        "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",
        "https://www.youtube.com/watch?v=jEDaVHmw7r4",
        "November 1990")
    inception = media.Movie(
        "Inception",
        "A story of dreams and the preception of reality.",
        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
        "https://www.youtube.com/watch?v=YoHD9XEInc0",
        "July 2010")
    step_brothers = media.Movie(
        "Step Brothers",
        "Two middle age men become brothers still living at home.",
        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/StepbrothersMP08.jpg/220px-StepbrothersMP08.jpg",
        "https://www.youtube.com/watch?v=CewglxElBK0",
        "July 2008")
    monsters_inc = media.Movie(
        "Monster's Inc",
        "A story of Monster who scare kids for electricity.",
        "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
        "https://www.youtube.com/watch?v=8IBNZ6O2kMk",
        "November 2001")
    harry_potter = media.Movie(
        "Harry Potter: Prisoner of Azkaban",
        "The story of Harry Potter and man called Sirius Black.",
        "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Prisoner_of_azkaban_UK_poster.jpg/220px-Prisoner_of_azkaban_UK_poster.jpg",
        "https://www.youtube.com/watch?v=lAxgztbYDbs",
        "June 2004")
    lord_of_the_rings = media.Movie(
        "Lord of the Rings: The Two Towers",
        "An epic journey around friendship and darkness.",
        "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
        "https://www.youtube.com/watch?v=LbfMDwc4azU",
        "December 2002")
    # Store the Movie objects in a list
    movies = [toy_story, pirates_of_the_carribean, dark_knight, home_alone, inception, step_brothers, monsters_inc, harry_potter, lord_of_the_rings]

    # Open the movie website in the users browser, with list of movies.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
