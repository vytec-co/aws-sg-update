foreach($line in Get-Content .\file.txt) {
    aws ec2 describe-volumes \
    --volume-ids $line | Out-File -FilePath .\output.txt
}


