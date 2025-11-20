read -p "Do you need system stats? " reply
if [ $reply=="Yes" ]; then 
echo lscpu>>log.txt
cat log.txt
free -h
df -h
else
echo "Enter next command"
fi
