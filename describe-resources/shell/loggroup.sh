aws logs describe-log-groups \
	--log-group-name-prefix "Default"
for line in `cat input_file`
do
    echo "$line"
    aws ec2 describe-instances --instance-id "$line" --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output table
done
