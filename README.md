# Jenkins Consul Webapp for to retrive k/v
## Just MVP, do not use it anywhere
### Requirements:
docker-compose (was tested on ubuntu20)
curl
### TL;DR:
1. Run:  
 `D_ID=$(stat -c '%g' /var/run/docker.sock) D_SOCK=$(which docker) docker-compose up -d`  

2. Open jenkins at localhost:8080 and run both jobs  
3. Set our key=value:
  `curl -X POST http://localhost:5000/set_value?some-key=some-value`
4. Retrieve value at flask web app or:
  `curl -X GET http://localhost:5000/v1/kv/some-key`  


## Development considerations
 - everything in docker  
 - all security stuff and error handling was omitted
 - currently supports only one key\value pair
 - tried to avoid any bash scripts because I think it's last resort measure (+ it looks doable)
 - didn't find any reason to bring up the multinode cluster, so went lazy way and used one instance (but could be extended ofc)
 - used an outdated but easy-to-use registator for cunsul in docker (ofc could be changed to smt else, but it saved a lot of time)
 - I know only basic functional programming, first time doing webapp..so, sorry for poor looking code ;)


