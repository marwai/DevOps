# Virtual Machines 
[140 DevOps](https://github.com/marwai/devops_67_intro)    
[141 README.md](https://github.com/marwai/readme)     
[142 Virtual Machine](https://github.com/marwai/multi_machine_task)  
[143 Reverse Nginx Proxy](https://github.com/marwai/solution-code-environment-vars)  
[144 Cheatsheet](https://github.com/marwai/vagrant_cheatsheet_md)     
[145 Solution to Nginx Proxy](https://github.com/marwai/solution-code-environment-vars)
## Part I 
- [Part I](#Vagrant)
- [Why](#Why?)
- [Developers](#Developers)
- [DevOps](#DevOps)

## Part II
- [Termninology](#Terminology)
- [Install Bundle](#Install-bundle )

## Vagrant

Vagrant is a software development tool used for building building and manging virtual machine environment in a single workflow.
Vagrant focuses on automation, and lowers development set up time, increases production parity. It is a key tool for DevOps
for automation.

## Why? 

Provides provides easy to configure, reproducible and portable work environments to maximise productivity and flexibility. Then 
provisioning tools such as shell scripts, can automatically install and configure software on the virtual machine. 
 
## Developers
Vagrant isolates dependencies and configurations within single flow, provide consistent environment without sacrificing tools,
such as (editors, browsers and debuggers etc.) With the use of  ```vagrant up ```  everything in installed. Others can create 
their develpoment environment from same configuration whether they are on Linux, Mac, OS X, or Windows

## DevOps
As a DevOps Engineer, it will be used for developing and testing infrastructure management scripts. Quick tests can be ran
against shell scripts, puppet modules, and more local virtualisation using VirtualBox or VMware. Even scripts on clouds 
such as AWS with the same workflow. Capababilities of juggling SSH prompts to various machines using vagrant will reduce 
custom scripts to recycle EC2 instances. 

## Vagrant
inside our VM machine 16.04sudo apt-get install -y
- where am I - pwd
- who am I - whoami
- what do I have available in current dir - ls
- how can I find out the name of the system I am using
- How do I find out my current OS - uname
- clear command clears the current whole screen
- How do we create a file - touch "name of file"
- How to create a directory - mkdir "name of directory"

## excercise create two folders: dir1 and dir2
1. in each dir create two files: test1 and test2.txt
2. check the current dir location and document the command to access the dir and exit 

## Terminology 
- cd .. - navigate back to previous folder 
- cd - move to folder
- rm - remove file or dir
- sudo su - change to root user
- id - check who is using the machine 
- echo - print command line 
- exit - go back to user 

- install packages - sudo apt-get install nginx
- check status or programs - 
- Launch nginx in browser            

## Steps to install              
- vagrant up 
- vagrant ssh
- sudo apt-get update -y
- sudo apt- get instal nginx
- systemctl status nginx  

# Starter-code
## Day 2 

- In order to understand it fully we can ask following questions:
```
Communication is the key to succesful projects communications between Dev-Ops-Tester-QA and DevOps
What language is used to build this app?
What framework has been used?
Are they any dependencies to be installed together 
What will the app looklike?
```

1. 
2. Node app requires nodes to be installed. 
3. Ruby to be installed to run the tests 

## install bundle 
- gem install bundler 
- bundle 

## Steps
RAKE SPEC
- rake spec runs the the test written in ruby in the rakefile 
- tests fail 
- install packages for success
- inside vm run:
	- sudo apt-get update
	- sudo apt-get install nginx 
	- systemctl status nginx (checks status)
	- sudo apt-get upgrade
	
	- __install node js__
	- pm2 
	- sudo apt-get install -y nodejs
	- run in root sudo su
	- npm install pm2 -g  

	- cd app 
	- npm install in the app folder 
	- development.localhost:3000
	
	- touch nginx_installation_script.sh
	- chmod +x turns files into executable 
	- chmod +x nginx_installation_script.sh	

# Provisioning with bash scripts
## launch node app
### running tests
- top command```top```
```ps``` command give ProgramID
- ```chmod +x file_name.sh```
- ```cat filename``` - computer aided translation - used in software to print the file without nano 

### Exercise to find the linux codes to assign permission 
[Link](https://www.guru99.com/file-permissions.html)

##syncing folder
```
nano vagrant file
```
Then edit the:
```
config.vm.synced_folder "app", "/home/vagrant/app"

change it to 

config.vm.synced_folder ".", "/home/vagrant/app"

```

## Update, install nginx and upgrade
```
#!/bin/bash

sudo apt-get update
sudo apt-get install nginx
sudo apt-get upgrade


```
## testing dependencies
We run a command to test our VM's dependencies:


rake spec - NOTE: This command is running in the directory of Spec-tests (Outside of the VM machine)

We run a command to install python properties within our VM machine:


sudo apt-get install python-software-properties

These are the steps we took to install Node:



curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

sudo apt-get install -y nodejs



Running an update to make sure all the dependencies and packages are up to date:


sudo apt-get update

Running PM2 package through NPM:


sudo npm install pm2 -g


Running an update again:


sudo apt-get update


## next 

Once we got this working, loading the app directory within the VM and then running another command:

npm install


Running an update again:


sudo apt-get update


Testing to make sure the app is running:


node app.js

## exercise multi-machine lab

The sample application has the ability to connect to a database. We need to provision our development environment with a vm for the database and one for the database.

Vagrant is capable of running two or more virtual machines at once with different configurations.

Tasks:
- Research how to create a multi machine vagrant environment
- Add a second virtual machine called "db" to your Vagrant file
- Configure the db machine with a different IP from the app
- Provision the db machine with a MongoDB database

Notes
When you have the second machine running further configuration of the app is required to make it use the database. We will cover this in the next lesson.

You can test your database is working correctly by running the test suite in the test folder. There are two sets of tests. One for the app VM and one for the db VM. Make them all pass.

cd test
rake spec
- starter-code sent to all trainees
