foreach($line in Get-Content .\file.txt) {
    aws ec2 describe-security-groups --group-ids $line | Out-File -FilePath .\output.txt
}
