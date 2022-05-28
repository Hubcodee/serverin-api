from MachineLearning import Mload

################ $ LAUNCH DataScience Notebook $ ################
# @Variables:
username = "Ansh-test"

# @Object Instatiate:
obj = Mload(username)

# @Function
obj.create_deploy()

################ $ DELETE DS Notebook $ ################
# @Variables:
deployName = "mats"

# @Function
# obj.terminate_deploy(deployName, username)
