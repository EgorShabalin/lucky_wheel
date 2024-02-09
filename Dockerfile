FROM python:3.9

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]