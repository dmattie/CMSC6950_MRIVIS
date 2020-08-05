#!/bin/bash
echo "Checking environment..."

errcnt=0

while read l; do
  package=$(echo $l |cut -d '=' -f 1)
  pkgtest=$(pip list |grep $package|wc -l)
  if [ $pkgtest -eq "0" ]
  then
    echo "xxxxxx FAIL xxxxxx $package not found"
    let "errcnt+=1"
  fi
done <requirements.txt

yellow=$(tput setaf 3)
green=$(tput setaf 2)
normal=$(tput sgr0)
if [ $errcnt -eq "0" ]
then
   echo "Everything looks hunky-dory.  You can run $green make $normal to get going."
else
   echo "Looks like you are missing some packages.  Try:$yellow pip install -r requirements.txt $normal"
fi
