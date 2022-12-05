#!/bin/bash
YEAR=$1
DAY=$2

mkdir -p $YEAR'/inputs'

URL='https://adventofcode.com/'$YEAR'/day/'$DAY
INPUT_FILE=$YEAR/inputs/day$DAY.in
SOLUTION_FILE=$YEAR/day$DAY.py

max_fails=10
cur_fails=0
until $(curl $URL'/input' --config aoc_session --output $INPUT_FILE --silent --fail --retry 10 --retry-delay 5)
do
    ((cur_fails++))
    echo $cur_fails': Not quite yet...'
    if [ $cur_fails -ge $max_fails ]
    then
       echo 'Puzzle not yet released, please be patient.'
       exit 1
    fi
    sleep 5
done

echo "It's ready, start solving!"
cp -i day0.py $SOLUTION_FILE
# Updates the day in the template
sed -i -E "s/day0/day$DAY/" $SOLUTION_FILE
cmd.exe /C start $URL
# code -r $INPUT_FILE $SOLUTION_FILE
code -r $SOLUTION_FILE
cd $YEAR
python day$DAY.py
