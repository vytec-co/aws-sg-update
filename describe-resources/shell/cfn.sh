for line in `cat cfn_input_file`
do
    echo "$line"
    aws cloudformation describe-stacks --stack-name $line --output text >> cfn_tags.txt
done

