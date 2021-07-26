#! /bin/bash

DIR=/tmp/.test

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ -d "$DIR" ]; then
    rm -rf "$DIR"
fi

if cookiecutter --no-input -f -o "$DIR" .; then
    printf "\n${GREEN}PASS:${NC} Successfully generated project.\n"
else
    printf "\n${RED}FAIL:${NC} Failed to generate project. Output is above.\n"
    exit 1
fi
