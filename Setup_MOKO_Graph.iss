#define SourceDir "D:\GitHub\MOKO\MOKO_GRAPH\App"
#define AppName "MOKO Graph"
#define GraphLink "MOKO Graph"
#define GraphExe "MOKO Graph"
#define AppPublisher "MOKO"
#define AppVersion "2.09.26.2"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same Am nppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F7E380BF-C77A-43BE-9154-9D7E266E5F92}
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
//Source: "Example script\*"; DestDir: "{app}\Example scripts" ;  Flags: ignoreversion  uninsremovereadonly
//Source: "Example script\Present Project\*"; DestDir: "{app}\Example scripts\Present Project" ;  Flags: ignoreversion  uninsremovereadonly

[Icons]
Name: "{commondesktop}\{#GraphExe}"; Filename: "{app}\{#GraphExe}.exe";
Name: "{group}\{#GraphExe}"; Filename: "{app}\{#GraphExe}.exe";

[Code]

[Run]














