#define SourceDir "D:\GitHub\MOKO\MOKO_GRAPH\App"
#define AppName "MOKO Graph"
#define MOKOGraphLink "MOKO Graph"
#define MOKOGraphExe "MOKO Graph"
#define AppPublisher "MOKO Graph"
#define AppVersion "0.06.19.1"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same Am nppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{A9BE419A-49E8-4942-8D7F-6057BAE01580}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName=C:\MOKO SE\Plugins\MOKO Graph\
DisableDirPage=auto
DefaultGroupName={#AppPublisher}
DisableProgramGroupPage=auto
LicenseFile="iss\license.txt" 
OutputDir="installer"
OutputBaseFilename=Setup_MOKO_Graph_{#AppVersion}
SetupIconFile="Icon\MOKO Graph IN.ico" 
Compression=lzma2/ultra64
SolidCompression=yes
DisableFinishedPage=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
;Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
           

[Files]
Source: "App\*"; DestDir: "{app}\" ;  Flags: ignoreversion  uninsremovereadonly
Source: "Example script\*"; DestDir: "{app}\Example scripts" ;  Flags: ignoreversion  uninsremovereadonly
Source: "Example script\Present Project\*"; DestDir: "{app}\Example scripts\Present Project" ;  Flags: ignoreversion  uninsremovereadonly

[Icons]
Name: "{commondesktop}\{#MOKOGraphExe}"; Filename: "{app}\{#MOKOGraphExe}.exe";
Name: "{group}\{#MOKOGraphExe}"; Filename: "{app}\{#MOKOGraphExe}.exe";

[Code]

[Run]














