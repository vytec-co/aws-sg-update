for line in `cat input_file`
do
    echo "$line"
    aws ec2 describe-volumes --volume-ids $line
done


