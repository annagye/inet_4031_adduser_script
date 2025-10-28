#!/usr/bin/python3

# INET4031
# Anna Gye
# Oct 27 2025
# Oct 27 2025

# os lets us run system commands, re is for pattern matching, sys lets us read from standard input
import os
import os
import re
import sys


def main():
    for line in sys.stdin:

       # Check if the line starts with a # (comment line in the input file) and skip it
        match = re.match("^#",line)

        # Split the line by ':' to separate each piece of user inf
        fields = line.strip().split(':')


        # Skip any line that’s a comment or doesn’t have exactly 5 fields
           if match or len(fields) != 5:
            continue

        # Assign variables for each user detail from the input file  
        username = fields[0]
        password = fields[1]
        # Combine first and last names to fit the “gecos” field used in Linux user info
        gecos = "%s %s,,," % (fields[3],fields[2])
        # Split the last field into multiple groups if needed
        groups = fields[4].split(',')

        #  Display message showing which user account is being created
        print("==> Creating account for %s..." % (username))
        # This command creates a new user account without immediately setting a password.
        # The --disabled-password flag prevents login until the password is set.
        # The "cmd" variable stores the full shell command to create the user.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

         # Print the command to the screen (useful for dry runs before actually creating users)
        print(cmd)
         # Execute the command to create the user account
        os.system(cmd)

        # display the message showing the set password for user account
        print("==> Setting the password for %s..." % (username))
        # This command uses "echo" to pass the password twice to the "passwd" command.
        # It automates password entry so the admin doesn't have to type it manually.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Print the password command (again, helpful during dry run)
        print(cmd)

        # Execute the command to actually set the user's password
        os.system(cmd)

        for group in groups:
          # If group is not a placeholder ('-'), add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()#!/usr/bin/env python3
import subprocess

with open('create-users.input', 'r') as f:
    users = f.read().splitlines()

for user in users:
    if user.strip() == "":
        continue
    try:
        subprocess.run(['sudo', 'useradd', '-m', user], check=True)
        print(f"User '{user}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user '{user}'. It may already exist.")
