#!/bin/zsh
# Use !/bin/bash if on Bash shell.

if [ -z "$1" ]; then
    echo "Nah bro, gimme an argument" # if there is no argument provided
    exit 1
fi

flomo s -t study -n $1 # execute command with given argument
