import logging

def setup_logging():
    logging.basicConfig(
        filename="var/main.log",
        encoding="utf-8",
        filemode="a",
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
