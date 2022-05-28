import subprocess

class HealthCheck:
    def __init__(self):
        self.insecure = "--insecure-skip-tls-verify"
        self.uri = '/readyz?verbose'

    def healthCheck(self):
        deploy = subprocess.getstatusoutput(
            f"kubectl get --raw={self.uri}")
        if deploy[0] == 0:
            return {"status": "healthy", "code": 200}
        else:
            return {"status": "unhealthy", "code": 404}
