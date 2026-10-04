# Define the IP range (e.g., 192.168.1.1 to 192.168.1.254)
$SubnetBase = "192.168.1"
$IPRange = 1..254

# Define the ports to test
$Ports = @(21, 22, 80, 443, 445, 3389)

# Generate the full list of IP addresses
$Targets = $IPRange | ForEach-Object { "$SubnetBase.$_" }

# Scan the targets in parallel (Default limit is 5 concurrent threads; adjust via -ThrottleLimit)
$Targets | ForEach-Object -Parallel {
    $IP = $_
    # Use $using: to pass variables from the main scope into the parallel blocks
    foreach ($Port in $using:Ports) {
        $Result = Test-NetConnection -ComputerName $IP -Port $Port -WarningAction SilentlyContinue -InformationLevel Quiet
        if ($Result) {
            Write-Host "[+] $IP : Port $Port is OPEN" -ForegroundColor Green
        }
    }
} -ThrottleLimit 20
