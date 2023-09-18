::@echo off
:: Script to convert png series in a folder to webm movie and mask for use in renpy games.
:: example: Png2Webm.bat fireAttack %2d
set basename=%1
set numbermask=%2
echo basename=%basename% numbermask=%numbermask%
set SourceRoot=F:\[Projects]\RenpyGames\Nova\game\img\animations\%1\

ffmpeg -framerate 10 -i %SourceRoot%%basename%%numbermask%.png %1_real.webm
ffmpeg -r 10 -i %SourceRoot%%basename%%numbermask%.png -filter:v alphaextract %1_mask.webm