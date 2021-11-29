#!/bin/sh
# envinfo=aws elasticbeanstalk describe-environment-resources --environment-name ENVNAME | jq '.EnvironmentResources| .Instances[]' | grep "Id"
# while read -r line; do
# instanceid=echo $line | awk -F ':' '{print $2}' | tr -d '"'
# echo $instanceid
# done <<< "$envinfo"

for line in `cat elasticbeanstalk_input_file`
do
    echo "$line"
    aws ec2 describe-instances --instance-id "$line" --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output table
done

