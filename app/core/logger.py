"""
Contains my logging application and logging format
"""
import logging
import json

#Structured logs Json
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
        }

        #Add extra fields if they exist
        if hasattr(record, "method"):
            log_record["method"] = record.method
        if hasattr(record, "path"):
            log_record["path"] = record.path
        if hasattr(record, "status"):
            log_record["status"] = record.status
        if hasattr(record,"duration"):
            log_record["duration"] = record.duration   
        
        return json.dumps(log_record)

#basic logging
def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)

    return logger


logger = setup_logger()