FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1/

COPY Mall_Customers.csv /home/doc-bd-a1/
COPY load.py dpre.py eda.py vis.py model.py /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1

# Add the virtual environment to the PATH
ENV PATH="/opt/venv/bin:$PATH"

CMD ["/bin/bash"]
