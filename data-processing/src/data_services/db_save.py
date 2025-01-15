import os
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
    text_content = Column(Text, nullable=False)


# Database setup
DATABASE_URL = "sqlite:///var/db/pdfs.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def save_to_db(data):
    """
    Save transformed PDF data to the database.

    :param data: list
        Transformed data containing PDF information.
    """
    try:
        for pdf_data in data:
            flattened_text = "\n".join(
                ["\n".join(page) for page in pdf_data["pages_text_list"]]
            )

            pdf_entry = PDFContent(
                filename=pdf_data["filename"],
                pdf_metadata=str(pdf_data["metadata"]),
                text_content=flattened_text,
            )
            session.add(pdf_entry)

        session.commit()
        logging.info("Data successfully saved to the database.")

    except Exception as e:
        logging.error(f"Failed to save data to the database: {e}")
        session.rollback()

    finally:
        session.close()
