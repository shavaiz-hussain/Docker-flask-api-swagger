#!/bin/bash
app="docker.test_3"
docker build -t ${app} .
docker run -d -p 56734:80 \
  --name=${app} \
  -v $PWD:/app ${app}
