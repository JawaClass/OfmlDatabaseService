FROM python:3.11

# container folder
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

#RUN mkdir /mnt/knps_testumgebung && \
#    pip install --no-cache-dir -r requirements.txt

# store mounted path in env
ENV CREATE_OFML_EXPORT_PATH=/mnt/knps_testumgebung/ofml_development/Tools/ofml_datenmacher

EXPOSE 9000

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "wsgi:app"]
