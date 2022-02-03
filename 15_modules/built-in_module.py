# Python built-in modules.
import os
import logging

print(os.name)

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app.")