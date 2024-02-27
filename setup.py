from setuptools import find_packages, setup

setup(
    name="movie-rating",
    version="0.0.1",
    description="Test job for ETL",
    author="Dheeraj Singh",
    author_email="dheerajksingh@gmail.com",
    packages=find_packages(),
    package_data={"src": ["resources/*.conf"]},
    platforms="any",
    setup_requires=["pytest-runner"],
)
