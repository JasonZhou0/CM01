@echo off
pushd %~dp0
Tools\Python\Python37-32\python.exe -B Tools\Python\Python37-32\Scripts\scons.py -c
Tools\Python\Python37-32\python.exe -B Tools\Python\Python37-32\Scripts\scons.py -Q %*
::# --site-dir tool/scons/site_scons %*
if not %errorlevel% == 0 (
  echo Build failed
  pause
  exit /b %errorlevel%
)
popd
echo Done.
pause