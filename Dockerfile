FROM python:3-slim
WORKDIR /app
COPY tnsping.py /app
ENTRYPOINT [ "/app/tnsping.py" ]