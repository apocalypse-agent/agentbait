FROM python:3.12-slim

WORKDIR /app

COPY agent /agent
COPY tools /tools
COPY sandbox /sandbox

CMD ["python", "/agent/agent.py"]
