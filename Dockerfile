# 🚀 Construcción del frontend
FROM node:18.12.1-buster-slim AS builder
WORKDIR /frontend
COPY ./frontend . 
RUN npm install && npm run build

FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    WORKDIR=/backend

WORKDIR $WORKDIR
RUN python -m pip install --upgrade pip
COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./backend .
COPY --from=builder /frontend/dist /frontend/dist
COPY data.json /data.json
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]