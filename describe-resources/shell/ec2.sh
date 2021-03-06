# aws ec2 describe-instances --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output table

for line in `cat ec2_input_file`
do
    echo "$line"
    aws ec2 describe-instances --instance-id "$line" --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output text >> ec2_tags.txt
done

