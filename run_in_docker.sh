#!/bin/bash
docker build -t p_docker .
docker run -ti --rm p_docker $1