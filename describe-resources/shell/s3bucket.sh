for line in `cat s3bucket_input_file`
do
    echo "$line"
    aws s3api get-bucket-tagging --bucket $line --query 'TagSet[*].{Tags:Tags[?Key == `Name`] | [0].Value}' --output txt >>s3_tags.txt
done

