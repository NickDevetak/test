#! /bin/bash
export DATABASE_URL='postgresql://localhost/cucumber'
export APP_SETTINGS='config.StagingConfig'
python app.py
