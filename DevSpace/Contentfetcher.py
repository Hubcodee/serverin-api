import subprocess
import os
import boto3
from botocore.exceptions import ClientError
import time


class Download:
    def __init__(self, pod_name, userName):
        self.user = userName
        self.pod_name = pod_name
        self.zipname = zipname(self.user)
        self.ssh_cmd = f"python3 /usr/serverin/download.py {self.user} {self.zipname}"
        self.zip_path = f"{self.pod_name}:/home/Serverin/{self.zipname}.zip"
        # self.dest_path = f"/tmp/Download/{self.zipname}.zip"
        self.dest_path = f"downloads/{self.zipname}.zip"
        self.valid = 600
        self.insecure = "--insecure-skip-tls-verify"

    def zip(self):
        try:
            down = subprocess.getstatusoutput(
                f"kubectl exec {self.insecure} {self.pod_name} -- {self.ssh_cmd}")
            if down[0] == 0:
                print(f"Zipped {self.zipname}")
                return True
            else:
                print(f"Not able to download \n{down}")
                return False
        except Exception as e:
            print(f"Not able to connect \n{e}")
            return False
            # return(f"Not able to connect to pod \n{e}")

    def download(self):
        try:
            print(f"Copying {self.zipname}")
            copy = subprocess.getstatusoutput(
                f"kubectl --insecure-skip-tls-verify cp {self.zip_path} {self.dest_path}")
            if copy[0] == 0:
                print(f"Downloaded {self.zipname}")
                return True
            else:
                print(f"Not able to download \n{copy}")
                return False
        except Exception as e:
            print(f"Not able to connect \n{e}")
            return False
            # return(f"Not able to connect \n{e}")

    def upload_s3(self):
        # Upload files to S3
        session_s3 = boto3.session.Session(profile_name="serverin-s3")
        client_s3 = session_s3.client('s3')
        bucket_name = 'serverin-test'

        data_file_folder = "downloads/"
        time.sleep(5)
        filename = f"{self.zipname}.zip"
        for root, dir, files in os.walk(data_file_folder):

            if filename in files:
                print("inside content downloader")
                try:
                    print(f'Uploading file {filename}...'),
                    r = client_s3.upload_file(os.path.join(data_file_folder, filename),
                                              bucket_name,
                                              filename
                                              )
                    print(r)
                    try:
                        resp = client_s3.generate_presigned_url('get_object',
                                                                Params={'Bucket': bucket_name,
                                                                        'Key': filename},
                                                                ExpiresIn=self.valid)
                    except ClientError as e:
                        # The response body contains information about the error.
                        print(e)

                    # Give this url to user at Frontend
                    # print(resp)
                    return {"status": True, "url": resp}
                except ClientError as e:
                    print('Credential is incorrect')
                    print(e)
                    return {"status": False, "url": "Credential is incorrect"}
                except Exception as e:
                    print(e)
                    return {"status": False, "url": "Something went wrong"}
                else:
                    continue
        else:
            print(f'File {filename} not found')
            return {"status": False, "url": "File not found"}
        # try:
        #     print(f'Uploading file {self.zip_path}...'),
        #     client_s3.upload_file(
        #         self.dest_path,
        #         bucket_name,
        #         self.zipname
        #     )
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False
        # except ClientError as e:
        #     print('Credential is incorrect')
        #     print(e)
        #     return False


def zipname(username):
    t = time.localtime()
    current_time = time.strftime("%H-%M-%S", t)
    zipname = username + "_" + current_time
    print("inside zipname")
    return zipname


def presigned_url(bucket_name, object_name, expiration):
    """Generate a presigned URL to share an S3 object"""
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        # The response body contains information about the error.
        print(e)
        return None

    # return the presigned URL
    return response
