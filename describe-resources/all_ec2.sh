aws ec2 describe-instances --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output table
