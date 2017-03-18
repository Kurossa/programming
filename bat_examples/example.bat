@echo off
rem Lukasz Glab
rem swap for english

echo "Task begining"

GOTO:end
echo "Middle task"

:end
echo "End of task"

echo %windir%


set debug=True
echo %debug%

rem Order is important
echo %1 %2

if "%1" == "debug" == (
set debug=True
GOTO:debugfunction
)

if "%1" == "release" == (
set debug=False
GOTO:releasefunction
)

echo Wrong parameter
GOTO:Trueend


:releasefunction
echo RELEASE Compilation %2 debug=%debug%
GOTO:Trueend
:debugfunction
echo DEBUG Compilation %2 debug=%debug%
GOTO:Trueend
:Trueend
@echo End