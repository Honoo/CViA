#!/usr/bin/env bash

git submodule update
cd vendor/cv-parser
npm install
pip install -r requirements.txt
