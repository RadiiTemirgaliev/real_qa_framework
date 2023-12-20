import logging

logging.basicConfig(
    filename=r'.\logs\automation.log', 
    encoding='utf-8', 
    level=logging.INFO, 
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
    )

logger = logging.getLogger()