#!/bin/bash
source venv/Scripts/activate
export FLASK_APP=app
export FLASK_ENV=development  # Optional: for enabling debug mode
flask run
