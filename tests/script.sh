generate_expression() {
    length=$1
    expression=""
    for ((i=1; i<=length; i++)); do
        expression+="$(shuf -i 1-9 -n 1)"
        if ((i < length)); then
            expression+="*"
        fi
    done
    echo "$expression"
}

num_expressions_to_generate=$1
max_length_of_each_expression=$2

for ((i=1; i<=num_expressions_to_generate; i++)); do
    expression_length=$((RANDOM % max_length_of_each_expression + 1))
    generated_expression=$(generate_expression $expression_length)
    echo "\"$generated_expression\""
done
