# SIG Interview Preparation Progress

## Dashboard

- [x] Linux fundamentals completed
- [x] Linux conversational drill completed
- [x] Python foundation drills completed without copying
- [ ] Python timed exercise completed
- [x] Pandas exploration workflow completed
- [x] Pandas analysis drill completed
- [ ] Full 60-minute mock completed
- [ ] Final open-book cheat sheet prepared

## Completed work

### Pandas exploration

- [x] Load a CSV using `pd.read_csv()`
- [x] Inspect sample rows, shape, columns, data types, and missing values
- [x] Filter rows using one and multiple boolean conditions
- [x] Select columns and create a derived column with a vectorized calculation
- [x] Sort rows using `sort_values()`
- [x] Handle missing values using `dropna()` and median `fillna()`
- [x] Group rows and aggregate with `groupby()`, `sum()`, `mean()`, and `count()`

### Python foundations

- [x] Write a function that counts matching list items using a loop and condition
- [x] Place `return` after the loop so all items are processed
- [x] Filter dictionaries into a new list using a threshold
- [x] Count values by category using a dictionary
- [x] Remove duplicates while preserving order using a set and list
- [x] Normalize strings using `strip()` and `upper()`
- [x] Handle expected missing dictionary keys using `.get()` with a default
- [x] Handle invalid numeric strings using `try` / `except ValueError`
- [x] Combine filtering, missing-key handling, and ordered output in one function (with hints)

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
| Linux | Used `head` when asked for the latest log entries | `head` shows the beginning; `tail` shows the end/latest entries | Yes |
| Linux | Read `rw-r-----` as `650` | Add `r=4`, `w=2`, `x=1`; `rw-r-----` is `640` | No |
| Linux | Did not initially identify the graceful process signal | Use default `kill PID` (`SIGTERM`) first; reserve `kill -9` for an unresponsive process | No |
| Python | Placed `return` inside a processing loop | Return after processing all required items | Yes |
| Python | Used one dictionary to collect multiple matching records | Use a list of dictionaries; repeated dictionary-key assignment overwrites earlier values | Yes |
| Python | Misspelled a loop variable and raised `NameError` | Use the same variable spelling where it is defined and referenced; read the final traceback line first | Yes |
| Python | Used required-key access for an optional key in a list of dictionaries | Each list item is one dictionary; use `job.get("status")` when the key may be missing | Yes |
| Pandas | Grouped the full DataFrame when the question asked about failed jobs only | Filter the relevant population first, then group and aggregate | Yes |

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

At the 9:00 AM restart, complete `python/python_retest.py` independently, run the compressed combined mock, generate the final cheat sheet, and revise weak points before the 3:00 PM interview.
