# SIG Interview Preparation Summary

This repository supports step-by-step preparation for Linux, foundational Python, pandas, and a final SIG interview simulation.

Current position: the initial live-coding interview was completed successfully. Linux questions were answered and the coding solution was completed and explained; notes were used only for occasional syntax checks. All original Linux, Python, and pandas teaching is complete.

New direction: use this repository as the foundation for a deeper Python phase aimed at a possible in-person coding round. Progress from core collection patterns into nested-data aggregation, sorting, parsing, file processing, generators, standard-library tools, testing, debugging, and complexity analysis. Require independent attempts before solutions and continue recording mistakes and concise revision notes.

Canonical roadmap: `.codex_notes/plan/2026-08/002-python-data-analysis-engineering-mastery-plan.md`. The roadmap covers Python from first principles through data analysis, pandas/NumPy, data-engineering pipelines, testing, maintainability, and advanced topics. Every concept uses an explain-trace-attempt-debug-test-document sequence and a mastery gate before combination.

Personalized continuation: preserve credit for demonstrated basic functions, loops, collections, exceptions, debugging, and pandas. Use a ten-step bridge to repair container/item distinctions, variable dictionary keys, tuples, function calls, and simple sorting. Begin with `python/foundations/01_container_map.py`; return to the paused custom-sort problem only after the bridge passes.

Latest checkpoint: Bridges 1–4 are complete: container distinctions, whole container versus loop item, literal versus variable dictionary keys, and tuple creation/indexing/unpacking with dictionary `.items()`. `python/foundations/05_function_calls.py` exists but has not been attempted. Resume with Step 1 only: run the file without calling `describe_job`, observe that it prints nothing, and explain that `def` stores the function body while a call executes it. The custom-sorting problem remains paused.

Phase 2 status: Problem 1, net positions by symbol, is complete and documented. Problem 2 at `python/phase2/02_rank_positions.py` is deliberately paused because the combined custom-sort exercise introduced too many concepts at once. Before returning, separately teach and practise tuples, tuple unpacking, function parameters and return values, plain `sorted()`, and one simple key function. Do not use lambdas or multi-key sorting until each prerequisite is independently clear.

Learning references:

- `.codex_notes/learn/2026-08/001-linux-fundamentals.md`
- `.codex_notes/learn/2026-08/002-python-foundations.md`
- `.codex_notes/learn/2026-08/003-pandas-foundations.md`

Canonical status is stored in `PROGRESS.md`. The ordered plan is stored under `.codex_notes/plan/` and learning material under `.codex_notes/learn/`.
