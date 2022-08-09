# BlackWall-lb

Target app instances - localhost:8081-8086
Loadbalancer instance - localhost:5005


## Installation

```
cd blackwall-lb/
sudo docker compose up --build
```

## Test load balancer

```
ab -k -c 100 -n 20000 localhost:5005/target_service/
```

-c: Concurrency. ndicates how many clients (people/users) will be hitting the site at the same time.

-n: Indicates how many requests are going to be made.


