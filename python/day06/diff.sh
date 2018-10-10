#/bin/sh
cat $1 |sort|uniq -c |awk '{print $2}' >/tmp/s1.txt
cat $2 |sort|uniq -c |awk '{print $2}' >/tmp/s2.txt

for i in `cat /tmp/s2.txt`
do
    grep "$i" /tmp/s1.txt || echo $i >/tmp/s3.txt
done

