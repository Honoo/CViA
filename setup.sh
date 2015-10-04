#!/usr/bin/env bash

git submodule init
pip install -r requirements.txt
git submodule update
cd vendor/cv-parser
npm install
