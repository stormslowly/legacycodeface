cat blame.txt |  awk '{print $1, $2}'  | sort  -n | uniq -c
