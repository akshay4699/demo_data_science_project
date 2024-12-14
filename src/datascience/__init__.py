import os
import sys
import logging

# Define logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)    # Log to console
    ]
)

logger = logging.getLogger("DataScienceLogger")

# Example usage of the logger
if __name__ == "__main__":
    logger.info("Logger is configured and ready to use.")
