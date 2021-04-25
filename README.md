# Jenkins Consul Webapp for to retrive k/v
## Just MVP, do not use it anywhere
### TL;DR:
1. Run:  
 `D_ID=$(stat -c '%g' /var/run/docker.sock) D_SOCK=$(which docker) docker-compose up -d`  

2. Open jenkins at localhost:8080 and run both jobs  
3. ###TODO MAKE POST to kv store
4. Retrieve value at flask web app:
  `curl -X GET http://localhost:5000/v1/kv/testkey`  