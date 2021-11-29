for line in `cat cfn_input_file`
do
    echo "$line"
    aws cloudformation describe-stacks --stack-name $line --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,Tags:Tags[?Key == `Name`] | [0].Value}' --output table
done

