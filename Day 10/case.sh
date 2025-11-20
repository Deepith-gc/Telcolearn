read -p "Enter your choice:" choice
case $choice in
1)touch demo.txt;;
2)mkdir files;;
3)ls -lat;;
*)echo "Invalid";;
esac
