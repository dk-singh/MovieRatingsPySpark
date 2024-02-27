import unittest

from src.transformations.data_transformer import (
    add_column_name,
    get_movie_rating,
    get_top_three_movie,
)


def test_add_column_name(spark):
    # Sample data
    data = [("Test1", "Test2"), ("Test3", "Test4")]
    columns = ["_c0", "_c1"]
    source_df = spark.createDataFrame(data, columns)

    new_column_names = ["first_name", "last_name"]
    result_df = add_column_name(source_df, new_column_names)

    # Check if the column names are correctly updated
    expected_columns = ["first_name", "last_name"]
    assert result_df.columns == expected_columns

    assert result_df.collect() == source_df.collect()


def test_get_movie_rating(spark):
    test = unittest.TestCase()
    # Sample Movie DataFrame
    movies_data = [
        (1, "Toy Story (1995)", "Animation|Children"),
        (2, "Jumanji (1995)", "Adventure|Children"),
        (3, "Grumpier Old Men (1995)", "Comedy|Romance"),
        (4, "Waiting to Exhale (1995)", "Comedy|Drama"),
        (5, "Father of the Bride Part II (1995)", "Comedy"),
    ]
    movies_columns = ["MovieID", "Title", "Genres"]
    movie_df = spark.createDataFrame(movies_data, movies_columns)

    # Sample Rating DataFrame
    ratings_data = [
        (1, 1, 5),
        (2, 1, 4),
        (3, 2, 3),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 5),
    ]
    ratings_columns = ["UserID", "MovieID", "Rating"]
    rating_df = spark.createDataFrame(ratings_data, ratings_columns)

    # Call the function
    result_df = get_movie_rating(rating_df, movie_df)

    # Assert the result DataFrame columns
    test.assertTrue("MovieID" in result_df.columns)
    test.assertTrue("Title" in result_df.columns)
    test.assertTrue("MaxRating" in result_df.columns)
    test.assertTrue("MinRating" in result_df.columns)
    test.assertTrue("AvgRating" in result_df.columns)

    # Assert specific values for max, min, and avg ratings
    expected_max_rating = 5
    expected_min_rating = 4
    expected_avg_rating = (5 + 4) / 2

    test.assertEqual(result_df.select("MaxRating").first()[0], expected_max_rating)
    test.assertEqual(result_df.select("MinRating").first()[0], expected_min_rating)
    test.assertAlmostEqual(
        result_df.select("AvgRating").first()[0], expected_avg_rating, places=2
    )


def test_get_top_three_movie(spark):
    test = unittest.TestCase()
    # Sample Movie DataFrame
    movies_data = [
        (1, "Toy Story (1995)", "Animation|Children"),
        (2, "Jumanji (1995)", "Adventure|Children"),
        (3, "Grumpier Old Men (1995)", "Comedy|Romance"),
        (4, "Waiting to Exhale (1995)", "Comedy|Drama"),
        (5, "Father of the Bride Part II (1995)", "Comedy"),
    ]
    movies_columns = ["MovieID", "Title", "Genres"]
    movie_df = spark.createDataFrame(movies_data, movies_columns)

    # Sample Rating DataFrame
    ratings_data = [
        (1, 1, 5),
        (1, 2, 4),
        (1, 3, 3),
        (2, 1, 2),
        (2, 2, 4),
        (2, 3, 5),
        (3, 1, 3),
        (3, 2, 5),
        (3, 3, 4),
        # Add more rating data as needed
    ]
    ratings_columns = ["UserID", "MovieID", "Rating"]
    rating_df = spark.createDataFrame(ratings_data, ratings_columns)

    # Call the function
    result_df = get_top_three_movie(movie_df, rating_df)

    # Assert the result DataFrame columns
    test.assertTrue("UserID" in result_df.columns)
    test.assertTrue("MovieID" in result_df.columns)
    test.assertTrue("Rating" in result_df.columns)
    test.assertTrue("Title" in result_df.columns)
    test.assertTrue("Genres" in result_df.columns)

    # Assert specific values for the top data
    expected_data = [
        (1, 1, 5, "Toy Story (1995)", "Animation|Children"),
        (2, 1, 4, "Jumanji (1995)", "Adventure|Children"),
        (3, 1, 3, "Grumpier Old Men (1995)", "Comedy|Romance"),
        # Add more expected data for each user as needed
    ]

    for expected_row, actual_row in zip(expected_data, result_df.collect()):
        test.assertEqual(expected_row, tuple(actual_row))
