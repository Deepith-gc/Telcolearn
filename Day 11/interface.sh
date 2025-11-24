for i in {1..10}; do
{
echo "Run #$1"
printf "%-15s %-15s\n" "Interface" "IPV4 Address"
ip -4 -o  addr show | awk '{split($4,a,"/"); printf "%-15s %-15s\n", $2, a[1]}'
echo "--------------------------------------"
echo
}>>iface.log
sleep 5
done
