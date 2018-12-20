for x in {1..50}
do 
 if (($x % 5 == 0 && $x % 7 == 0));
 then 
  echo "sivakrishna"
 elif (($x % 5 == 0))
 then 
  echo "krishna"
 elif (($x % 5 == 0 ));
 then
  echo "siva"
 else
  echo "$((x))"
 fi
done
