import logging
import traceback
import time
from src.data_services.miner import miner
from src.data_services.cleaner import cleaner
from src.data_services.transformer import transformer
from src.data_services.db_save import save_to_db
from config.logging_config import setup_logging


def execute_step(step_name, step_function, *args, **kwargs):
    """
    Executes a pipeline step and handles errors specific to that step.

    :param step_name: The name of the pipeline step
    :param step_function: The function to execute for the step
    :param args: Positional arguments to pass to the step function
    :param kwargs: Keyword arguments to pass to the step function
    :return: The result of the step function if successful
    """
    try:
        start_step_exec = time.time()
        result = step_function(*args, **kwargs)
        end_step_exec = time.time()
        logging.info(f"Step {step_name}: Completed successfully in {round((end_step_exec - start_step_exec)
                                                                          * 1000, 2)} ms.")
        return result
    except Exception as e:
        logging.error(f"Error in Step {step_name}: {e}")
        raise


def pipeline():
    """
    Executes the complete data processing pipeline.

    Steps:
    1. Mining: Extracts raw data from source files (PDFs)
    2. Cleaning: Processes and removes noise from the raw data
    3. Transformation: Applies transformations to prepare data for export
    4. DB Saving: Saves the transformed data on the SQL database,

    :return: dict
        A dictionary containing the export status and some useful information
    """
    try:
        # Step 1: Mining
        pdfs_raw_data = execute_step("1: Mining", miner)

        # Step 2: Cleaning
        pdfs_cleaned_data = execute_step("2: Cleaning", cleaner, pdfs_raw_data)

        # Step 3: Transformation
        transformed_data = execute_step("3: Transformation", transformer, pdfs_cleaned_data)

        # Step 4: DB Saving
        execute_step("4: Db saver", save_to_db, transformed_data)


    except Exception as e:
        logging.critical(f"Pipeline execution failed with error: {e}")
        logging.error("Traceback details:")
        logging.error(traceback.format_exc())
        raise

    return {
        "success": True,
        "pdf_processed": len(transformed_data),
        "pdf_failed_to_process": len(pdfs_raw_data) - len(transformed_data),
        "pages_mined": sum(len(data["pages_text_list"]) for data in transformed_data)
    }


if __name__ == "__main__":
    setup_logging()
    logging.info("Starting the pipeline...")
    logging.info(pipeline())
