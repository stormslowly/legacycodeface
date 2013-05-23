#!/bin/sh




> .blames.log

for f in `svn ls $0`
do

	svn blame $f -v >> .blames.log
done




cat .blames.log |  awk '{print $1, $2}'  | sort  -n | uniq -c
