foreach($line in Get-Content .\file.txt) {
    aws ec2 describe-volumes \
    --volume-ids $line >> .\output.txt
}
for line in `cat input_file`
do
    echo "$line"
    aws ec2 describe-instances --instance-id "$line" --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output table
done


