from pyspark.sql import SparkSession

from src.common.logger import setup_logger
from src.common.settings import Config
from src.transformations.data_transformer import (
    add_column_name,
    get_movie_rating,
    get_top_three_movie,
    read_csv_file,
    write_to_parqurt,
)


class DataTransformer:
    # Create a Spark session

    def __init__(self) -> None:
        self.config = Config()

    def run(self):
        logger = setup_logger()
        logger.info("Start the application")
        logger.info("Create the spark session")
        spark = SparkSession.builder.getOrCreate()
        spark.sparkContext.appName = self.config.application_name
        spark.conf.set("spark.sql.session.timeZone", "UTC")

        logger.info("Reading movie data..")
        movie_raw_df = read_csv_file(
            spark, self.config.input_path, self.config.movie_file, self.config.delimiter
        )
        movie_df = add_column_name(movie_raw_df, self.config.movie_columns)
        logger.info("Total movie records sourced : " + str(movie_df.count()))

        logger.info("Reading ratings data..")
        rating_raw_df = read_csv_file(
            spark,
            self.config.input_path,
            self.config.rating_file,
            self.config.delimiter,
        )
        rating_df = add_column_name(rating_raw_df, self.config.rating_column)
        logger.info("Total rating records sourced : " + str(rating_df.count()))

        logger.info("Reading user data..")
        user_raw_df = read_csv_file(
            spark,
            self.config.input_path,
            self.config.user_file,
            self.config.delimiter,
        )
        user_df = add_column_name(user_raw_df, self.config.user_column)
        logger.info("Total user records sourced : " + str(user_df.count()))

        logger.info("Generating movie ratings..")
        movie_rating_df = get_movie_rating(rating_df, movie_df)
        logger.info("Total records in ratings : " + str(movie_rating_df.count()))

        logger.info("Generating top three movie for each user..")
        top_three_movie_df = get_top_three_movie(movie_df, rating_df)
        logger.info(
            "Total records in top three movie : " + str(top_three_movie_df.count())
        )

        # Test to show data frames
        # movie_df.show()
        # rating_df.show()
        # user_df.show()
        # movie_rating_df.show()
        # top_three_movie_df.show()

        logger.info("Writing output to parquet file ..")
        write_to_parqurt(
            movie_df,
            self.config.output_path,
            self.config.movie_file,
        )
        write_to_parqurt(
            rating_df,
            self.config.output_path,
            self.config.rating_file,
        )
        write_to_parqurt(
            user_df,
            self.config.output_path,
            self.config.user_file,
        )
        write_to_parqurt(
            movie_rating_df,
            self.config.output_path,
            self.config.movie_rating_file_name,
        )
        write_to_parqurt(
            top_three_movie_df,
            self.config.output_path,
            self.config.top3_movie_file_name,
        )
        # Stop the Spark session
        logger.info("Stopping Spark Session ..")
        spark.stop()
        logger.info("-- End of Process --")


if __name__ == "__main__":
    dataTransformer = DataTransformer()
    dataTransformer.run()
