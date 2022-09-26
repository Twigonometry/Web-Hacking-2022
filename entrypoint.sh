#!/bin/bash
sqlite3 database.db < seed.sql
python app.py