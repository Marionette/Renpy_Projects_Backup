; -- NovaInstall.iss --

#define MyAppName "Nova: Synthesis Creaturum"   
#define MyAppDirName "Nova - Synthesis Creaturum"                                                              
#define ExeName "Nova_Synthesis_Creaturum"

[Setup]
AppName={#MyAppName}
AppVersion=0.11
DefaultDirName={pf}\{#MyAppDirName}
DefaultGroupName={#MyAppDirName}
UninstallDisplayIcon={app}\{#ExeName}.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output   
OutputBaseFilename={#ExeName}_install
SetupIconFile=game\icon.ico

[Files]
Source: "game\*"; DestDir: "{app}\game"; Flags: ignoreversion recursesubdirs     
Source: "lib\*"; DestDir: "{app}\lib" ; Flags: ignoreversion recursesubdirs     
Source: "{#ExeName}.app\*"; DestDir: "{app}\{#ExeName}.app"; Flags: ignoreversion recursesubdirs 
Source: "renpy\*"; DestDir: "{app}\renpy"; Flags: ignoreversion recursesubdirs   
Source: "{#ExeName}.exe"; DestDir: "{app}"   
Source: "{#ExeName}.py"; DestDir: "{app}"   
Source: "{#ExeName}.sh"; DestDir: "{app}"   
Source: "README.html"; DestDir: "{app}"

[Icons]
Name: "{group}\{#MyAppDirName}"; Filename: "{app}\{#ExeName}.exe"
Name: "{group}\README"; Filename: "{app}\README.html"          
Name: "{group}\Uninstall {#MyAppDirName}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#ExeName}"; Filename: "{app}\{#ExeName}.exe"
;Name: "{commonprograms}\{#ExeName}"; Filename: "{app}\{#ExeName}.exe"
;Name: "{commonstartup}\{#ExeName}"; Filename: "{app}\{#ExeName}.exe"
