#!/bin/sh
envinfo=aws elasticbeanstalk describe-environment-resources --environment-name ENVNAME | jq '.EnvironmentResources| .Instances[]' | grep "Id"
while read -r line; do
instanceid=echo $line | awk -F ':' '{print $2}' | tr -d '"'
echo $instanceid
done <<< "$envinfo"
