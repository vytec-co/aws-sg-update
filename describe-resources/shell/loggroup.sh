for line in `cat input_file`
do
    echo "$line"
    aws logs describe-log-groups --log-group-name-prefix "Default" --output text >> loggroup_tags.txt
done
