while IFS= read -r line; do
    info=$(aws cloudformation describe-stacks --stack-name $line)
    echo $info  >> stack_deails.txt
done < my_filename.txt
