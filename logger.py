import logging
import os

os.makedirs('Logs',exist_ok=True)

logging.basicConfig(filename='D:/ravi/Data Engineer/Project/Ecommarce/Logs/report.log',
                   level=logging.INFO,
                   format='%(asctime)s-%(levelname)s-%(message)s')

logger=logging.getLogger()