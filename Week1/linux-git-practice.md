# Linux and Git Practical Practice

This document records the Week 1 command-line topics practised and provides concise examples for revision.

## 1. Navigation and directories

```bash
pwd                 # show the current directory
ls                  # list visible entries
ls -lah              # detailed listing including hidden files
cd /tmp              # change directory
cd ..                # move to parent directory
cd ~                 # move to home directory
mkdir practice       # create a directory
mkdir -p project/logs/archive
```

## 2. File operations

```bash
touch notes.txt                 # create an empty file
cat notes.txt                   # display file contents
head -n 5 application.log       # display first five lines
tail -n 3 application.log       # display last three lines
cp notes.txt notes-copy.txt     # copy a file
mv notes-copy.txt backup.txt    # rename or move a file
find . -type f                  # list files below current directory
find . -name "*.log"            # find log files
```

`touch` creates an empty file if it does not exist; it does not write text into an existing file. `find` searches recursively from the path supplied.

## 3. Searching and analysing logs

```bash
grep "ERROR" application.log
grep -i "error" application.log
grep -n "ERROR" application.log
grep -v "INFO" application.log
grep -c "ERROR" application.log
grep -E 'INFO|WARN|ERROR' application.log
wc -l application.log
awk '{print $3}' application.log | sort -u
tail -3 application.log
```

- `grep` prints lines matching a pattern.
- `-i` ignores letter case, `-n` shows line numbers, `-v` inverts the match, and `-c` counts matching lines.
- `grep -E` supports extended patterns such as alternatives separated by `|`.
- `wc -l` counts lines.
- `awk '{print $3}'` prints the third whitespace-separated field; for the sample log, this is the log level.
- `sort -u` sorts values and removes duplicates.
- `head` and `tail` inspect the beginning and end of files.

## 4. Pipes and redirection

```bash
grep "ERROR" application.log | wc -l
grep "ERROR" application.log > errors.log
grep "ERROR" application.log >> errors.log
echo "APP_ENV=testing" > app.conf
```

- `|` sends one command's output to another command.
- `>` creates or overwrites the destination file.
- `>>` appends to the destination file.
- Re-running a command with `>>` may add duplicate lines; use `>` when regenerating a result from scratch.
- `>&2` sends a message to standard error.

## 5. Permissions and processes

```bash
ls -l
chmod u+x health-check.sh
chmod 600 private-file.txt
ps
ps aux
sleep 300 &
echo $!
```

`ls -l` displays permissions. `chmod u+x` adds execute permission for the owner; `chmod 600` restricts file access to the owner. `ps` inspects processes. `&` starts a command in the background and `$!` gives the most recent background process ID. Only manage processes you own or are authorised to manage.

## 6. Bash scripting and exit codes

```bash
if [[ -f "app.conf" ]]; then
    echo "Configuration file exists"
else
    echo "Configuration file is missing" >&2
    exit 1
fi

echo $?
```

- `[[ -f file ]]` checks whether a regular file exists.
- `>&2` sends diagnostics to standard error.
- `exit 0` conventionally indicates success; non-zero values indicate failure or another condition.
- `$?` contains the previous command's exit status, so inspect it immediately after the command.

A health-check script is included in `health-check.sh`. It checks for a configuration file and accepts `development`, `testing`, or `production` as `APP_ENV` values.

## 7. Git version control

```bash
git status
git diff
git log --oneline
git log --oneline --graph --all
git switch -c feature/logging
git switch main
git merge feature/logging
git add notes.txt
git commit -m "Add practice notes"
git restore notes.txt
git revert <COMMIT_ID>
```

- `git status` shows staged, unstaged, and untracked changes.
- `git diff` shows unstaged changes.
- `git log` inspects commit history.
- Branches isolate work; merging integrates a branch.
- A merge conflict requires editing the affected file, removing conflict markers, staging the resolution, and completing the merge.
- `git restore` can discard uncommitted file changes. Use it carefully.
- `git revert` creates a new commit that reverses an earlier commit. Replace `<COMMIT_ID>` with a real commit ID.

## 8. Practical log investigation results

For the included seven-line sample log:
- Total entries: **7**
- Entries containing `ERROR`: **3**
- Distinct log levels: **ERROR**, **INFO**, **WARN**

The commands and findings are described in `evidence/linux/incident-report.txt`.

## Lessons learned
1. Confirm the working directory before modifying files.
2. Use filters and pipelines to reduce large logs to relevant evidence.
3. Understand the difference between overwriting and appending output.
4. Use meaningful exit codes to make scripts easier to automate.
5. Check Git state before recovery commands and use a temporary repository for risky practice.
