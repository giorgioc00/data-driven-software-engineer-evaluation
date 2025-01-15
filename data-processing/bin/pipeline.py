import logging
from src.data_services.miner import miner
from src.data_services.cleaner import cleaner
from src.data_services.transformer import transformer
from src.data_services.exporter import exporter
from config.logging_config import setup_logging

def pipeline():

    # Step 1: Mining
    pdfs_raw_data = miner()
    logging.info("Step 1: Data mined.")

    # Step 2: Cleaning
    pdfs_cleaned_data = cleaner(pdfs_raw_data)
    logging.info("Step 2: Data cleaned.")

    # Step 3: Transformation
    transformed_data = transformer(pdfs_cleaned_data)
    logging.info("Step 3: Data transformed.")

    # Step 4: Exporting
    exporter(transformed_data, "data/output/processed_data.csv")
    logging.info("Step 4: Data exported.")

if __name__ == "__main__":
    setup_logging()
    logging.info("Starting the pipeline...")
    pipeline()
