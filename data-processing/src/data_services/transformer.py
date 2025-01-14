import logging

logger = logging.getLogger(__name__)




def transformer(pdfs_cleaned_data):

    formatted_data = [
        {
            "filename": pdf_data_dict["filename"],
            "metadata": pdf_data_dict["metadata"],
            "pages_text": pdf_data_dict["pages_text"],
        }
        for pdf_data_dict in pdfs_cleaned_data]

    logging.debug(formatted_data)
