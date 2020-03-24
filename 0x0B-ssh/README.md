# SSH

## Resources

### Read or watch:

What is a (physical) server - text
What is a (physical) server - video
SSH essentials
SSH Config File
Public Key Authentication for SSH
How Secure Shell Works
SSH Crash Course

### For reference:


    Understanding the SSH Encryption and Connection Process
    Secure Shell Wiki
    IETF RFC 4251 (Description of the SSH Protocol)
    Internet Engineering Task Force
    Request for Comments


## Learning Objectives


    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash


## Requirements


    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 16.04 LTS
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    All your Bash script files must be executable
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing

| TASKS | DESCRIPTION |
| ---- | ------------- |
| 0-use_a_private_key | Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.|
| 1-create_ssh_key_pair | Bash script that creates an RSA key pair.|
| 2-ssh_config | ou can connect to a server without typing a password.|
