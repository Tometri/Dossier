# Define the IP range and ports
$SubnetBase = "192.168.1"
$IPRange = 1..254
$Ports = @(21, 22, 80, 443, 445, 3389)

Write-Host "Starting background scan jobs..." -ForegroundColor Cyan

# Launch a background job for each IP address
foreach ($ID in $IPRange) {
    $IP = "$SubnetBase.$ID"
    
    Start-Job -ScriptBlock {
        param($TargetIP, $TargetPorts)
        foreach ($Port in $TargetPorts) {
            $Result = Test-NetConnection -ComputerName $TargetIP -Port $Port -WarningAction SilentlyContinue -InformationLevel Quiet
            if ($Result) {
                [PSCustomObject]@{
                    IP   = $TargetIP
                    Port = $Port
                }
            }
        }
    } -ArgumentList $IP, $Ports | Out-Null
}

# Wait for all background jobs to finish and collect results
Write-Host "Waiting for scans to complete..." -ForegroundColor Yellow
$Results = Get-Job | Wait-Job | Receive-Job

# Clean up completed jobs from memory
Get-Job | Remove-Job

# Display results
Write-Host "`n--- OPEN PORTS FOUND ---" -ForegroundColor Cyan
foreach ($Row in $Results) {
    Write-Host "[+] $($Row.IP) : Port $($Row.Port) is OPEN" -ForegroundColor Green
}
