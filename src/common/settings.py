INPUT_PATH = "input"
OUTPUT_PATH = "output"
DELIMITER = "::"
MOVIE_FILE_NAME = "movies.dat"
RATING_FILE_NAME = "ratings.dat"
USER_FILE_NAME = "users.dat"

MOVIE_RATING_FILE_NAME = "movie_rating"
TOP3_MOVIE_FILE_NAME = "top3_movie"

APPLICATION_NAME = "movie-rating"

MOVIE_COLUMN = ["MovieID", "Title", "Genres"]
RATING_COLUMN = ["UserID", "MovieID", "Rating", "Timestamp"]
USER_COLUMN = ["UserID", "Gender", "Age", "Occupation", "Zip-code"]


class Config:
    @property
    def input_path(self):
        return INPUT_PATH

    @property
    def output_path(self):
        return OUTPUT_PATH

    @property
    def movie_file(self):
        return MOVIE_FILE_NAME

    @property
    def movie_columns(self):
        return MOVIE_COLUMN

    @property
    def rating_file(self):
        return RATING_FILE_NAME

    @property
    def rating_column(self):
        return RATING_COLUMN

    @property
    def user_file(self):
        return USER_FILE_NAME

    @property
    def user_column(self):
        return USER_COLUMN

    @property
    def application_name(self):
        return APPLICATION_NAME

    @property
    def delimiter(self):
        return DELIMITER

    @property
    def movie_rating_file_name(self):
        return MOVIE_RATING_FILE_NAME

    @property
    def top3_movie_file_name(self):
        return TOP3_MOVIE_FILE_NAME
