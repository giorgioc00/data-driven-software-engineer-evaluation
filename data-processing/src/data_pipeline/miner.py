from ..utils.finder import collect_files
import logging
import PyPDF2


logger = logging.getLogger(__name__)


def miner():
    files = collect_files()
    """
    Entry point of the miner module.
    Collects PDF file paths using the finder utility, extracts data from each PDF,
    and logs the total number of processed files.

    :return: list
        A list containing extracted data from all PDF files found.
        Each entry in the list is a dictionary with "metadata" and "content" keys.
    """
    logging.debug(f"Number of files found {len(files)}")

    pdfs_extracted_data = []
    for i, file in enumerate(files):
        pdfs_extracted_data.append(get_pdf_data(files[i]))

    # logging.debug(pdfs_extracted_data)
    return pdfs_extracted_data


def get_pdf_data(file_path):
    """
    Extracts data from a PDF file, including metadata and text content.

    This function retrieves the metadata of the PDF file (e.g., author, title)
    and extracts text from all pages of the document. The extracted text is
    organized page by page.

    :param file_path: str
        The file path of the PDF to be processed.
    :return: dict
        A dictionary containing:
        - "metadata" (dict): Metadata of the PDF file, such as author, title, etc.
        - "content" (list): A list of strings where each entry corresponds to
          the text extracted from a single page.
    """

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        logging.debug(f"Number of pages: {len(reader.pages)}")

        # Extract metadata
        meta = reader.metadata

        # Extract text from all pages
        pages_text = []
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            pages_text.append(page_text)

            logging.debug(f"Extracted text from page {i + 1}")

        pdf_data = {
            "metadata": meta,
            "pages_text": pages_text,
        }

        #logging.debug(f"Data extracted from PDF file: {pdf_data}")
        return pdf_data


if __name__ == "__main__":
    miner()
