from SecurePlay import Snort, Kali

################ $ LAUNCH Snort $ ################
# @Variables:
username = "Ansh-test"

# @Object Instatiate:
# obj = Snort(username)

# @Function
# obj.create_deploy()

################ $ DELETE Snort $ ################
# @Variables:
deployName = "shyam"

# @Function
# obj.terminate_deploy(deployName, username)

######################################################################
################ $ LAUNCH Kali $ ################
# @Variables:
username = "Ansh-test"

# @Object Instatiate:
obj = Kali(username)

# @Function
# obj.create_deploy()

################ $ DELETE Snort $ ################
# @Variables:
deployName = "giles"

# @Function
obj.terminate_deploy(deployName, username)
