import subprocess
import time
from .randName import words_fetch
from .Contentfetcher import Download
from .terminate_deploy import delete_deploy
# from GLOBAL_INI import *
set_name = set()


# Class Instances
class Instances:
    def __init__(self, userName):
        self.category = "Instances"
        self.insecure = "--insecure-skip-tls-verify"
        self.type = "NodePort"
        self.user = userName
        self.exposed_port = ()
        self.pod_name = ()
        # self.port = 4200

    # Deployment creator method

    def create_deploy(self, port, image):
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
                f"kubectl create deployment {name} {self.insecure} --image={image}")

            # if successfully deployed then create service
            if deploy[0] == 0:
                print("Deployment created successfully")
                print("Waiting for the pod to be ready")
                time.sleep(10)

                # Get pod name here
                self.pod_name = subprocess.getstatusoutput(
                    f'kubectl get pods {self.insecure} --selector=app=%s -o jsonpath="{{.items[*].metadata.name}}"' % name)
                print(f"Pod name {self.pod_name}")
                # Creating service
                expose = subprocess.getstatusoutput(
                    f"kubectl expose deployment {name} {self.insecure} --port={port} --type={self.type} ")
                if expose[0] == 0:
                    print("Service created successfully")
                    # time.sleep(5)
                    print("Getting port number of service ...")
                    # Get port Number
                    self.exposed_port = subprocess.getstatusoutput(
                        f"kubectl get svc {self.insecure} {name} -o jsonpath='{{.spec.ports[0].nodePort}}'")
                    print(
                        f"{self.pod_name[1]} is exposed at {self.exposed_port[1]}")

                    # name =  deployment name

                    print("Storing deployment details in DB")
                    # create_record(self,
                    #               name, self.exposed_port[1], self.category, self.user, self.pod_name[1])
                    return {"status": "Passed",
                            "code": 200,
                            "exposedPort": self.exposed_port[1],
                            "podName": self.pod_name[1],
                            "deployName": name,
                            }
                else:
                    print("Service not created")
                    return {"status": "Failed to create service",
                            "code": 404}
            else:
                # if deployment failed then exit
                error = subprocess.getstatusoutput(
                    f"kubectl {self.insecure} cluster-info")
                print(error)
                print("Deployment creation failed")
                return {"status": error,
                        "code": 404}

        except Exception as e:
            return {"status": e,
                    "code": 404}

    # get response from user for downloading content
    def terminate_deploy(self, podName, deployName, response, user):
        # get deploy name ,running of category - devspace for particular user from DB

        # Get User content
        # if user says to terminate without downloading material delete the deployment
        # else download the material and delete the deployment
        if response:
            obj = Download(podName, user)
            if obj.zip():
                print("Downloading in progress ....")
                if obj.download():
                    print("Uploading to S3 in progress ....")
                    url_s3 = obj.upload_s3()
                    print(url_s3)
                    if url_s3["status"]:
                        print("Successfully uploaded ...")
                    else:
                        print("Failed to upload")
                        return {"status": "Failed",
                                "code": 404,
                                "message": "Failed to upload"}
                else:
                    print("Failed to download")
                    return {"status": "Failed",
                            "code": 404,
                            "message": "Failed to download"}

                stat = delete_deploy(deployName, self.insecure)
                if stat:
                    print("Successfully deleted deployment")
                    return {"status": "Passed",
                            "code": 200,
                            "message": "Successfully deleted deployment",
                            "url_s3": url_s3["url"]
                            }
                else:
                    print("Failed to delete deployment")
                    return {"status": "Failed",
                            "code": 404,
                            "message": "Failed to delete deployment"
                            }
            else:
                print("Failed to create zip")
                return {"status": "Failed",
                        "code": 404,
                        "message": "Failed to create zip"
                        }
        else:
            print(
                f"Deleting your current deployment w/o saving your workspace {deployName}...")
            stat = delete_deploy(deployName, self.insecure)
            if stat:
                print("Successfully deleted deployment w/0 saving")
                return {"status": "Passed",
                        "code": 200,
                        "message": "Successfully deleted deployment w/0 saving",
                        }

            else:
                print("Failed to delete deployment")
                return {"status": "Failed",
                        "code": 404,
                        "message": "Failed to delete deployment",
                        }

# print(CLUSTERIP)


# Table - devSpace
# DB entry for WEBIDE category


def create_record(self, deployName, exposedPort, serviceCategory, userName, podName):
    pass


# Class WebIDE
class WebIDE:
    def __init__(self, userName):
        self.category = "WebIDE"
        self.insecure = "--insecure-skip-tls-verify"
        self.type = "NodePort"
        self.user = userName
        self.exposed_port = ()
        self.port = 80
        self.image = "serverin/web-ide"

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
                    return {"status": "Passed",
                            "code": 200,
                            "name": name,
                            "port": self.exposed_port[1],
                            "category": self.category,
                            "user": self.user,
                            "deploy":  deploy[1],
                            "message": "Failed to delete deployment",
                            }

                else:
                    print("Service not created")
                    return {"status": "Failed",
                            "code": 404,
                            "message": "Service not created",
                            }
            else:
                # if deployment failed then exit
                error = subprocess.getstatusoutput("kubectl cluster-info")
                # print(error)
                print("Deployment creation failed")
                return {"status": "Failed",
                        "code": 404,
                        "message": "Failed to create deployment",
                        "error": error
                        }
        except Exception as e:
            return {"error": e,
                    "status": 404}

        # Terminate deployment method
    def terminate_deploy(self, deployName, user):
        # get deploy name ,running of category - devspace for particular user from DB

        stat = delete_deploy(deployName, self.insecure)
        if stat:
            print("Successfully deleted deployment")
            return {"status": "Passed",
                    "code": 200,
                    "message": "Successfully deleted deployment"}
        else:
            print("Failed to delete deployment")
            return {"status": "Failed",
                    "code": 404,
                    "message": "Failed to delete deployment"}

# Class Wordpress


class Wordpress:
    def __init__(self, userName):
        self.category = "Wordpress"
        self.insecure = "--insecure-skip-tls-verify"
        self.type = "NodePort"
        self.user = userName
        self.exposed_port = ()
        self.port = 80
        self.image = "wordpress"

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
                        f"kubectl get svc {name} -o jsonpath='{{.spec.ports[0].nodePort}}'")
                    print(
                        f"{deploy[1]} is exposed at {self.exposed_port[1]}")

                    # name =  deployment name
                    print("Storing deployment details in DB")
                    # create_record(
                    #     name, self.exposed_port[1], self.category, self.user)
                    return {"status": "Passed",
                            "code": 200,
                            "name": name,
                            "port": self.exposed_port[1],
                            "category": self.category,
                            "user": self.user,
                            "deploy":  deploy[1],
                            "message": "Deployment creation successfull",
                            }
                else:
                    print("Service not created")
                    return {"status": "Failed",
                            "code": 404,
                            "message": "Service not created"}
            else:
                # if deployment failed then exit
                error = subprocess.getstatusoutput("kubectl cluster-info")
                print(error)
                print("Deployment creation failed")
                return {"status": "Failed",
                        "code": 404,
                        "message": "Deployment creation failed",
                        "error": error}

        except Exception as e:
            return {"error": e,
                    "status": 404}

        # Terminate deployment method
    def terminate_deploy(self, deployName, user):
        # get deploy name ,running of category - devspace for particular user from DB

        stat = delete_deploy(deployName, self.insecure)
        if stat:
            print("Successfully deleted deployment")
            return {"status": "Passed",
                    "code": 200,
                    "message": "Successfully deleted deployment"}
        else:
            print("Failed to delete deployment")
            return {"status": "Failed",
                    "code": 404,
                    "message": "Failed to delete deployment"}
