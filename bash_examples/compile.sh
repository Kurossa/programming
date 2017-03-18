#!/bin/bash
#Zadanie z maila
#Kompilacja pliku example.cpp debug/release za pomocą g++
# z użuciem dowolnej nazwy

debug () {
	echo "Podaj nazwę pliku wyjściowego:"
	read nazwa
		while [ -e "$nazwa" ] ; do
		echo "Plik o takiej nazwie już istnieje. Podaj nową nazwę:"
		read nazwa
		done
	g++ -g -Wall -o $nazwa example.cpp
	echo "Wykonano kompilację debug"
}

release () {
	echo "Podaj nazwę pliku wyjściowego:"
	read nazwa
		while [ -e "$nazwa" ] ; do
		echo "Plik o takiej nazwie już istnieje. Podaj nową nazwę:"
		read nazwa
		done
	g++ -O2 -Wall -o $nazwa example.cpp
	echo "Wykonano kompilację release"
}

echo "Witaj"
echo "Program kompiluje plik example.cpp"
echo "1) Debug"
echo "2) Release"
echo "3) Wyjście"
echo "Podaj rodzaj kompilacji:"

read x



if [ "$x" == "1" ] ; then
	debug

elif [ "$x" == "2" ] ; then
	release

elif [ "$x" == "3" ]; then
	echo "Do widzenia"
	exit

else echo "Nieznana kompilacja"
fi