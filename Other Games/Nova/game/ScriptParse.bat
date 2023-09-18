::@echo off
setlocal enabledelayedexpansion
set SourceRoot=F:\[Projects]\RenpyGames\Nova\game\[in]
set TargetRoot=F:\[Projects]\RenpyGames\Nova\game\[out]
set FileMask=*.*
for /r "%SourceRoot%" %%a in (%FileMask%) do (
	echo Processing [%%~ta] %%~fa
	::for /f "tokens=1-3 delims=/ " %%f in ("%%~ta") do (
	::	set DD=%%f
	::	set MM=%%g
	::	set YYYY=%%h
	::)
	::set TargetFolder=!YYYY!-!MM!-!DD!
	::if not exist "%TargetRoot%\!YYYY!\!TargetFolder!" md "%TargetRoot%\!YYYY!\!TargetFolder!"
	::C:\Python27\python.exe Nova_TextToRenpy.py "%%~fa" "nova_story_chapter%%~fa.done"
	C:\Python27\python.exe Nova_TextToRenpy.py "%%~fa" "%%~fa.done"
  move "%%~fa.done" "%TargetRoot%\"
  
)