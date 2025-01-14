from ..utils.finder import collect_files
import logging
import PyPDF2


logger = logging.getLogger(__name__)

def miner():
    files = collect_files()
    logging.debug(f"Number of files found {len(files)}")
    load_pdf(files[0])


def load_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Number of pages: {len(reader.pages) }")

        meta = reader.metadata

        # All of the following could be None!
        print(meta.author)
        print(meta.creator)
        print(meta.producer)
        print(meta.subject)
        print(meta.title)

        page = reader.pages[0]
        print(page.extract_text())


if __name__ == "__main__":
    miner()
