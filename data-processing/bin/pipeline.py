import logging
import traceback
from src.data_services.miner import miner
from src.data_services.cleaner import cleaner
from src.data_services.transformer import transformer
from src.data_services.exporter import exporter
from config.logging_config import setup_logging


def execute_step(step_name, step_function, *args, **kwargs):
    try:
        result = step_function(*args, **kwargs)
        logging.info(f"Step {step_name}: Completed successfully.")
        return result
    except Exception as e:
        logging.error(f"Error in Step {step_name}: {e}")
        raise


def pipeline():
    try:
        # Step 1: Mining
        pdfs_raw_data = execute_step("1: Mining", miner)

        # Step 2: Cleaning
        pdfs_cleaned_data = execute_step("2: Cleaning", cleaner, pdfs_raw_data)

        # Step 3: Transformation
        transformed_data = execute_step("3: Transformation", transformer, pdfs_cleaned_data)

        # Step 4: Exporting
        execute_step("4: Exporting", exporter, transformed_data, "data/output/processed_data.csv")

    except Exception as e:
        logging.critical(f"Pipeline execution failed with error: {e}")
        logging.error("Traceback details:")
        logging.error(traceback.format_exc())
        raise

    return {
        "success": True,
        "pdf_processed": len(transformed_data),
        "pages_mined": sum(len(data["pages_text_list"]) for data in transformed_data)
    }


if __name__ == "__main__":
    setup_logging()
    logging.info("Starting the pipeline...")
    logging.info(pipeline())
