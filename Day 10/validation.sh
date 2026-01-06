
read -p  "Enter your name:" name
read -p "Enter your age:" age
echo $age
if [ -z "$name" ];then
echo "Name should not be empty"
echo $name
fi

if  [[ $name =~ ^[A-Za-z\ ]+$ ]] && (( age>0 && age<100  )); then
echo "Valid name"
else
echo "Not a valid name"
fi
