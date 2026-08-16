# SIG Interview Preparation Progress

## Dashboard

- [x] Linux fundamentals completed
- [ ] Linux conversational drill completed
- [ ] Python foundation drills completed without copying
- [ ] Python timed exercise completed
- [ ] Pandas exploration workflow completed
- [ ] Pandas analysis drill completed
- [ ] Full 60-minute mock completed
- [ ] Final open-book cheat sheet prepared

## Completed work

### Linux navigation

- [x] `pwd`
- [x] `ls` and Linux `ls -la`
- [x] `cd directory`
- [x] `cd ..`
- [x] `cd ~`

### Linux file operations

- [x] `mkdir`
- [x] `touch` and PowerShell `New-Item`
- [x] `cp`
- [x] `mv` for moving and renaming
- [x] `rm` for a specific temporary file
- [x] Recursive CSV search using Linux `find` and PowerShell `Get-ChildItem`

### Linux logs and search

- [x] Read a complete small log file using `cat`
- [x] Navigate and search a log file using `less` in WSL
- [x] Read the beginning of a log file using `head`
- [x] Read recent entries using `tail` and follow updates using `tail -f` / `tail -F`
- [x] Search log contents and show matching line numbers using `grep -n`
- [x] Count file lines, words, and bytes using `wc`
- [x] Combine commands with a pipe to count matching log entries
- [x] Find and count multiple log levels using `grep -E` and a pipe

### Linux processes and resources

- [x] Inspect running processes using `ps aux`
- [x] Monitor live CPU, memory, and processes using `top`
- [x] Check available memory and swap using `free -h`
- [x] Check filesystem capacity and utilization using `df -h`
- [x] Measure a directory's disk usage using `du -sh`
- [x] Explain the difference between `free`, `df`, and `du`
- [x] Start, find, inspect, and gracefully stop a temporary process

### Linux permissions

- [x] Read file type and owner/group/others permissions using `ls -l`
- [x] Explain `r`, `w`, and `x` access rules
- [x] Explain symbolic and numeric `chmod` using real operational scenarios
- [x] Explain ownership using `chown` and `chgrp`

### Linux shell essentials

- [x] Redirect standard output and errors using `>`, `>>`, `2>`, and `2>&1`
- [x] Identify the current user with `whoami`
- [x] Locate the selected executable with `which`
- [x] Review previous shell commands with `history`

## Mistake bank

| Area | Mistake | Correct rule | Retested? |
|---|---|---|---|
| Linux | Expected `ls -la` to work in PowerShell | Confirm the shell; PowerShell uses `ls -Force` | No |
| Linux | Moved up one directory too far | Run `pwd` after changing location | Yes |
| Linux | Tried searching before creating a matching test file | Create known input so the result can be verified | Yes |
| Linux | Answered with the line number when asked for the failure log level | Distinguish a line's position from its level, such as `ERROR` | No |
| Linux | Used `practice/logs/application.log` while already inside `Practice/logs` | Relative paths start from the current directory; use `application.log` there, or use the absolute path | Yes |
| Python | Placed `return` inside a processing loop | Return after processing all required items | No |

## Confidence

| Skill | Current | Target |
|---|---:|---:|
| Linux navigation and files | 3 | 4 |
| Linux logs and search | 3 | 4 |
| Processes and permissions | 3 | 4 |
| Short Python function | 2 | 4 |
| Python debugging | 2 | 4 |
| Pandas loading and inspection | 1 | 4 |
| Pandas filtering and grouping | 1 | 4 |
| Reasoning aloud | 2 | 4 |

## Next action

Complete the timed Linux conversational drill and retest weak points.
