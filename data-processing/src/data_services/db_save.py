import json
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# SQLAlchemy Base
Base = declarative_base()


# Define the database model
class PDFContent(Base):
    __tablename__ = "pdf_content"

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)
    pdf_metadata = Column(Text, nullable=True)
    pages_text_content = Column(Text, nullable=False)


# Database setup
DATABASE_URL = "sqlite:///var/db/pdfs.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def save_to_db(data):
    """
    Save transformed PDF data to the database if the file doesn't already exist.

    :param data: list
        Transformed data containing PDF information.
    """
    try:
        for pdf_data in data:
            existing_entry = session.query(PDFContent).filter_by(filename=pdf_data["filename"]).first()
            if existing_entry:
                logging.info(f"Data for {pdf_data['filename']} already exists in the database. Skipping...")
                continue

            text_content_data_json = json.dumps(pdf_data["pages_text_list"])
            logging.debug(text_content_data_json)
            pdf_entry = PDFContent(
                filename=pdf_data["filename"],
                pdf_metadata=str(pdf_data["metadata"]),
                pages_text_content=text_content_data_json,
            )
            session.add(pdf_entry)

        session.commit()
        logging.info("Data successfully saved to the database.")

    except Exception as e:
        logging.error(f"Failed to save data to the database: {e}")
        session.rollback()

    finally:
        session.close()
