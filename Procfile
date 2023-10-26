web: gunicorn -w 4 -b 0.0.0.0:5000 renderer.src.app:app
worker-renderer: python3 renderer/src/main.py
worker-transformer: python3 transformer/src/main.py
worker-collector: python3 collector/src/main.py
