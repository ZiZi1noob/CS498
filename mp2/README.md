# cs498 
uiuc cs498 -- mp2


1. create EC2
2. upload .py scirp to ec2

    a. access to ec2
    
    b. sudo su
    
    c. yum update
    
    d. yum install git
    
    e. git clone [address]
    
    f. yum install python3-pip
    
    g. python3 -m pip install flask
    
    h. ps -ef  / lsof -i :80 /   kill [pid#]
    
    
    •	running server
    
        - python3 [name.py]
        
        - flask --app [name of .py] run --host=0.0.0.0 --port=xxxx
        
        - curl -X POST -H "content-Type:application/json” -d '{"num":100}' [public address]:[port]

    •	Use the same flask port number in your test.py file for the two EC2 instances, and Target Groups
    
    •	Your Security Group should allow all HTTP traffic and a Custom TCP rule for your flask port number
    
    •	Load Balancer can be listening to Port 80

