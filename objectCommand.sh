#!/bin/sh

curl --request POST --url http://192.168.0.10:8081/api/setStatus --header 'accept: application/json' --header 'content-type: application/json' --header 'Access-Control-Allow-Origin: *'  --header 'Access-Control-Allow-Headers: X-Requested-With' --data '{"uID":"0001"}'


