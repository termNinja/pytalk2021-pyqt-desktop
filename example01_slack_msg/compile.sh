#!/usr/bin/env bash

declare -a ui_files_to_process=("MainWindow")

for val in "${ui_files_to_process[@]}"
do
    pyuic5 "${val}".ui > "${val}".py

    if [[ $? -ne 0 ]]; then
        echo "Failed compiling $val.ui"
        exit
    else
        echo "Compiled $val.ui"
    fi
done

echo "Compiling resources to resources_rc.py"
pyrcc5 -o resources_rc.py resources.qrc
