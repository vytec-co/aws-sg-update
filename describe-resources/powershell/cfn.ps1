foreach($line in Get-Content .\file.txt) {
    aws cloudformation describe-stacks --stack-name $line >> .\output.txt
}
