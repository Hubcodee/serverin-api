import subprocess
import time

from isort import code
from .rand_name import words_fetch
from .terminate_deploy import delete_deploy
# from GLOBAL_INI import *
set_name = set()

# Class MLoad


class Mload:
    def __init__(self, userName):
        self.category = "Mload"
        self.insecure = "--insecure-skip-tls-verify"
        self.type = "NodePort"
        self.user = userName
        self.exposed_port = ()
        self.port = 8888
        self.image = "serverin/jupyter_serverin"
        self.password = "Serverin"

    # Deployment creator method
    def create_deploy(self):
        name = words_fetch().lower()
        print("fetching pod name {name}")
        if name not in set_name:
            set_name.add(name)
            print(f"Name of pod set {set_name}")
        else:
            name = words_fetch()
            set_name.add(name)
            print(f"Name of pod set {set_name}")
        try:
            print(f"Creating deployment {name}")
            # Creating deployment
            deploy = subprocess.getstatusoutput(
                f"kubectl create deployment {name} {self.insecure} --image={self.image}")

            # if successfully deployed then create service
            if deploy[0] == 0:
                print("Deployment created successfully")
                print("Waiting for the pod to be ready")
                time.sleep(5)
# *********************************************************************************
                # # Get pod name here
                # self.pod_name = subprocess.getstatusoutput(
                #     'kubectl get pods --selector=app=%s -o jsonpath="{.items[*].metadata.name}"' % name)
                # print(f"Pod name {self.pod_name}")
# *********************************************************************************
                # Creating service
                expose = subprocess.getstatusoutput(
                    f"kubectl expose deployment {name} {self.insecure} --port={self.port} --type={self.type} ")
                if expose[0] == 0:
                    print("Service created successfully")
                    # time.sleep(5)
                    print("Getting port number of service ...")
                    # Get port Number
                    self.exposed_port = subprocess.getstatusoutput(
                        f"kubectl get svc {self.insecure} {name} -o jsonpath='{{.spec.ports[0].nodePort}}'")
                    print(
                        f"{deploy[1]} is exposed at {self.exposed_port[1]}")

                    # name =  deployment name
                    print("Storing deployment details in DB")
                    # create_record(
                    #     name, self.exposed_port[1], self.category, self.user)
                    return {"status": "success",
                            "message": "Deployment created successfully",
                            "code": 200,
                            "name": name,
                            "port": self.exposed_port[1],
                            "category": self.category,
                            "user": self.user,
                            "deployment": deploy[1]}
                else:
                    print("Service not created")
                    return {"status": "failure",
                            "message": "Service not created",
                            "code": 404}
            else:
                # if deployment failed then exit
                error = subprocess.getstatusoutput("kubectl cluster-info")
                print(error)
                print("Deployment creation failed")
                return {"status": "failure",
                        "message": "Deployment not created",
                        "code": 404}
        except Exception as e:
            return {"status": "failure",
                    "code": 404,
                    "error": e}

        # Terminate deployment method
    def terminate_deploy(self, deployName, user):
        # get deploy name ,running of category - Mload for particular user from DB

        stat = delete_deploy(deployName, self.insecure)
        # print(stat)
        if stat:
            print("Successfully deleted deployment")
            return {"status": "Success",
                    "message": "successfully deleted deployment",
                    "code": 200}
        else:
            print("Failed to delete deployment")
            return {"status": "failure",
                    "message": "Failed to delete deployment",
                    "code": 404}


# print(CLUSTERIP)


# Table - Mload
# DB entry for Mload category


def create_record(self, deployName, exposedPort, serviceCategory, userName, podName):
    pass
