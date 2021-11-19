

while read -r line; do
instanceid=$(aws ec2 describe-instances --instance-ids i-07d469ee66c1342d2 --query 'Reservations[0].Instances[0].InstanceId' --output text)
echo $instanceid
done <<< "$envinfo"
