import threading
import os
import logging
from app.services.data_loader import load_and_update_data

logger = logging.getLogger(__name__)

_scheduler_thread = None

def scheduler_job():
    interval = int(os.getenv("LOAD_INTERVAL_SECONDS", 3600))
    while True:
        try:
            logger.info("Загрузка данных из API...")
            load_and_update_data()
            logger.info("Обновление данных прошло успешно")
        except Exception as e:
            logger.error(f"Ошибка в планировщике: {e}", exc_info=True)
        threading.Event().wait(interval)

def start_scheduler():
    global _scheduler_thread
    if _scheduler_thread and _scheduler_thread.is_alive():
        logger.info("Планировщик уже запущен")
        return
    _scheduler_thread = threading.Thread(target=scheduler_job, daemon=True)
    _scheduler_thread.start()
    logger.info("Планировщик запущен")
