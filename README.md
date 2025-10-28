# INET4031 Add Users Script and User List

## Program Description

This program is an automated way to add users to a Linux system. Normally, a system administrator would have to type several commands one by one to create each user, set their password, and assign them to groups. This script does all of that automatically by reading information from an input file. It uses the same commands that would normally be entered manually but runs them through Python, saving time and reducing errors when adding many users.

## Program User Operation

This section explains how to use the program and what it does. After reading this section, a user should understand how to set it up and run it properly.

## Input File Format

The input file contains one user per line. Each line has five pieces of information separated by colons: username, password, last name, first name, and group.

Lines that start with a # are treated as comments and skipped.

If a user does not need to belong to a group, a dash (-) is placed in the group field.

Multiple groups can be listed by separating them with commas.

## Command Execution

Before running the script, the file may need to be made executable. Once ready, the script can be run using the sudo command so it has permission to add users. The input file is read into the script using the less-than symbol (<), which sends the file’s contents into the program.

## Dry Run

A dry run allows the user to test the script before actually creating any accounts. In this mode, the commands are only printed on the screen instead of being executed. This helps confirm that everything looks correct. Once the output appears as expected, the user can remove the comment marks in the code to run it for real.
