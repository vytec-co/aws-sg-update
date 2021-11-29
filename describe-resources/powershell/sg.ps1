foreach($line in Get-Content .\file.txt) {
    aws ec2 describe-security-groups --group-ids $line >> .\output.txt
}
