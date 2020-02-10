# 0x05. Processes and signals

## Resources

### Read or watch:

Linux PID
Linux process
Linux signal

## Learning Objectives

### General

What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored

## Requirements

### General

Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

|TASKS | DESCRIPTION|
|---------|------------|
|0-what-is-my-pid | Bash script that displays its own PID|
|1-list_your_processes | Bash script that displays a list of currently running processes|
|2-show_your_bash_pid | Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process |
|3-show_your_bash_pid_made_easy | Bash script that displays the PID, along with the process name, of processes whose name contain the word bash |
|4-to_infinity_and_beyond | Bash script that displays To infinity and beyond indefinitely |
|5-kill_me_now | Bash script that kills 4-to_infinity_and_beyond process. |
|6-kill_me_now_made_easy | Bash script that kills 4-to_infinity_and_beyond process |
|7-highlander |  Bash script that displays .To infinity and beyond indefinitely .With a sleep 2 in between each iteration .I am invincible!!! when receiving a SIGTERM signal |
|8-beheaded_process | Bash script that kills the process 7-highlander |