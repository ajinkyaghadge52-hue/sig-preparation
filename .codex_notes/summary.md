# SIG Interview Preparation Summary

This repository supports step-by-step preparation for Linux, foundational Python, pandas, and a final SIG interview simulation.

Current position: the initial live-coding interview was completed successfully. Linux questions were answered and the coding solution was completed and explained; notes were used only for occasional syntax checks. All original Linux, Python, and pandas teaching is complete.

New direction: use this repository as the foundation for a deeper Python phase aimed at a possible in-person coding round. Progress from core collection patterns into nested-data aggregation, sorting, parsing, file processing, generators, standard-library tools, testing, debugging, and complexity analysis. Require independent attempts before solutions and continue recording mistakes and concise revision notes.

Phase 2 status: Problem 1, net positions by symbol, is complete and documented. Problem 2 is paused at `python/phase2/02_rank_positions.py`. Dictionary traversal with `.items()` has been introduced. Resume by printing each `(symbol, position)` tuple and its `(-abs(position), symbol)` sort key before calling `sorted(..., key=get_sort_key)`. Do not jump directly to a lambda; use a named helper function and intermediate values first.

Learning references:

- `.codex_notes/learn/2026-08/001-linux-fundamentals.md`
- `.codex_notes/learn/2026-08/002-python-foundations.md`
- `.codex_notes/learn/2026-08/003-pandas-foundations.md`

Canonical status is stored in `PROGRESS.md`. The ordered plan is stored under `.codex_notes/plan/` and learning material under `.codex_notes/learn/`.
