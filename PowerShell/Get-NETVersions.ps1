#Lookup table for .NET versions
$Lookup = @{
    378389 = [version]'4.5'
    378675 = [version]'4.5.1'
    378758 = [version]'4.5.1'
    379893 = [version]'4.5.2'
    393295 = [version]'4.6'
    393297 = [version]'4.6'

}

Get-ChildItem 'HKLM\SOFTWARE\Microsoft\NET Framework Setup\NDP' -Recurse | Get-ItemProperty -Name Version, Release -ErrorAction 0 | Where-Object { $_.PSChildName -match '^(?!S)\p{L}'} | Select-Object @{name = ".NET Framework"; expression = {$_.PSChildName}}, @{name = "Product"; expression = {$Lookup[$_.Release]}}, Version, Release