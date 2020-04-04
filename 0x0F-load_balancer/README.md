# 0x0F. Load balancer

## Background Context

We have been given 2 additional servers:

    gc-[STUDENT_ID]-web-02-XXXXXXXXXX
    gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources


    Introduction to load-balancing and HAproxy
    HTTP header
    Debian/Ubuntu HAProxy packages

## Requirements


    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 16.04 LTS
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    All your Bash script files must be executable
    Your Bash script must pass Shellcheck (version 0.3.7) without any error
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing

| TASKS | DESCRIPTION |
| ----- | ----------- |
| 0-custom_http_response-header | Double the number of webservers |
| 1-install_load_balancer | Install your load balancer |
| 2-puppet_custom_http_response-header.pp | Add a custom HTTP header with Puppet |
