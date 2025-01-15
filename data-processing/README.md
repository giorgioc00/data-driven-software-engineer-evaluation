# PDF Data Processing

This project provides an easy and fast solutions to extract text data from provided PDFs files.
It focuses on scalability and can handle errors or corrupted PDF files without compromising the data extraction process.
The data is then made available for analysis on a SQLite DB table.


Installation
------------
1. Clone the repository:
   `git clone https://github.com/giorgioc00/data-driven-software-engineer-evaluation.git`
2. Got to the project dir: `cd data-driven-software-engineer-evaluation/data-processing`

3. Create a virtual environment:
   `python3 -m venv venv` - on Unix-like OS
   `source venv/bin/activate`  - On Windows: `venv\Scripts\activate`

4. Install dependencies:
   `pip install -r requirements.txt`

Usage
-----
1. Go to the `.data/input/pdfs` directory
   and place the PDF files that need to be processed in that folder.

2. Run the Pipeline as module:
   `python3 -m bin.pipeline`

   This will:
   - Extract data from the PDFs in the `./pdfs` folder.
   - Clean the extracted data to remove any unwanted characters or formatting issues.
   - Transform the cleaned data into a structured format.
   - Store all the new extracted data in a SQlite database (located at `.var/db/pdfs.db`)

For analyzing the collected data, you can directly query the database table named `pdf_content`.

N.B., A file has only one record on the table and the file name is used as identification of it, running the app
different times on the same files will not create duplicated entries on the DB table.



Logging
-------
The project uses Python's built-in `logging` module to track the progress of the data processing steps. The logs include information such as:
- The number of files processed or failed to process
- The number of pages processed
- The total length of the text extracted
- Errors encountered during extraction, cleaning, transformation and database operations
- Execution time for each step

Logs are written to `var/main.log`, with different log levels (e.g., `INFO`, `ERROR`, `CRITICAL`).
   


# Assignment details

## Data processing

In the `./pdfs` folder you will find a set of PDF files containing data that needs to be processed.
Your task is to extract the data from these PDFs and store it in a structured format for further analysis.

Assume that these won't be the only PDFs you'll need to process, and that you'll need to scale your solution to handle a larger number of files, both in 
terms of file structure and data volume.

Please code your solution using Python.

You're free to structure the project as you see fit, but make sure to include clear instructions on how to run your solution.

## Attention points

Make sure to consider the following points when designing your solution:
* code quality - make sure your code is clean, readable, and maintainable
* performance - as said before, in the future you'll need to process a larger number of files, so make sure your solution is scalable
* error handling - make sure your solution can handle exceptions and edge cases (malformed files, etc.)
* testing - make sure your solution is well tested
* git usage - make sure your commits are well organized and that you have a good commit history
