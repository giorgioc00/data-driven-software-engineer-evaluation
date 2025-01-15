import logging
import re
from sys import argv

logger = logging.getLogger(__name__)


def remove_noise_characters(text: str) -> str:
    """
    Removes noise characters from a string, like new line characters "\n" and spaces inside a word

    :param text to be processed
    :return: cleaned text
    """
    text = re.sub(r"(?<!\w)\s+|\s+(?!\w)", "", text)
    text = text.replace('●', '')
    text = text.strip()

    return text


def cleaner(pdfs_raw_data: list) -> list[dict]:
    """
    Cleans text data from PDF pages by removing noise by updating each element of the 'pages_text' list.

    :param pdfs_raw_data: list of dict
        Each dictionary contains:
        - "metadata": PDF metadata.
        - "pages_text": List of text from PDF pages (cleaned)
    :return: list of dict
        Updated data with cleaned text for each page with the same input format.
    """
    pdfs_clean_data = []
    for pdf in pdfs_raw_data:
        cleaned_pages_text = [remove_noise_characters(text) for text in pdf["pages_text"]]
        pdfs_clean_data.append({
            "filename": pdf["filename"],
            "metadata": pdf["metadata"],
            "pages_text": cleaned_pages_text,
        })

    return pdfs_clean_data


if __name__ == "__main__":
    # For test purpose
    cleaner(argv[1])

