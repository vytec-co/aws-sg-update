for line in `cat sg_input_file`
do
    echo "$line"
    aws ec2 describe-security-groups --group-ids $line --query 'SecurityGroups[*].{GroupName:GroupName,Tags:Tags[?Key == `Name`] | [0].Value}' --output text >> sg_tags.txt
done

