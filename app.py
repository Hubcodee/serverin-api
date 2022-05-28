from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
# from flask_restful import Api, Resource
from DevSpace.Devspace import Instances, WebIDE, Wordpress
from MachineLearning.MachineLearning import Mload
from SecurityPlayground.SecurePlay import Snort, Kali
from HealthCheck.health import HealthCheck
# import json
app = Flask(__name__)
# api = Api(app)


@app.route("/api/v1/health", methods=['GET'])
def home():
    user = request.args.get('username')
    obj = HealthCheck()
    res = obj.healthCheck()
    print(res)
    return jsonify({"message": "Welcome to Serverin",
                    "status_code": res['status'],
                    "api_version": "1.0.0",
                    "api_author": "Serverin Community",
                    "api_status": res['code'],
                    "user": user})


########################@ DevSpace @###################################

# *************************INSTANCES********************************


@ app.route("/api/v1/devspace/instances/launch", methods=['GET'])
def dev_inst_launch():
    userName = request.args.get('username')
    port = request.args.get('port')
    image = request.args.get('image')
    obj = Instances(userName)
    res = obj.create_deploy(port, image)
    # print(res)
    op = {"message": "Welcome to DevSpace Instances Launch Service",
          "username": userName,
          "image": image,
          "deployName": res['deployName'],
          "exposedPort": res['exposedPort'],
          "status": res['status'],
          "podName": res['podName']}
    return jsonify(op)
    # return render_template('index.html', res=res)


@ app.route("/api/v1/devspace/instances/terminate", methods=['GET'])
def dev_inst_terminate():
    userName = request.args.get('username')
    pod_name = request.args.get('pod_name')
    deploy_name = request.args.get('dep_name')
    response = request.args.get('resp')
    obj = Instances(userName)
    res = obj.terminate_deploy(pod_name, deploy_name, response, userName)
    return jsonify({"message": "Welcome to DevSpace Instances Terminate Service",
                    "userName": userName,
                    "podName": pod_name,
                    "deployName": deploy_name,
                    "response": response,
                    "res": res})
# *****************************************************************
# ************************* @ WebIDE @ *****************************


@ app.route("/api/v1/devspace/webide/launch", methods=['GET'])
def devspace_webide_inst():
    userName = request.args.get('username')
    obj = WebIDE(userName)
    res = obj.create_deploy()
    return jsonify({"message": "Welcome to DevSpace WebIde Service",
                    "userName": userName,
                    "result": res})


@ app.route("/api/v1/devspace/webide/terminate", methods=['GET'])
def devspace_webide_term():
    userName = request.args.get('username')
    deployName = request.args.get('deployName')
    obj = WebIDE(userName)
    res = obj.terminate_deploy(deployName, userName)
    return jsonify({"message": "Welcome to DevSpace WebIde Service",
                    "result": res})

# *****************************************************************
# ************************* @ WordPress @ ************************************


@ app.route("/api/v1/devspace/wordpress/launch", methods=['GET'])
def devspace_wordpress_launch():
    userName = request.args.get('username')
    obj = Wordpress(userName)
    res = obj.create_deploy()
    return jsonify({"message": "Welcome to DevSpace WordPress Service", "result": res})


@ app.route("/api/v1/devspace/wordpress/terminate", methods=['GET'])
def devspace_wordpress_terminate():
    userName = request.args.get('username')
    deployName = request.args.get('deployName')
    obj = Wordpress(userName)
    res = obj.terminate_deploy(deployName, userName)
    return jsonify({"result": res})

##############################@ END @####################################

############################@ CodeDeployer @#############################
#########################################################################


############################@ MachineLearning @##########################
@ app.route("/api/v1/machinelearning/launch", methods=['GET'])
def machinelearning_launch():
    userName = request.args.get('username')
    obj = Mload(userName)
    res = obj.create_deploy()
    return jsonify({"result": res})


@ app.route("/api/v1/machinelearning/term", methods=['GET'])
def machinelearning_term():
    userName = request.args.get('username')
    deployName = request.args.get('deployName')
    obj = Mload(userName)
    res = obj.terminate_deploy(deployName, userName)
    return jsonify({"result": res})
#########################################################################

############################@ SecurityPlayground @#######################


@ app.route("/api/v1/secureplay/snort/launch", methods=['GET'])
def secureplay_snort_launch():
    userName = request.args.get('username')
    obj = Snort(userName)
    res = obj.create_deploy()
    return jsonify({"result": res})


@ app.route("/api/v1/secureplay/snort/terminate", methods=['GET'])
def secureplay_snort_term():
    userName = request.args.get('username')
    deployName = request.args.get('deployName')
    obj = Snort(userName)
    res = obj.terminate_deploy(deployName, userName)
    return jsonify({"result": res})


@ app.route("/api/v1/secureplay/kali/launch", methods=['GET'])
def secureplay_kali_launch():
    userName = request.args.get('username')
    obj = Kali(userName)
    res = obj.create_deploy()
    return jsonify({"result": res})


@ app.route("/api/v1/secureplay/kali/terminate", methods=['GET'])
def secureplay_kali_term():
    userName = request.args.get('username')
    deployName = request.args.get('deployName')
    obj = Kali(userName)
    res = obj.terminate_deploy(deployName, userName)
    return jsonify({"result": res})
#########################################################################


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
