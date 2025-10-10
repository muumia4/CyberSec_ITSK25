Clear-Host

#Küsin kasutajalt matriksi suurust (3-10)
[int]$rows = Read-Host "Matriksi suurus (3-10): "
$collumns = $rows 
$dst = Join-Path -Path $PSScriptRoot -ChildPath "output.txt" #Output

#Genereeri matriks vastuse põhjal numbitega 1-99
if(($rows -ge 3) -and ($rows -le 10)){
    if(Test-Path $dst) { #Testime kas fail juba eksiteerib
        Remove-Item $dst
    }

    for($i = 0; $i -lt $rows; $i++){
        $line = ""

        for($n = 0; $n -lt $collumns; $n++){
            $randomnr = Get-random -Minimum 1 -Maximum 99
            
            #Ühekohalised numbrid saavad ette 0
            if(($randomnr -ge 1) -and ($randomnr -le 9)){
                $randomnr = "0" + $randomnr
                $line += ("{0,3}" -f $randomnr)
            } else {
                $line += ("{0,3}" -f $randomnr)
            }
        }
        #Väljasta tulemus output.txt
        Add-Content -Path $dst -Value $line

    }
    Write-Host "Fail salvestatud asukohta $dst"
} else {
    Write-Host "Vale suurus. Sisesta number 3-10"
}

