FROM python:3.11

# container folder
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# make ebase builder executable
RUN chmod +x ./tools/linux/ebmkdb

# store mounted path in env
ENV W2_FS1_DRIVE_KNPS_TESTUMGEBUNG=/mnt/knps_testumgebung

EXPOSE 9000

CMD gunicorn --bind 0.0.0.0:9000 --timeout 600 --workers 2 --threads 2 wsgi:app
