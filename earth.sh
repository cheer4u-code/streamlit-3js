#!/usr/bin/sh

if grep -q WSL2 /proc/version; then
    export BROWSER='/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
fi
export STREAMLIT_SERVER_ADDRESS='localhost'

exec venv/bin/streamlit run app.py
