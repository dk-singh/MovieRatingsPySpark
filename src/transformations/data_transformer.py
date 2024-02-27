from pyspark.sql import functions as F
from pyspark.sql.window import Window


def read_csv_file(spark, path, file_name, delimiter):
    df = spark.read.option("delimiter", delimiter).csv(path + "/" + file_name)
    return df


def add_column_name(source_df, column_list):
    for i, col_name in enumerate(column_list):
        source_df = source_df.withColumnRenamed("_c{}".format(i), col_name)
    return source_df


def get_movie_rating(rating_df, movie_df):
    joined_df = rating_df.join(movie_df, "MovieID")

    # Calculate Max, Min, and Average Ratings
    rating_analysis_df = joined_df.groupBy("MovieID", "Title").agg(
        F.max("Rating").alias("MaxRating"),
        F.min("Rating").alias("MinRating"),
        F.avg("Rating").alias("AvgRating"),
    )
    return rating_analysis_df


def get_top_three_movie(movie_df, rating_df):
    # Rank movies for each user based on their ratings
    window_spec = Window.partitionBy("UserID").orderBy(F.col("Rating").desc())
    ranked_movies_df = (
        rating_df.withColumn("rank", F.row_number().over(window_spec))
        .filter("rank <= 3")
        .drop("rank")
    )
    # Join with movie data to get movie details
    top3_movies_df = ranked_movies_df.join(movie_df, "MovieID").orderBy(
        "UserID", "Rating", ascending=[True, False]
    )
    return top3_movies_df


def write_to_parqurt(df, path, file_name):
    df.write.parquet(path + "/" + file_name, mode="overwrite")
