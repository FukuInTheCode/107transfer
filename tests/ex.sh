(echo -n "./107transfer "; echo -n $(./tests/script.sh $1 $2)) > command; echo "finish gen!!";bash < command; cat command; echo
