#!/bin/bash

/usr/local/bin/docker-compose -f docker-compose.yml kill
/usr/local/bin/docker-compose -f docker-compose.yml rm -f
/usr/local/bin/docker-compose -f docker-compose.yml pull
/usr/local/bin/docker-compose -f docker-compose.yml up -d
