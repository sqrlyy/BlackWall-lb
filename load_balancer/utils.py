from schemas import Server
import random
import yaml


def load_configuration(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return dict(config)


def get_servers_from_config(config):
    servers = {}
    for entry in config.get('services', []):
        servers[entry['service']] = [Server(endpoint) for endpoint in entry['servers']]
    return servers


def get_healthy_server(servers):
    try:
        return random.choice([server for server in servers if server.healthy])
    except IndexError:
        return None


def healthcheck_servers(servers):
    for server in servers:
        server.update_healthy_status()
    return servers
