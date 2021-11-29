for line in `cat elasticbeanstalk_input_file`
do
    echo "$line"
    aws elasticbeanstalk describe-environment-resources --environment-name ENVNAME
done

