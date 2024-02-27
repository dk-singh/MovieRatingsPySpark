# MovieRatingsPySpark

Using the movie open data set (ml-1m.zip) from http://files.grouplens.org/datasets/movielens/ml-1m.zip. The source data is copied under `input` directory.


Prerequisite to run the application:
- `Python 3.8.10`
- `pyenv 2.3.35`

Setup the environment:

- `make build-pyenv`

Activate the environment:

- `pyenv activate movie-rating`

Run the application:

- `make run`

### Development and Testing

Format the code:

- `make format`

Run complete test and generate the coverage:

- `make test`

Run the unit tests locally:

- `make test-unit`

View the application log:

- `cat application.log`