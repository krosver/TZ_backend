from app import create_app
from app.services.scheduler import start_scheduler
from app.utils.logger import logger

app = create_app()

if __name__ == '__main__':
    logger.info("Запуск сервиса...")
    start_scheduler(app)
    app.run(host="0.0.0.0", port=5000, threaded=True)
    
