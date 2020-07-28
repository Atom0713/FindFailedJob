FROM python:2
# workdirectory within the Docker venv
WORKDIR /user/src/app

COPY parser.py .
COPY test_data.csv .


CMD ["python", "./parser.py"]





