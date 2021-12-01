for line in `cat lamda_input_file`
do
    echo "$line"
    aws lambda list-tags --resource "$line"  --output text >> lambda_tags.txt
done

