FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Run the FastAPI app from the app module
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

