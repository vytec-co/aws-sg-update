
for line in `cat elb_input_file`
do
    echo "$line"
    aws elbv2 describe-load-balancers --names $line --query LoadBalancers[].{DNSName:DNSName,Tags:Tags[?Key == `Name`] | [0].Value}' --output text >> elb_tags.txt
done
