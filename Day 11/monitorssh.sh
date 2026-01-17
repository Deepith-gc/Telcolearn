for i in {1..10}
do
    if nc -z localhost 22 >/dev/null 2>&1; then
        echo "SSH port 22 is OPEN"
    else
        echo "SSH port 22 is CLOSED"
    fi
    sleep 5
done
