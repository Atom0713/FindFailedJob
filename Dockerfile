FROM python:2.7.18-windowsservercore
# workdirectory within the Docker venv
WORKDIR /user/src/app

COPY parser.py .
COPY test_data.csv .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./parser.py"]





