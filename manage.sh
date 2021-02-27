#!/bin/bash

dir_path=$(dirname "$(realpath "$0")")
cd "$dir_path" || exit

app_pid_file="app.pid"

# app.pid 是否存在
app_pid=-1
if [ -f "$app_pid_file" ]; then
    app_pid=$(cat "$app_pid_file")
fi

if [ "$1" == "start" ]; then

    if [ "$app_pid" -gt -1 ]; then
        echo "$app_pid_file already existed. first stop the application or remove it"
    else
        gunicorn -c gunicorn.conf.py app:app
    fi

elif [ "$1" == "stop" ]; then

    if [ "$app_pid" -eq -1 ]; then
        echo "$app_pid_file does not exist."
    else
        kill "$(cat "$app_pid_file")"
    fi

elif [ "$1" == "restart" ]; then

    if [ "$app_pid" -eq -1 ]; then
        echo "$app_pid_file does not exist."
    else
        kill -HUP "$(cat "$app_pid_file")"
    fi

else
    echo "useage: manage.sh [start | stop | restart]"
fi
