from app import create_app
import logging

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True)
    # logger.info("Загрузка данных из API...")
