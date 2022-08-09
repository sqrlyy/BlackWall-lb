import requests
from flask import Flask, Response

from utils import load_configuration, get_servers_from_config, healthcheck_servers, get_healthy_server

loadbalancer = Flask(__name__)
config = load_configuration('loadbalancer.yaml')
servers = get_servers_from_config(config)


@loadbalancer.route("/<service>/")
@loadbalancer.route("/<service>/<path:url>")
def load_balance(service='target_service', url=''):
    service_servers = servers.get(service, None)
    if service_servers:
        updated_servers = healthcheck_servers(service_servers)
        print(updated_servers)
        healthy_server = get_healthy_server(updated_servers)
        if not healthy_server:
            return Response('No servers available', status=503)
        response = requests.get(f'http://{healthy_server.endpoint}/{url}')
        return Response(response.content, status=response.status_code)
    return Response('No such services', status=404)


if __name__ == '__main__':
    loadbalancer.run(host="0.0.0.0", debug=True)
