from src.common import settings


def test_application_name():
    settings.Config()
    assert settings.APPLICATION_NAME == "movie-rating"


def test_input_path():
    settings.Config()
    assert settings.INPUT_PATH == "input"


def test_output_path():
    settings.Config()
    assert settings.OUTPUT_PATH == "output"


def test_movie_file():
    settings.Config()
    assert settings.MOVIE_FILE_NAME == "movies.dat"


def test_rating_file():
    settings.Config()
    assert settings.RATING_FILE_NAME == "ratings.dat"


def test_user_file():
    settings.Config()
    assert settings.USER_FILE_NAME == "users.dat"


def test_delimiter():
    settings.Config()
    assert settings.DELIMITER == "::"


def test_top3_movie_file_name():
    settings.Config()
    assert settings.TOP3_MOVIE_FILE_NAME == "top3_movie"


def test_movie_rating_file_name():
    settings.Config()
    assert settings.MOVIE_RATING_FILE_NAME == "movie_rating"


def test_movie_columns():
    settings.Config()
    assert settings.MOVIE_COLUMN == ["MovieID", "Title", "Genres"]


def test_rating_column():
    settings.Config()
    assert settings.RATING_COLUMN == ["UserID", "MovieID", "Rating", "Timestamp"]


def test_user_column():
    settings.Config()
    assert settings.USER_COLUMN == ["UserID", "Gender", "Age", "Occupation", "Zip-code"]
