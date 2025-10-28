#!/usr/bin/python3
# INET4031
# Anna Gye
# Oct 27 2025
# Oct 27 2025


# This program reads user account data from a file (via standard input)
# and creates users, sets passwords, and assigns groups automatically.
#
# DRY-RUN MODE:
# The program asks the user whether to run in "dry-run" mode.
# - If "Y", the program only PRINTS the commands (it DOES NOT execute them).
# - If "N", the program executes the system commands using os.system().
# This allows safe testing before actually modifying the system.

# os lets us run system commands
# re is for pattern matching (regular expressions)
# sys lets us read from standard input
import os
import re
import sys

def main():
    dry_run = input("Would you like to run this in dry-run mode? (Y/N): ").strip().lower()

    for line in sys.stdin:
        # Skip commented lines starting with #
        match = re.match("^#", line)
        fields = line.strip().split(':')

        # Skip bad or comment lines (if dry-run, tell user why)
        if match or len(fields) != 5:
            if dry_run == 'y':
                if match:
                    print("Skipped comment line.")
                else:
                    print("Skipped line with missing fields.")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Create user
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run == 'y':
            print(f"[Dry Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # Set password
        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run == 'y':
            print(f"[Dry Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # Add to groups
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run == 'y':
                    print(f"[Dry Run] Would run: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
