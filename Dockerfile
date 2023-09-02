
FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

COPY app /opt/app
COPY requirements.txt /opt/

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV PYTHONPATH="${PYTHONPATH}:app/"

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]