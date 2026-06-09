from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "End-to-End-Book-Recommender-System"
AUTHOR_USER_NAME = "md-naim-molla"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name="book-recommender",
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="naim.molla.stats@gmail.com",
    packages= find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)