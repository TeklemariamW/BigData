#! /bin/bash
echo “Welcome to the Linux family.”

#Check if a file exist
if [ -f file.ttxt ]; then
  echo "File exists."
else
  echo "File does not exists."
fi

#Count the number of lines in the file
wc -l < file.txt

#Add a new line at the end of the file
echo "Adding a new line at the end of the file" >> file.txt

#remove a specific line from the file (last line in this case '$')
sed -i '$d' file.txt

#Find a specific keyword in the file: -n:line n.,-w:match Word,-i:ignore case
grep --color -n -w -i "big data" file.txt

#Replace a keyword with a new value
sed -i 's/file/big-data file./g' file.txt

#Display the modified file
find . -type f -mmin -15
