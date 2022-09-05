FROM python:3.8

VOLUME /nginx

COPY nginxGenerateConfig.py ./
COPY nginx-template.config ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir jinja2

CMD ["python", "./nginxGenerateConfig.py"]