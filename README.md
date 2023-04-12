# SERVERIN-API
 ServerIn act as Platform as a Service (PaaS)
 It aims to provide computing resources to community on their fingertips. 
 They would be able to code, build, run, test and deploy their applications as per their requirements. 
 This design plans to provide facilities like – online web editor, deploying your code over Kubernetes cluster, getting your ML data automatically trained, setting up a system like your own local PC. 
 These facilities are automated using automation tools like Ansible, Terraform and Jenkins CI/CD.
 
 # OBJECTIVES
 1. Using the concept of containerization and virtualization to acheive the environment similar to bare metal.
 2. Using Terraform, Ansible automation tool for launching and configuring various servers.
 3. Using managed services by cloud like AWS in order to integrate multiple technologies over cloud.
 4. Provisioning highly available infrastructure for testing and development purposes.
 
 # RELEVANCE OF TECHNOLOGIES 
 1. Python - programming language is used since it supports multiple programming paradigms and synamic system, automatic memory management. 
 2. Ansible is used to automate the scripts to run the services.
 3. roles have been created for every service so that the required services can be available to the user. These roles automates the launching of computind units over AWS Cloud.
 4. Docker deploys the services.
 5. Kubernetes manages multiple containers, scaleup, scale down and restart them.
 6. Jenkis monitors the repeated tasks which arise during the development of a project.
 7. Terraform is used to build, change and version infrastructure safely and efficiently.
 
# APIs formed under SERVERIN
 1. DevSpace API 
      It is responsible to launch and deploy instances over kubernetes service and give endpoint.
      It deploys web IDE and WordPress application which is open to world.
 2. MLoad API
      It is responsible for launching the Jupyter web based instance where user can use various machine learning modules, train the models, test the models and deploy the model. 
 3. Security Playground API
      It is responsible for launching the security playground Kali-Linux and snort tool enviornment.

# SERVERIN ARCHITECTURE
    <img src="/serverin-api/blob/main/images/Serverin%20Dashboard.png" title="Architecture">
    
    https://github.com/Hubcodee/serverin-api/blob/main/images/Internal%20Serverin%20Service%20Strcuture.png
    
# User Interface
    Serverin Dashboard- https://github.com/Hubcodee/serverin-api/blob/main/images/Serverin%20Dashboard.png
    
    Published Projects - https://github.com/Hubcodee/serverin-api/blob/main/images/published%20projects.png
    
    Code Deployer - https://github.com/Hubcodee/serverin-api/blob/main/images/Code%20Deployer.png
    
    Web IDE - https://github.com/Hubcodee/serverin-api/blob/main/images/web%20IDE.png
              https://github.com/Hubcodee/serverin-api/blob/main/images/web%20IDE%20part%202.png
              
    MLoad - https://github.com/Hubcodee/serverin-api/blob/main/images/ML%20load.png
    
    ML Pipeline - https://github.com/Hubcodee/serverin-api/blob/main/images/ml%20pipeline.png
    
    Security Playground - https://github.com/Hubcodee/serverin-api/blob/main/images/security%20playground.png
    
    Attendance System - https://github.com/Hubcodee/serverin-api/blob/main/images/attendance%20system.png
    
# Demo
https://youtu.be/xgNc8xL9obk
    
    


    

      
      

 
