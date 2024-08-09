# Copyright (C) 2022 Mikhail Isaev <admin@ismv.ru>

FROM python:3-slim
WORKDIR /app
COPY tnsping.py /app
ENTRYPOINT [ "/app/tnsping.py" ]
