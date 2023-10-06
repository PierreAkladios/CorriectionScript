@echo off
cd /d %~dp0
%CD%
javac -cp "junit-4.13.jar;hamcrest-core-1.3.jar;." TestL8.java
java -cp "junit-4.13.jar;hamcrest-core-1.3.jar;." TestL8
%CD%
pause
cls