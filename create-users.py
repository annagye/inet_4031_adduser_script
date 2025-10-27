#!/usr/bin/env python3
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
