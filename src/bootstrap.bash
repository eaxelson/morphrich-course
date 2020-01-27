#!/bin/bash

cd /home/jovyan/work

export GIT_COMMITTER_NAME=anonymous
export GIT_COMMITTER_EMAIL=anon@localhost

git clone https://github.com/eaxelson/morphrich-course.git
cd /home/jovyan
cp -r /home/jovyan/work/morphrich-course /home/jovyan/Lectures

python3 -m pip install graphviz
python3 -m pip install hfst-dev

cd /home/jovyan/Lectures
rm -fR Lecture6
rm -fR src
rm -f README.md
mv README_FOR_USER.md README.md
