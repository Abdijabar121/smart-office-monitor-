FROM python:3.12-slim

WORKDIR /app

RUN useradd -m simuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY simulator.py .

USER simuser

CMD ["python", "simulator.py"]
