for line in `cat volume_input_file`
do
    echo "$line"
    aws ec2 describe-volumes --volume-ids $line  --query 'Volumes[*].{VolumeId:VolumeId,Tags:Tags[?Key == `name`] | [0].Value}' --output text >> volume_tags.txt
done


