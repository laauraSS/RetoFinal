#!/bin/bash
# Requires the database to be up
FLASK_ENV=development DATABASE_URI=postgresql://postgres:mypassword@localhost:5432 python .github/workflows/ci.yaml
