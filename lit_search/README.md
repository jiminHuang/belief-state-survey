# Reproducible literature search for the belief-state survey

1. Edit `config.json` (queries per survey section, date window, screening rules). Do not edit scripts for a rerun.
2. `python3 search.py` — queries OpenAlex, snapshots `runs/<ts>/raw.json`, `config_snapshot.json`, `counts_search.json`.
3. `python3 screen.py <ts>` — applies inclusion/exclusion rules, writes `screened.csv`, `shortlist_recent.csv`, `counts_screen.json`.
4. Manual full-text screening of `shortlist_recent.csv` is recorded in `runs/<ts>/manual_screen.csv` (decision + taxonomy cell).

All numbers for the survey's "Methodology / paper collection" paragraph come from `counts_search.json` and `counts_screen.json`.
