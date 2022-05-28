import subprocess
import time
from .rand_name import words_fetch
from .terminate_deploy import delete_deploy
# from GLOBAL_INI import *
set_name = set()

# Class Snort


class Snort:
    def __init__(self, userName):
        self.category = "SecurityPlayground"
        self.insecure = "--insecure-skip-tls-verify"
        self.type = "NodePort"
        self.user = userName
        self.exposed_port = ()
        self.port = 22
        self.image = "serverin/serverin_snort"
        self.password = "serverin"
        self.name = words_fetch().lower()
    # Deployment creator method

    def create_deploy(self):
        print("fetching pod name {self.name}")
        if self.name not in set_name:
            set_name.add(self.name)
            print(f"Name of pod set {set_name}")
        else:

            set_name.add(self.name)
            print(f"Name of pod set {set_name}")
        try:
            print(f"Creating deployment {self.name}")
            # Creating deployment
            deploy = subprocess.getstatusoutput(
                f"kubectl create deployment {self.name} {self.insecure} --image={self.image}")

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
                    f"kubectl expose deployment {self.name} {self.insecure} --port={self.port} --type={self.type} ")
                if expose[0] == 0:
                    print("Service created successfully")
                    # time.sleep(5)
                    print("Getting port number of service ...")
                    # Get port Number
                    self.exposed_port = subprocess.getstatusoutput(
                        f"kubectl get svc {self.name} {self.insecure} -o jsonpath='{{.spec.ports[0].nodePort}}'")
                    print(
                        f"{deploy[1]} is exposed at {self.exposed_port[1]}")

                    # name =  deployment name
                    print("Storing deployment details in DB")
                    # create_record(
                    #     self.name, self.exposed_port[1], self.category, self.user)
                    return {"status": "success",
                            "message": "Deployment created successfully",
                            "port": self.exposed_port[1],
                            "name": self.name,
                            "category": self.category,
                            "user": self.user,
                            "deployment": deploy[1],
                            "port": self.exposed_port[1]}
                else:
                    print("Service not created")
                    return {"status": "failure",
                            "message": "Service not created",
                            "code": 404}
            else:
                # if deployment failed then exit
                error = subprocess.getstatusoutput(
                    f"kubectl {self.insecure} cluster-info")
                print(error)
                print("Deployment creation failed")
                return {"status": "failure",
                        "message": "Deployment creation failed",
                        "code": 404}

        except Exception as e:
            return {"status": "failure",
                    "error": str(e),
                    "code": 404}

        # Terminate deployment method
    def terminate_deploy(self, deployName, user):
        # get deploy name ,running of category - Mload for particular user from DB

        stat = delete_deploy(deployName, self.insecure)
        if stat:
            print("Successfully deleted deployment")
            return {"status": "success",
                    "code": 200,
                    "message": "Successfully deleted deployment"}
        else:
            print("Failed to delete deployment")
            return {"status": "failure",
                    "code": 404,
                    "message": "Failed to delete deployment"}

# Class Snort


class Kali:
    def __init__(self, userName):
        self.category = "SecurityPlayground"
        self.insecure = "--insecure-skip-tls-verify"
        self.type = "NodePort"
        self.user = userName
        self.exposed_port = ()
        self.port = 6080
        self.image = "serverin/serverin_kali_desktop"
        self.password = "kali"
        self.name = words_fetch().lower()
    # Deployment creator method

    def create_deploy(self):
        print(f"fetching pod name {self.name}")
        if self.name not in set_name:
            set_name.add(self.name)
            print(f"Name of pod set {set_name}")
        else:
            set_name.add(self.name)
            print(f"Name of pod set {set_name}")
        try:
            print(f"Creating deployment {self.name}")
            # Creating deployment
            deploy = subprocess.getstatusoutput(
                f"kubectl create deployment {self.name} {self.insecure} --image={self.image}")

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
                    f"kubectl expose deployment {self.name} {self.insecure} --port={self.port} --type={self.type} ")
                if expose[0] == 0:
                    print("Service created successfully")
                    # time.sleep(5)
                    print("Getting port number of service ...")
                    # Get port Number
                    self.exposed_port = subprocess.getstatusoutput(
                        f"kubectl get svc {self.name} {self.insecure} -o jsonpath='{{.spec.ports[0].nodePort}}'")
                    print(
                        f"{deploy[1]} is exposed at {self.exposed_port[1]}")

                    # name =  deployment name
                    print("Storing deployment details in DB")
                    # create_record(
                    #     self.name, self.exposed_port[1], self.category, self.user)
                    return {"status": "success",
                            "message": "Kali Deployment created successfully",
                            "port": self.exposed_port[1],
                            "name": self.name,
                            "category": self.category,
                            "user": self.user,
                            "deployment": deploy[1],
                            "port": self.exposed_port[1]}
                else:
                    print("Service not created")
                return {"status": "failure",
                        "message": "Deployment creation failed",
                        "code": 404}
            else:
                # if deployment failed then exit
                error = subprocess.getstatusoutput(
                    "kubectl {self.insecure} cluster-info")
                print(error)
                print("Deployment creation failed")
                return {"status": "failure",
                        "message": "Deployment creation failed",
                        "code": 404,
                        "error": error}
        except Exception as e:
            return (e, 404)

        # Terminate deployment method
    def terminate_deploy(self, deployName, user):
        # get deploy name ,running of category - Mload for particular user from DB

        stat = delete_deploy(deployName, self.insecure)
        if stat:
            return {"status": "success",
                    "code": 200,
                    "message": "Successfully deleted deployment"}
        else:
            return {"status": "success",
                    "code": 404,
                    "message": "Failure deleting deployment"}

# print(CLUSTERIP)


# Table - Mload
# DB entry for Mload category


def create_record(self, deployName, exposedPort, serviceCategory, userName, podName):
    pass
