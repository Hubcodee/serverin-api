from Devspace import Instances, WebIDE, Wordpress

################ $ LAUNCH INSTANCE $ ################
# @Variables:
username = "Ansh-test"
port = 22
image = "serverin/serverin-test-down:v1"

# @Object Instatiate:
obj = Instances(username)

# @Function
# obj.create_deploy(port, image)

################ $ DELETE INSTANCE $ ################
# @Variables:
user = "Ansh-test"
pod_name = "sri-6bb4956ccd-8znsp"
response = True
deploy_name = "sri"

# @Function
obj.terminate_deploy(pod_name, deploy_name, response, user)

#############################################################################################
############# LAUNCH WEBIDE ########################
# @Variables:
username = "Ansh-test"

# @object instantiate:
obj = WebIDE(username)

# @function
# obj.create_deploy()

############# DELETE WEBIDE ########################
# @Variables:
deployName = "dewey"

# @function
# obj.terminate_deploy(deployName, username)

###########################################################################
############# LAUNCH Wordpress ########################
# @Variables:
username = "Ansh-test"

# @object instantiate:
obj = Wordpress(username)

# @function
# obj.create_deploy()

############# DELETE Wordpress ########################
# @Variables:
deployName = "randall"

# @function
# obj.terminate_deploy(deployName, username)
