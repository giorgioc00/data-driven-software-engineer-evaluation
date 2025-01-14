import os
import logging


def pdfs_finder():
    """
    Collects the full paths of all files within the 'data/input' directory.

    This function traverses the specified directory and all its subdirectories,
    retrieving the full paths of each file it encounters.

    :return: A list containing the absolute paths of all files found in 'data/input'.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "../../data/input/")
    data_dir = os.path.abspath(data_dir)

    files = []
    for root, _, filenames in os.walk(data_dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    logging.debug(files)
    return files


if __name__ == '__main__':
    file_found = collect_files()
    print(file_found)

