FROM ubuntu:20.04


RUN ln -sf /usr/share/zoneinfo/America/Mexico_City /etc/localtime
WORKDIR /code

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y gnupg2 curl
RUN curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub | apt-key add -

# Instalar bibliotecas de CUDA y otros paquetes necesarios
RUN apt-get install -y nvidia-cuda-toolkit python3.9 python3-pip


ENV PYHTONUNBUFFERED=1
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH

COPY ./ /code
RUN python -m pip install --upgrade pip
RUN pip3 install numpy scipy scikit-learn
RUN pip3 install -U --no-cache-dir -r /code/requirements.txt

RUN python -m decompress Cod_Red.zip /code/Cod_Red.h5

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]