import requests


class Server:
    def __init__(self, endpoint, health_path='/healthcheck'):
        self.endpoint = endpoint
        self.health_path = health_path
        self.healthy = True
        self.timeout = 1
        self.scheme = 'http://'

    def update_healthy_status(self):
        try:
            response = requests.get(self.scheme + self.endpoint + self.health_path, timeout=self.timeout)
            print(response.ok)
            self.healthy = bool(response.ok)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            self.healthy = False

    def __repr__(self):
        return f'<Server: {self.endpoint} {self.healthy}>'
