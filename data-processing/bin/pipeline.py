
from ..src.data_pipeline.miner import extract_data
from ..src.data_pipeline.cleaner import clean_data
from ..src.data_pipeline.transformer import transform_data
from ..src.data_pipeline.exporter import export_data
from config.logging_config import setup_logging

def main():

    # Step 1: Mining
    raw_data = extract_data("data/input/pdfs/")
    print("Step 1: Data extracted.")

    # Step 2: Cleaning
    cleaned_data = clean_data(raw_data)
    print("Step 2: Data cleaned.")

    # Step 3: Transformation
    transformed_data = transform_data(cleaned_data)
    print("Step 3: Data transformed.")

    # Step 4: Exporting
    export_data(transformed_data, "data/output/processed_data.csv")
    print("Step 4: Data exported.")

if __name__ == "__main__":
    main()
