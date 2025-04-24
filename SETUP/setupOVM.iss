[Setup]
AppName=Osu! Voice Menu
AppVersion=0.1
DefaultDirName={pf}\OVM
DefaultGroupName=OVM
OutputDir=.
OutputBaseFilename=OVM_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=build\OVM.ico

[Files]
Source: "build\OVM.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\OVM_GUI.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\OVM.ico"; DestDir: "{app}"; Flags: ignoreversion;

[Icons]
Name: "{group}\OVM!"; Filename: "{app}\OVM.exe"; IconFilename: "{app}\OVM.ico";
Name: "{commondesktop}\Osu! Voice Menu"; Filename: "{app}\OVM.exe"; IconFilename: "{app}\OVM.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Создать ярлык на рабочем столе?"; GroupDescription: "Дополнительно"
Name: "openwebsite"; Description: "Посетить сайт автора после установки"; GroupDescription: "Дополнительно";

[Run]
Filename: "cmd"; Parameters: "/c start http://github.com/dvakerr"; Flags: runhidden; Tasks: openwebsite