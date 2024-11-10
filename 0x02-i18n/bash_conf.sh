#!/usr/bin/env bash
# Initializing translations
pybabel extract -F babel.cfg -o messages.pot .
# dicionaries
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
# edit the files then run the last command to compile the dictionaries
# pybabel compile -d translations
