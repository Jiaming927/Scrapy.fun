#! /bin/bash

clear

echo '## TEXTBOOK DATA HUNTER ##'

echo 'Please wait for around 1 minute'
python courseAndSLNSoup.py

python refineCourseAndSLN.py
echo 'Done'

echo 'Now Step two:'

echo 'This is going to take a long long time...'

echo 'Be patient'
python textbookSoup.py

python refineTextBook.py

echo 'Done :)'


