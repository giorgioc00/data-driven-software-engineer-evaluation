import logging

logger = logging.getLogger(__name__)


def gen_list_from_text(text: str) -> list:
    """
    This function converts a string into a list of strings splitting the text based on the new line character "\n"
    :param text:
    :return: list of strings
    """
    paragraphs = text.split('\n')
    logging.debug(f'Paragraphs: {len(paragraphs)}')
    return paragraphs


def transformer(pdfs_cleaned_data):
    """
    This function is the entry point of the Pipeline of the transformer module.
    Its purpose is to change the data structure and format of data to be ready for the collection.

    :param pdfs_cleaned_data:
    :return: formatted_data: where inside 'pages_text_list' is formatted as a list of strings
    """
    formatted_data = [
        {
            "filename": pdf_data_dict["filename"],
            "metadata": pdf_data_dict["metadata"],
            "pages_text_list": [gen_list_from_text(page_text) for page_text in pdf_data_dict["pages_text"]],
        }
        for pdf_data_dict in pdfs_cleaned_data]

    logging.debug(formatted_data)

    return formatted_data

    # logging.debug(formatted_data)

