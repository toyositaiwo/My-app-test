from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def process_message(self, email, message):
    time.sleep(10)  # simulate long process
    result = f"Processed message from {email}: {message}"
    logger.info(result)
    return result
