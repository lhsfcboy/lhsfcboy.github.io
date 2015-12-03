@echo off

goto menu

:menu
cls
@echo 1. Use Java 7
@echo 2. Use Java 8


set selc=2
set /p selc=

@echo.
@echo Configuring...
@echo.


IF %selc%==1 goto Java7
IF %selc%==2 goto Java8


:Java7
cls
SET JAVA_HOME="C:\Program Files\Java\jdk1.7.0_79"
ECHO %JAVA_HOME%
pause
exit


:Java8
cls
SET JAVA_HOME="C:\Program Files\Java\jdk1.8.0_45"
ECHO %JAVA_HOME%
pause
exit
