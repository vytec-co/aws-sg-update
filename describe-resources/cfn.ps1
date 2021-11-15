foreach($line in Get-Content .\file.txt) {
     info=$(aws cloudformation describe-stacks --stack-name $line)
     Write-Host $val
}
