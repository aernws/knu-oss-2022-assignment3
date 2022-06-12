FROM ubuntu:22.04

RUN apt update && apt -y upgrade
RUN apt install git python3 python3-pip

RUN pip3 install fastapi
RUN pip3 install uvicorn

RUN WORKDIR /root
RUN git clone https://github.com/aernws/knu-oss-2022-assignment3.git

RUN WORKDIR /root/knu-oss-2022-assignment3

CMD ["uvicorn", "main:app", "--reload"]
