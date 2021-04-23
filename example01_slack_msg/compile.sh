#!/usr/bin/env bash

declare -a StringArray=("MainWindow")
for val in ${StringArray[@]}; do
    pyuic5 ${val}.ui > ${val}.py

    if [[ $? -ne 0 ]]; then
        echo "${red}Failed compiling $val.ui${reset}"
        exit
    else
        echo "${green}Compiled $val.ui${reset}"
    fi
done

