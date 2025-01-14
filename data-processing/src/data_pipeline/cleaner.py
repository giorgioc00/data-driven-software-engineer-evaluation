import logging
import re
from sys import argv

logger = logging.getLogger(__name__)


def remove_noise_characters(text):
    """
    Removes noise characters from a string, like new line characters "\n" and spaces inside a word

    :param text to be processed
    :return: cleaned text
    """

def cleaner(pdfs_raw_data):
    """
    Cleans text data from PDF pages by removing noise by updating each element of the 'pages_text' list.

    :param pdfs_raw_data: list of dict
        Each dictionary contains:
        - "metadata": PDF metadata.
        - "pages_text": List of text from PDF pages (cleaned)
    :return: list of dict
        Updated data with cleaned text for each page with the same input format.


if __name__ == "__main__":
    # For test purpose
    cleaner(argv[1])

