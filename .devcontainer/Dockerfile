# Find the Dockerfile for mcr.microsoft.com/azure-functions/python:3.0-python3.8-core-tools at this URL
# https://github.com/Azure/azure-functions-docker/blob/master/host/3.0/buster/amd64/python/python38/python38-core-tools.Dockerfile
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8-core-tools

RUN apt-get update &&\
    wget "https://releases.hashicorp.com/terraform/0.13.3/terraform_0.13.3_linux_amd64.zip" && \
    unzip terraform_0.13.3_linux_amd64.zip && \
    mv terraform /usr/local/bin && \
    rm terraform_0.13.3_linux_amd64.zip


