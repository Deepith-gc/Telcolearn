echo "Monitoring top 3 processes every 5 seconds for 120 seconds"
echo "----------------------------------------------------------"
 
END_TIME=$((SECONDS + 120))
 
while [ $SECONDS -lt $END_TIME ]
do
    echo ""
    echo "Top 3 processes at: $(date +"%H:%M:%S")"
    ps -eo pid,comm,%cpu --sort=-%cpu | head -n 4   # header + top 3 rows
 
    sleep 5
done
 
echo ""
echo "Done! Monitoring completed."
