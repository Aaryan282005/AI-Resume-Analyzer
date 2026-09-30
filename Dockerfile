FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout 1800 torch==2.14.0+cpu --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir --timeout 1800 -r requirements.txt

COPY app ./app

RUN mkdir -p data/uploads output

EXPOSE 8000

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]