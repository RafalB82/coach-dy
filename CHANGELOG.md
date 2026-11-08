# Changelog

All notable changes to this repository.

## [Unreleased]

### Added

- `repo-about.json` — versioned GitHub About metadata (description, homepage,
  topics).
- `scripts/set_repo_about.py` — validates and applies the About metadata with
  `gh api`; supports `--dry-run`.
- `make about` / `make about-dry` shortcuts.
- Repository About section filled with a description and 12 topics.

## [0.1.0] - 2026-11-08

### Added

- `SKILL.md` — coaching skill grounded in Dorian Yates' high-intensity,
  low-volume philosophy, with evidence-aware framing and contextual
  optimization.
- `references/knowledge_base_dy.md` — thematic digest of the Huberman Lab
  podcast with Dorian Yates, with timestamps.
- `references/knowledge_base_dy.json` — structured version: 20 principles,
  12 numbers, evidence map, context, boundaries.
- `references/evidence_base.md` — evidence map with 13 key studies and
  verdicts (supported / partial / not supported), plus the n=1 caveat.
- `README.md`, `README.pl.md` — English and Polish documentation.
- `LICENSE` (MIT), `NOTICE.md` — licensing and third-party notices.
- `scripts/validate.py` — repository validation.
- `Makefile` — `make validate` and `make install` shortcuts.
- `.github/workflows/validate.yml` — CI validation.

### Fixed (relative to the first draft)

- `+0.5 kg` → `+0.5 lb` (~0.25 kg), matching the transcript.
- `+30 lbs in 6 weeks on deca` → `+20 lbs (210→230) in 6 weeks on 20 mg/day
  Dianabol`.
- Deload `1–2×/year` → about `2×/year` ("a couple of times a year").
- "Creator of Blood and Guts" → "associated with the method; the name was
  coined later".
- Timestamps for "don't copy champions", "adversity as fuel", "destined",
  TRT, and periodization.
- Attribution: 1×/week frequency (Huberman/Mentzer), MPS 48 h (Huberman),
  protein 1 g/lb (sponsor read).

### Notes

- No full transcript, audio, or video is included.
- This is not medical advice.
