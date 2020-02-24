# Regular expression

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Resources

### Read or watch:

Regular expressions - basics
Regular expressions - advanced
Rubular is your best friend
Use a regular expression against a problem: now you have 2 problems
Learn Regular Expressions with simple, interactive exercises

## Requirements

Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
All your regex must be built for the Oniguruma library

| TASKS | DESCRIPTION |
| ------ | ----------- |
| 0-simply_match_holberton.rb | The regular expression must match Holberton |
| 1-repetition_token_0.rb | Find the regular expression that will match the above cases | 
| 2-repetition_token_1.rb | Find the regular expression that will match the above cases |
| 3-repetition_token_2.rb | Find the regular expression that will match the above cases |
| 4-repetition_token_3.rb | Find the regular expression that will match the above cases | 
| 5-beginning_and_end.rb | The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between |
| 6-phone_number.rb | The regular expression must match a 10 digit phone number |
| 7-OMG_WHY_ARE_YOU_SHOUTING.rb | The regular expression must be only matching: capital letters |