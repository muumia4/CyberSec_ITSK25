# CyberSec
Documentation from CyberSec course
```
Lingid:
Pythoni õpik - https://progeopik.cs.ut.ee/
Clientless VPN (Kehtna) - gp.kehtnakhk.ee
Intra VM 192.168.20.17
```

Käsud
```
#LAB masina tarkvara
#Powershell
winget install --id Microsoft.PowerShell --source winget

#GIT
winget install --id Git.Git -e --source winget
#git config --global user.email sinuIsiklik@email.com (githubi konto)
#git config --global user.name "Eesnimi Perenimi"

#Notepad++
winget install -e --id Notepad++.Notepad++

#Visual Studio Code
winget install -e --id Microsoft.VisualStudioCode

#Python
winget install -e --id Python.Python.3.11

#7-zip
winget install -e --id 7zip.7zip
```

Kali PW reset
```
1. Boot
2. GRUB menüüs vajuta e
3. linux real Asenda splash, guiet ja ro sellega rw init=/bin/bash
4. nano /etc/shadow - siit leian kontod
5. passwd kasutajanimi
```
