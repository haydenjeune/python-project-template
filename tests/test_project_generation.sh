#! /bin/bash

# TODO: make sure if one command fails, they all do. look at set -e just watch for caveats

DIR=/tmp/.test

if [ -d "$DIR" ]; then
    rm -rf "$DIR"
fi

cookiecutter --no-input -f -o "$DIR" .
