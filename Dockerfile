FROM continuumio/miniconda3:latest

LABEL author="Louis B"
LABEL description="DockerImage for Steamlit Trimble "

COPY environment.yml /app/environment.yml


WORKDIR /app

RUN conda env create -f environment.yml
RUN conda activate trimble_tf1
RUN echo "environment is succefuly created"

EXPOSE 8501

COPY app/ .
# ENTRYPOINT [ "python3","/exemple/startup.py" ]


ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# CMD ["python3","/exemple/test.py"]