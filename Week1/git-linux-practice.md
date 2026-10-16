# Linux and Git Practice

## 1. Objective

The objective of this task is to practise essential Linux commands and Git operations used in DevOps workflows.

## 2. Linux Command Practice

The following commands are used to navigate the filesystem, manage files, inspect processes, and work with permissions.

| Command | Purpose | Example |

grep -i	Search text without case sensitivity	grep -i "error" app.log
grep -n	Show matching lines with line numbers	grep -n "error" app.log
grep -r	Search recursively through files	grep -r "TODO" .
head	Display the first 10 lines by default	head app.log
head -n	Display a specified number of lines	head -n 5 app.log
tail	Display the last 10 lines by default	tail app.log
tail -n	Display a specified number of lines	tail -n 20 app.log
tail -f	Follow a log as new lines appear	tail -f app.log
history	Display commands from shell history	history
du -sh	Show the total size of a directory in readable units	du -sh ~/devops-practice
du -h	Show file and directory disk usage in readable units	du -h ~/devops-practice
df -h	Show filesystem space in readable units	df -h
wc -l	Count lines in a file	wc -l app.log
sort	Sort lines of text	sort names.txt
uniq	Remove adjacent duplicate lines	sort names.txt \| uniq
cut	Extract fields from text	cut -d: -f1 /etc/passwd
less	Read long files page by page	less app.log
tee	Display output and save it to a file	echo "Test" \| tee output.txt
tar -czf	Create a compressed archive	tar -czf backup.tar.gz devops-practice/
uname -a	Display kernel and system information	uname -a
free -h	Display memory usage	free -h
uptime	Show uptime and load averages	uptime
which	Locate a command executable	which git

## 3. Practical Linux Exercises

### Exercise 1: Directory Management

Create a practice directory and inspect its contents.

```bash
mkdir -p ~/devops-practice
cd ~/devops-practice
pwd
ls -la
```

### Exercise 2: File Operations

Create, copy, rename, and inspect a text file.

```bash
echo "DevOps practice" > notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt backup.txt
cat notes.txt
ls -la
```

### Exercise 3: File Permissions

Create a script and grant execute permission.

```bash
printf '#!/bin/bash\necho "Hello DevOps"\n' > hello.sh
chmod +x hello.sh
./hello.sh
```

Expected output:

```text
Hello DevOps
```

### Exercise 4: Search and Processes

Search a log file for an error and inspect running processes.

```bash
echo "ERROR: sample failure" > app.log
grep "ERROR" app.log
ps aux
```

## 4. Git Practice

Git tracks changes and helps maintain a history of project development.

### Exercise 1: Inspect the Repository

Run these commands from the internship repository.

```bash
git status
git log --oneline
git branch
```

### Exercise 2: Stage and Commit Changes

Create a small practice file, then stage and commit it.

```bash
echo "Git practice completed" > git-practice.txt
git add git-practice.txt
git commit -m "Add Git practice exercise"
```

### Exercise 3: Synchronize with GitHub

Push your committed changes to the remote repository.

```bash
git push
```

### Exercise 4: Inspect Changes

Modify a tracked file and inspect the difference.

```bash
git diff
git status
```

## 5. Results

Record the commands executed, their outputs, and any errors encountered during practice.

| Exercise | Status | Observations |
|---|---|---|
| Directory management | Pending | |
| File operations | Pending | |
| File permissions | Pending | |
| Search and processes | Pending | |
| Git operations | Pending | |
| GitHub push | Pending | |

## 6. Conclusion

These exercises provide practical experience with Linux filesystem operations, permissions, processes, text searching, and Git version control. These skills support the shell automation and containerization projects planned for the internship.