import logging

logger = logging.getLogger(__name__)


def gen_list_from_text(text: str) -> list:
    paragraphs = text.split('\n')
    logging.debug(f'Paragraphs: {len(paragraphs)}')
    return paragraphs


def transformer(pdfs_cleaned_data):
    formatted_data = [
        {
            "filename": pdf_data_dict["filename"],
            "metadata": pdf_data_dict["metadata"],
            "pages_text": [gen_list_from_text(page_text) for page_text in pdf_data_dict["pages_text"]],
        }
        for pdf_data_dict in pdfs_cleaned_data]

    logging.debug(len(formatted_data[0]["pages_text"]))

    # logging.debug(formatted_data)
