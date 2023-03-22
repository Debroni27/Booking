#!/bin/bash

connected=false

while ! $connected; do
    if nc -z mongodb 27017; then
        echo "DB Connection -- Successful!"
        connected=true
    else
        echo "DB Connection -- Failed!"
        sleep 1
        echo "DB Connection -- Retrying . . ."
    fi
done

uvicorn backend.src.main:backend_app --reload --workers 4 --host 0.0.0.0 --port 8000

