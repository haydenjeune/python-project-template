#! /bin/bash
set -euxo pipefail

git init

make install

git add .
git commit -m "Initial commit"
