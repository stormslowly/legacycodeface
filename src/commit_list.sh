#!/bin/sh

> .blames.log

echo $1

for f in `svn ls $1 -R`
do
	echo 'blaming '$f
	svn blame $1'/'$f -v | awk '{print substr($3,0,4)}' >> .blames.log
done

cat .blames.log | sort -n | uniq -c > pie.txt

python draw_pie.py