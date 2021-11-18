foreach($line in Get-Content .\file.txt) {
    aws ec2 describe-instances --instance-ids i-1234567890abcdef0 $line | Out-File -FilePath .\output.txt
}
