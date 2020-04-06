# HTTPS SSL

## Resources

    What is HTTPS?
    What are the 2 main elements that SSL is providing
    HAProxy SSL termination on Ubuntu16.04
    SSL termination
    Bash function

## Learning Objectives

    What is HTTPS SSL 2 main roles
    What is the purpose encrypting traffic
    What SSL termination means

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
| 0-https_abc | HTTPS ABC |
| 1-world_wide_web | Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01)|
| 2-haproxy_ssl_termination | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www. |
