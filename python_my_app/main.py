import os
import logging

import pendulum

logger = logging.getLogger(__name__)
logger.info("INFO")

now_in_paris = pendulum.now("Europe/Paris")
print(now_in_paris)
