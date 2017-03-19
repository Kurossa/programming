#!/bin/bash
# Task from e-mail
# Compile file example.cpp using g++ with debug/release flags
# Use defuned file name as input parameter

INPUT_FILE_TEXT="Enter output file name:"
WARNING_TEXT="Such file name exists, enter new file name:"
DONE_TEXT="Compilation Done"


debug () {
	echo $INPUT_FILE_TEXT
	read file_name
		while [ -e "$file_name" ] ; do
		echo $WARNING_TEXT
		read file_name
		done
	g++ -g -Wall -o $file_name example.cpp
	echo $DONE_TEXT
}

release () {
	echo $INPUT_FILE_TEXT
	read file_name
		while [ -e "$file_name" ] ; do
		echo $WARNING_TEXT
		read file_name
		done
	g++ -O2 -Wall -o $file_name example.cpp
	echo $DONE_TEXT
}

main () {
	clear
	echo "Script compiles example.cpp file"
	echo "1) Debug flag"
	echo "2) Release flag"
	echo "3) Exit script"
	echo "What compilation flag you want to use:"

	read x

	if [ "$x" == "1" ] ; then
		debug

	elif [ "$x" == "2" ] ; then
		release

	elif [ "$x" == "3" ]; then
		echo "Exit, file not compiled."
		exit
	else 
		echo "Not allowed switch!"
		sleep 1
		main
	fi
}

main