import subprocess
# Deployment deletion method


def delete_deploy(name, insecure):
    try:
        # Delete SVC and Deployment
        del_svc = subprocess.getstatusoutput(
            f"kubectl delete {insecure} svc " + name)
        if del_svc[0] == 0:
            print("Service deleted successfully")
        # Deleting deployment
            deploy = subprocess.getstatusoutput(
                f"kubectl delete deployment {name} {insecure}")
            if deploy[0] == 0:
                print("Deployment deleted successfully")
                return True
            else:
                print("Deployment deletion failed")
                return False
    except Exception as e:
        return (e, 404)
