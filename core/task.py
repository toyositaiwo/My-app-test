from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def process_message(self, email, message):
    logger.info(f"Processing message for {email}")
    time.sleep(10)  # Simulate a long task
    result = f"Processed message from {email}: {message}"
    logger.info(result)
    return result
