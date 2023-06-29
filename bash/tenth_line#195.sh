# Read from the file file.txt and output the tenth line to stdout.
count=0
while read line;
do
    count=$(($count+1))
    if [ $count -eq 10 ];
        then
            break
    fi
done < file.txt
echo $line
