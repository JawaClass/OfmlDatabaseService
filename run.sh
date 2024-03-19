
celery --app wsgi:celery_app worker --hostname 'worker_1@%h' --loglevel INFO --concurrency 2 --pool threads --detach

celery --app wsgi:celery_app worker --hostname 'worker_2@%h' --loglevel INFO --concurrency 2 --pool threads --detach

gunicorn --bind 0.0.0.0:9000 --timeout 600 --workers 2 --threads 2 wsgi:app