#!/bin/bash
# Task from e-mail
# Compile file example.cpp using g++ with debug/release flags
# Use defuned file name as input parameter

INPUT_FILE_TEXT="Enter output file name:"
WARNING_TEXT="Such file name exists, enter new file name:"
DONE_TEXT="Compilation Done"
COMPILE_FLAGS = ""

print_help () {
	clear
	echo "Script compiles example.cpp file"
	echo "1) Debug flag"
	echo "2) Release flag"
	echo "3) Exit script"
	echo "What compilation flag you want to use:"
}

compile_file () {
	echo $INPUT_FILE_TEXT
	read OUTPUT_FILE_NAME
		while [ -e "$OUTPUT_FILE_NAME" ] ; do
		echo $WARNING_TEXT
		read OUTPUT_FILE_NAME
		done
	g++ $COMPILE_FLAGS -o $OUTPUT_FILE_NAME example.cpp
	echo $DONE_TEXT
}

main () {
	print_help
	read x

	if [ "$x" == "1" ] ; then
		# 1 - Debug version
		COMPILE_FLAGS="-g -Wall" 
		compile_file

	elif [ "$x" == "2" ] ; then
		# 2 - Release version
		COMPILE_FLAGS="-O2 -Wall"
		compile_file

	elif [ "$x" == "3" ]; then
		# 3 - Exit script
		echo "Exit, file not compiled."
		exit
	else 
		echo "Not allowed switch!"
		sleep 1
		main
	fi
}

main