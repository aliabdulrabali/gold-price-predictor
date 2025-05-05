import time
import logging
from cron import daily_job

logging.basicConfig(level=logging.INFO)

def start_loop():
    while True:
        logging.info("🔁 Running scheduled daily job...")
        try:
            daily_job()
            logging.info("✅ Daily job completed successfully")
        except Exception as e:
            logging.error(f"❌ Job failed: {e}")
        time.sleep(86400)  # Sleep for 24 hours (86,400 seconds)

if __name__ == "__main__":
    start_loop()
