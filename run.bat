@ECHO OFF
Setlocal EnableDelayedExpansion
set /p folder=Please enter folder:
set /p url=Please enter the url of novels:
set /p start= Please enter start chapter:
set /p stop= Please enter stop chapter:

python D:\Python3\Source\tangthuvien\run.py -i %url% -l %start% -d %stop% -f %folder%

pause