import logging
from sys import argv

logger = logging.getLogger(__name__)


def remove_new_line_char(text):
    return text.replace('\n', '')


def cleaner(pdfs_raw_data):
    pdfs_clean_data = []
    for pdf in pdfs_raw_data:
        cleaned_texts = [remove_new_line_char(text) for text in pdf["pages_text"]]
        pdfs_clean_data.append(cleaned_texts)

    return pdfs_clean_data


if __name__ == "__main__":
    # For test purpose
    cleaner(argv[1])

