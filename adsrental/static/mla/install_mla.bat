@echo off

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit)

echo [*] Installing MLA wallpaper
powershell iwr https://adsrental.com/static/images/mla_wp.png -OutFile C:\Users\Administrator\mla_wp.png
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d C:\Users\Administrator\mla_wp.png /f
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

if exist C:\mla_2.1.4.zip (
    echo [!] Latest MLA is already downloaded. To download again, please delete C:\mla_2.1.4.zip file
) else (
    echo [*] Downloading latest MLA
    powershell iwr -outf C:\mla_2.1.4.zip https://cdn-download.multiloginapp.com/multilogin/2.1.4/multilogin-2.1.4-windows_x86_32_setup.zip
)

echo [*] Installing MLA
powershell Expand-Archive -force C:\mla_2.1.4.zip -DestinationPath C:\
C:\multilogin-2.1.4.470-windows_x86_32-setup.exe /VERYSILENT

echo [*] Done. You can close this window now and run Multilogin shortcut from desktop

pause
