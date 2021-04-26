# Jenkins Consul Webapp for to retrive k/v
## Just MVP, do not use it anywhere
### Requirements:
python-pip
docker-compose (was tested on ubuntu20)
curl
user with privileges to run docker or sudo user (docker-compose then should be installed globally)
### TL;DR:
1. Clone repo:  
 `git clone https://github.com/PavelPaladin/jencons-compose.git && cd jencons-compose`  

2. Run in repo folder:  
 `D_ID=$(stat -c '%g' /var/run/docker.sock) D_SOCK=$(which docker) docker-compose up -d`  
 
3. Open jenkins at localhost:8080 and run both jobs  

4. Set our key=value:  
 `curl -X POST http://localhost:5000/set_value?some-key=some-value`

5. Retrieve value at flask web app or:  
 `curl -X GET http://localhost:5000/v1/kv/key=some-key`  


## Development considerations
 - everything in docker  
 - all security stuff and error handling was omitted
 - currently supports only one key\value pair
 - tried to avoid any bash scripts because I think it's last resort measure (+ it looks doable)
 - didn't find any reason to bring up the multinode cluster, so went lazy way and used one instance (but could be extended ofc)
 - used an outdated but easy-to-use registator for cunsul in docker (ofc could be changed to smt else, but it saved a lot of time)
 - I know only basic functional programming, first time doing webapp..so, sorry for poor looking code ;)
