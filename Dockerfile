FROM python:3.10.6-buster
COPY taxifare /taxifare
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY Makefile Makefile
RUN make reset_local_files
CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT
