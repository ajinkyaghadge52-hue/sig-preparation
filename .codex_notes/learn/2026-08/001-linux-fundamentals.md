# Linux Fundamentals - 101

## Completed navigation commands

| Task | Linux command | Meaning |
|---|---|---|
| Show location | `pwd` | Print the current working directory |
| List items | `ls` | List files and directories |
| Detailed hidden list | `ls -la` | Long listing including hidden items |
| Enter directory | `cd directory` | Change into a named directory |
| Move to parent | `cd ..` | Move up one directory level |
| Move home | `cd ~` | Move to the user home directory |

## Completed file commands - Short

| Task | Linux command | Meaning |
|---|---|---|
| Create directory | `mkdir logs` | Make a directory |
| Create empty file | `touch app.log` | Create a file if it does not exist |
| Copy | `cp source destination` | Copy a file to another path |
| Move or rename | `mv source destination` | Move a file or change its name |
| Delete file | `rm file.txt` | Remove the exact file specified |
| Find CSV files | `find . -name "*.csv"` | Search recursively from the current directory |

## Reading a complete small file with `cat`

### Purpose

`cat` prints the complete contents of a text file directly in the terminal. It is useful for quickly inspecting a small text or log file. For large files, use tools such as `less`, `head`, or `tail` instead of printing everything at once.

### Syntax

```bash
cat filename
```

### Practised example

```bash
cat practice/logs/application.log
```

The practice file contained six log entries. The fourth entry had the `ERROR` level. The number `4` describes the line's position; `ERROR` describes its log level.

### Interview answer

> I use `cat` to print the complete contents of a small text file for quick inspection. For a large log, I would use `less` or `tail` instead.

## Navigating a file with `less`

### Purpose

`less` opens a text file in an interactive viewer. It is suitable for large logs because it supports navigation and searching without printing the entire file onto the terminal.

### Syntax

```bash
less filename
```

### Essential controls

| Key | Action |
|---|---|
| Arrow keys or `Enter` | Move one line |
| `Space` | Move forward one screen |
| `b` | Move backward one screen |
| `g` | Go to the beginning |
| `G` | Go to the end |
| `/ERROR` then Enter | Search forward for `ERROR` |
| `n` / `N` | Next / previous match |
| `q` | Quit |

`less` was practised in WSL because it is a Linux utility and may not be installed in PowerShell.

### Interview answer

> I use `less` to inspect a large log interactively because I can navigate and search it without flooding the terminal with the entire file.

## Reading the beginning with `head`

### Purpose

`head` displays the beginning of a file. By default it displays the first 10 lines; `-n` selects a specific number of lines. It is useful for checking a file's format, headers, or earliest log entries.

### Syntax and example

```bash
head filename
head -n 3 practice/logs/application.log
```

The practised command displayed three lines, and the third line had the `WARN` log level.

### Interview answer

> I use `head` to quickly inspect the beginning of a file. The `-n` option controls how many lines are displayed.

## Reading recent entries with `tail`

### Purpose

`tail` displays the end of a file, which usually contains the most recent log entries. It displays 10 lines by default, while `-n` selects a specific number.

### Syntax and examples

```bash
tail filename
tail -n 2 practice/logs/application.log
tail -f practice/logs/application.log
```

`tail -f` keeps watching an open file for appended lines. `tail -F` is more robust when a log may be rotated or replaced because it follows the filename and reopens it. Stop either command with `Ctrl+C`.

### Interview answer

> I use `tail` to inspect the latest log entries and `tail -f` to monitor new entries in real time. For a rotated or replaced log, I can use `tail -F`.

## Searching text with `grep`

### Purpose

`grep` prints lines that match a word or pattern. It is commonly used to find warnings, errors, identifiers, or timestamps in logs.

### Syntax and useful options

```bash
grep "ERROR" filename       # matching lines
grep -n "ERROR" filename    # include line numbers
grep -i "error" filename    # ignore letter case
grep -c "ERROR" filename    # count matching lines
```

Options can be combined, such as `grep -in "error" filename`.

### Interview answer

> I use `grep` to find lines matching a word or pattern. I can use `-i` for case-insensitive matching, `-n` for line numbers, and `-c` for a match count.

## Counting content with `wc`

### Purpose

`wc` counts content in a file. With no option, its output order is lines, words, bytes, and filename.

### Useful options

```bash
wc -l filename  # lines
wc -w filename  # words
wc -c filename  # bytes
wc -m filename  # characters
wc -L filename  # longest line length
```

The practice log contained 8 lines, 40 words, and 314 bytes at the time of the exercise.

### Path reminder

A relative path starts from the current directory. When already inside `practice/logs`, use `application.log`. From the project root, use `practice/logs/application.log`. An absolute WSL path such as `/mnt/d/Projects/sig-preparation/practice/logs/application.log` works regardless of the current directory.

### Interview answer

> I use `wc` to count lines, words, bytes, or characters. I commonly use `wc -l` to count records in a text file or output received through a pipe.

## Combining commands with a pipe

The pipe operator `|` sends the standard output of the command on its left to the standard input of the command on its right.

```bash
grep "ERROR" application.log | wc -l
```

Here, `grep` produces the matching error lines and `wc -l` counts those lines. Each command performs one small task, making the pipeline easy to explain and extend.

### Interview answer

> A pipe passes one command's output into another command. For example, I can use `grep` to find error lines and pipe them to `wc -l` to count the errors.

### Multiple-pattern incident triage

```bash
grep -nE "WARN|ERROR" application.log
grep -E "WARN|ERROR" application.log | wc -l
```

`-E` enables an extended pattern, where `WARN|ERROR` means `WARN` or `ERROR`. `-n` adds matching line numbers. The practice log contained two matching problem entries: one `WARN` and one `ERROR`.

## Inspecting processes with `ps`

`ps` means process status. Basic `ps` shows processes associated with the current terminal. `ps aux` gives a detailed system-wide snapshot.

```bash
ps
ps aux
```

Important columns include `USER` for the owner, `PID` for the unique process identifier, `%CPU`, `%MEM`, and `COMMAND`.

### Interview answer

> I use `ps` to take a snapshot of running processes. `ps aux` shows system-wide details including each process's PID, owner, CPU, memory, and command.

## Live process monitoring with `top`

`top` continuously updates CPU, memory, load, and process information. `P` sorts processes by CPU, `M` sorts by memory, and `q` quits.

```bash
top
```

### Interview answer

> I use `top` for live monitoring of CPU, memory, system load, and processes. I use `ps` when I need a one-time process snapshot.

## Checking memory with `free`

`free` reports system memory and swap usage. `-h` displays human-readable units such as MiB and GiB.

```bash
free -h
```

Important columns are `total`, `used`, `free`, `buff/cache`, and `available`. Focus on `available` when judging whether programs have enough memory because Linux can reclaim cached memory.

### Interview answer

> I use `free -h` to inspect memory and swap in readable units. I focus on available memory because cached memory can be reclaimed.

## Checking filesystem capacity with `df`

`df` means disk free. It reports total, used, and available space for mounted filesystems. `-h` uses readable size units.

```bash
df -h
df -h /mnt/d/Projects/sig-preparation
```

Important columns include `Size`, `Used`, `Avail`, `Use%`, and `Mounted on`. Supplying a path reports the filesystem containing that path.

### Interview answer

> I use `df -h` to check filesystem capacity and available disk space. I focus on the utilization percentage and mount point.

## Measuring file and directory usage with `du`

`du` means disk usage. It measures the space consumed by a particular file or directory. `-s` gives one summary total and `-h` uses readable units.

```bash
du -sh /mnt/d/Projects/sig-preparation
du -h --max-depth=1 directory
```

### `free` versus `df` versus `du`

| Command | Simple question | Resource |
|---|---|---|
| `free -h` | How much working memory is available? | RAM |
| `df -h` | How full is the whole filesystem? | Disk/filesystem capacity |
| `du -sh folder` | How much space does this folder consume? | Specific file or directory |

Memory aid: `free` = memory, `df` = filesystem, `du` = directory usage.

### Interview answer

> `free` reports RAM usage, `df` reports capacity and available space for entire filesystems, and `du` reports disk space consumed by a particular file or directory.

## Finding and stopping processes

Every process has a unique process identifier (`PID`). A harmless practice process can be started in the background with:

```bash
sleep 300 &
```

`sleep 300` waits for 300 seconds, while `&` runs it in the background. `jobs -l` lists jobs belonging to the current shell and includes their PIDs.

```bash
jobs -l
pgrep -a sleep
ps -p PID -f
kill PID
```

`pgrep -a name` finds processes by name and displays their full commands. Verify the PID before stopping a process. Plain `kill PID` sends `SIGTERM` for a graceful shutdown. `kill -9 PID` sends `SIGKILL` and should be a last resort because the process cannot clean up.

### Interview answer

> I identify and verify the correct PID, then send the default SIGTERM for a graceful shutdown. I use SIGKILL only if the process does not respond.

## Reading Linux permissions

`ls -l` displays the file type and permissions in its first ten characters.

```bash
ls -l application.log
```

Example:

```text
-rw-r--r--
```

The first character is the type: `-` is a regular file, `d` is a directory, and `l` is a symbolic link. The remaining characters form three groups:

```text
rw-  r--  r--
user group others
```

The access letters are `r` for read, `w` for write, `x` for execute, and `-` when access is not granted.

### Important access rules

For a regular file:

- `r` allows reading its contents.
- `w` allows modifying its contents.
- `x` allows running it as a program or script.

For a directory:

- `r` allows listing its names.
- `w` allows creating, deleting, or renaming entries inside it.
- `x` allows entering or traversing it and accessing known entries.

Directory permissions depend on one another. For example, listing names requires `r`, while accessing an item inside generally requires `x`. Deleting a file is primarily controlled by the parent directory's permissions, not the file's own write bit.

### Interview scenario

For `-rw-r----- application.log`, the owner can read and modify the file, the group can only read it, and others have no access. A read-only file may still be deletable when the user has write and execute permissions on its parent directory: file `w` controls changing contents, while parent-directory `w` controls creating, deleting, and renaming entries.

A readable Python script without `x` can still be passed to an interpreter with `python3 script.py`, but it cannot normally be launched directly as `./script.py` until execute permission is added.

### Interview answer

> Linux permissions are defined separately for the owner, group, and others. Each can receive read, write, and execute access, and those permissions have different effects on files and directories.

## Changing permissions with `chmod` — important interview topic

`chmod` means change mode. Symbolic mode describes the change directly: `u` is owner, `g` is group, `o` is others, and `a` is all. `+`, `-`, and `=` add, remove, or set permissions.

```bash
chmod u+x deploy.sh     # let the owner execute the script
chmod g-w report.csv    # prevent the group from modifying the report
chmod o-r secrets.txt   # prevent others from reading secrets
chmod u=rw notes.txt    # give the owner exactly read and write
```

### Numeric permissions

The numeric values are `r = 4`, `w = 2`, and `x = 1`. Add them for each of owner, group, and others:

| Number | Permissions | Calculation |
|---:|---|---|
| `7` | `rwx` | 4 + 2 + 1 |
| `6` | `rw-` | 4 + 2 |
| `5` | `r-x` | 4 + 1 |
| `4` | `r--` | 4 |
| `0` | `---` | 0 |

### Real operational scenarios

```bash
chmod 600 private-key.pem
```

Only the owner can read and write a private key. Group and others have no access. SSH commonly rejects private keys that are accessible too broadly.

```bash
chmod 644 application.conf
```

The owner can read and modify a configuration file; everyone else can only read it.

```bash
chmod 755 deploy.sh
```

The owner can read, modify, and execute the script; group and others can read and execute it but cannot modify it.

```bash
chmod 640 application.log
```

The owner can read and modify the log, the operational group can read it, and others have no access.

Avoid solving permission problems with `chmod 777`: it grants everyone read, write, and execute access and usually violates least privilege. Determine which identity needs which specific access instead.

On a Windows drive mounted under WSL, such as `/mnt/d`, Windows permission mapping may make `chmod` results differ from a native Linux filesystem. Adding a permission that is already present also causes no visible change.

### Strong interview answer

> I use `chmod` to apply least-privilege access. For example, `600` protects a private key, `644` suits a readable configuration file, `755` makes a script executable without letting other users modify it, and `640` lets an operations group read a log. I avoid `777` because it grants unnecessary access.

## File ownership with `chown` and `chgrp`

Every file has one owner user and one associated group. Think of the owner as the responsible person and the group as the associated team.

```bash
sudo chown bob report.csv              # change the owner person
sudo chgrp operations report.csv       # change the associated team
sudo chown bob:operations report.csv   # change both together
```

`chown` changes who owns the file, `chgrp` changes its group, and `chmod` changes what the owner, group, and others are allowed to do. Ownership changes often require elevated privileges. `-R` applies a change recursively and must be used cautiously.

### Memory aid

```text
chown = change the person
chgrp = change the team
chmod = change what they may do
```

### Interview answer

> If a log should belong to a service account but remain readable by operations, I set the service account as owner, operations as the group, and use permissions such as `640` to define their access.

## User, executable, and command history

```bash
whoami
which python3
history
history | grep "chmod"
```

`whoami` identifies the current user, which helps explain the permissions that apply. `which` shows the executable selected from the directories in `PATH`; use it to diagnose multiple installations or unexpected versions. `history` displays recent shell commands and can be piped to `grep` to find a previous command.

```bash
echo $PATH
type -a python3
```

`PATH` is the ordered list of directories searched for commands. `type -a` can show all matching command definitions, including aliases, functions, and executable locations.

### Interview answer

> `whoami` identifies my current user, `which` shows the executable selected from my PATH, and `history` shows previously executed shell commands.

## Redirecting command output

Linux separates normal results (`stdout`, stream 1) from errors (`stderr`, stream 2).

```bash
command > output.log             # overwrite with normal output
command >> output.log            # append normal output
command 2> error.log             # overwrite with errors
command > combined.log 2>&1      # send errors to the same destination as output
```

Use `>` carefully because it replaces existing file contents. `>>` preserves the existing contents and appends new output.

### Interview answer

> `>` redirects normal output and overwrites the target, while `>>` appends. `2>` redirects errors. I use `2>&1` when normal output and errors should be written to the same log.

## Next lesson

Linux conversational drill completed. Retest numeric permissions (`640`) and graceful process termination (`SIGTERM`) during the final mock interview.

## Conversational drill results

Strengths: selected appropriate commands for log filtering, pipelines, system resources, and permission roles; clearly distinguished `chmod`, `chown`, and `chgrp`.

Retest points:

- Use `tail`, not `head`, for the latest log entries.
- `rw-r-----` is `640`; group `5` would incorrectly add execute permission.
- Locate processes broadly with `pgrep -a name` or `ps aux`; inspect a PID before acting.
- Send default `SIGTERM` with `kill PID` first. Use `kill -9 PID` only as a last resort.
