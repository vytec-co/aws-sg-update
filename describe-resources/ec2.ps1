foreach($line in Get-Content .\file.txt) {
    aws ec2 describe-instances --instance-ids $line >> .\output.txt
}
