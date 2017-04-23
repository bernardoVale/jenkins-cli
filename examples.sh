#!/bin/bash

jenkins run deploy-qa6-mg-CONTENT_klmcrossbrand-wrk-160524 \
CONTENT_BRANCH=klmcrossbrand-wrk-160524 ENVIRO=qa6 PROJECT=mg FORCEBUILD=false

jenkins(){
    docker run -it --rm \
    -v ~/.jenkins_config.yml:/root/.jenkins_config.yml \
    jenkinscli $@
}