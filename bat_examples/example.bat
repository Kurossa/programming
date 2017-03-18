@echo off
rem Lukasz Glab


echo "Poczatek zadania"

GOTO:end
echo "Srodek zadania"

:end
echo "Koniec zadania"

echo %windir%


set debug=True
echo %debug%

rem Kolejnoœæ ma znaczenie
echo %1 %2

if "%1" == "debug" == (
set debug=True
GOTO:debugfunction
)

if "%1" == "release" == (
set debug=False
GOTO:releasefunction
)

echo Bledny parametr
GOTO:Trueend


:releasefunction
echo Kompilacja RELEASE %2 debug=%debug%
GOTO:Trueend
:debugfunction
echo Kompilacja DEBUG %2 debug=%debug%
GOTO:Trueend
:Trueend
@echo Koniec