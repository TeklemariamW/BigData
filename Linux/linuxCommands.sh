:wq #save file and quite editor in terminal
#colorize the output
ls --color=auto
#The alias command lets you define temporary aliases in your shell session
alias = NAME="VALUE"
alias ls="ls --color=auto"

alias #list all the aliases you have in your shell session
unalia #remove an alias from the already defined aliases
pwd #print working directory
cp file_to_copy.txt new_file.txt #copy files and folders
cp -r dir_to_copy/ new_copy_dir/  #copy entire directories by using the recursive flag
rm filename #removing a file
mv #move (or rename) files and directories through your file system.
mv source_file destination_folder/ #moving file
mv old_file.txt new_named_file.txt #rename a file
mkdir folderName #create a new folder
man #displays the manual page of any other command (as long as it has one)
ex. man mkdir

touch #allows you to update the access and modification times of the specified files
touch -m filename
touch new_file_name #create a new empty file

chmod #change the mode of a file (permissions) quickly
chmod +x script #make a file executable by the user
    #u: User, meaning the owner of the file.
    #g: Group, meaning members of the group the file belongs to.
    #o: Others, meaning people not governed by the u and g permissions.
    #a: All, meaning all of the above.

sudo #superuser do

#Debian-based (Ubuntu, Linux Mint)
sudo apt install gimp

#Red Hat-based (Fedora, CentOS)
sudo yum install gimp

#Arch-based (Manjaro, Arco Linux)
sudo pacman -S gimp

echo "Cool message" #displays defined text in the terminal
cat #short for “concatenate,” lets you create, view, and concatenate files directly from the terminal.
kill #sends a TERM or kill signal to a process that terminates it.
ping #networking terminal utility used to test network connectivity.


#Making passwordless connection b/n VMs and creating CLUSTER---wheel Group
#1. inside root@localhost or root@hostname
#. inside home directory
bigdata@hostname
su bigdata #home directory
cd ~
ssh-keygen # generating public/private rsa key pair
ssh-copy-id -i ~/.ssh/id_rsa.pub bigdata@<compute4.hadoop.local> #Then enter password for the hostname

chmod 0600 ~/.ssh/authorized_keys

#do copy for all VMs like for hostname compute1.hadoop.local
ssh-copy-id -i ~/.ssh/id_rsa.pub bigdata@<compute1.hadoop.local> #Then enter password for the hostname
#like this we copy to all VMs
#Now you can connect to the other vm with out password
ssh bigdata@compute1.hadoop.local