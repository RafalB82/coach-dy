# Coach-DY

> A practical coaching skill for resistance training, recovery, fat loss, and mindset — grounded in Dorian Yates' high-intensity, low-volume "Blood and Guts" philosophy, with an explicit evidence map.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Why this skill exists

Most training advice is written for people with unlimited time and recovery. This skill is built for the opposite: people with work, children, a home, poor sleep, stress, or older age — people for whom recovery is the bottleneck.

It keeps Dorian Yates' core principles:

- 2×/week full-body training, ~45 minutes
- 8–10 exercises covering the whole body
- one hard set to failure after warm-ups (second set only if the first didn't land)
- 2–3 minutes rest between sets
- progressive overload, even by half a pound or one rep
- 5–6 hard weeks, then a lighter period

…and it states clearly where research supports them and where it doesn't.

Dorian's 6× Mr. Olympia record and current health are treated as a **plausibility case (n=1)**, not proof of universal optimality. Genetics, anabolic steroids during his career, decades of training, and survivorship bias are confounders.

## What's inside

| File | Purpose |
|---|---|
| `SKILL.md` | Main skill instructions: operating rules, evidence-aware framing, intake, decision loop, response format, key principles, boundaries |
| `references/knowledge_base_dy.md` | Thematic digest of the Huberman Lab podcast with Dorian Yates, with timestamps and corrections |
| `references/knowledge_base_dy.json` | Structured version: 20 principles, 12 numbers, evidence map, context, boundaries |
| `references/evidence_base.md` | Evidence map: 13 key studies, verdicts (supported / partial / contradicted), contextual optimization, n=1 caveat |
| `agents/openai.yaml` | Minimal agent metadata |
| `scripts/validate.py` | Repository validation: JSON, frontmatter, required files, no media files |
| `.github/workflows/validate.yml` | CI that runs the validator on push and pull request |

## Evidence at a glance

| Claim | Verdict |
|---|---|
| 2–3 min rest between sets | **Supported** (Schoenfeld 2016) |
| 2×/week is enough for the average person | **Supported as a minimum** (Schoenfeld 2016/2019) |
| Training close to failure | **Partly supported** — small advantage for trained lifters (Grgic 2021; Robinson 2024) |
| One set to failure is optimal | **Not supported** — multiple sets generally produce more hypertrophy (Krieger 2010; Schoenfeld 2017) |
| Low-volume HIT is sufficient | **Partly supported** — effective and time-efficient, not optimal for maximal hypertrophy (Giessing 2016) |
| 6 min HIIT ≈ 45 min steady cardio | **Supported for cardiometabolic fitness** (Gillen 2016) |
| 1 g/lb protein is necessary | **Not supported** — plateau is ~1.6 g/kg (Morton 2018) |
| 5–6 weeks hard + 2 weeks light | **Partly supported** — safe/plausible, not clearly superior for hypertrophy (Moesgaard 2022; Coleman 2024) |

Full citations and caveats: [`references/evidence_base.md`](references/evidence_base.md).

## Install

### OpenCode

```bash
git clone https://github.com/RafalB82/coach-dy.git ~/.config/opencode/skills/coach-dy
```

Restart OpenCode or reload skills. The skill is registered by its frontmatter name: `Coach-DY`.

### Manual

Copy this folder to:

```text
~/.config/opencode/skills/coach-dy/
```

Or, from a local clone:

```bash
make install
```

The `SKILL.md` file must stay at the root of that folder; relative links to `references/` depend on it.

## Usage

Example prompts:

- "Ułóż plan HIT 2×/tydz. na 6 tygodni; mam 45 min i słaby sen."
- "Czy 2×/tydz. wystarczy przy moim wieku i pracy?"
- "Oceń mój dziennik treningowy i zaproponuj jedną zmianę."
- "Co mówią badania o treningu do upadku?"

The skill answers in this format:

```text
Obserwacja:
Interpretacja:
Rekomendacja:
Monitoruj:
Ponowna ocena:
Źródło:
```

## Design rules

- **Evidence-aware:** separates podcast claims from research findings and labels the evidence status.
- **Context-first:** "optimal" depends on time, recovery, age, and adherence — not on a universal rule.
- **Conservative:** no doping, no medication advice, no diagnosis; red flags go to a clinician.
- **Attribution:** timestamps for Dorian's claims; citations for research.
- **No full transcript:** the repository does not redistribute the podcast transcript or audio.

## Sources

- Huberman Lab podcast with Dorian Yates: <https://youtu.be/qzXU390N3vs>
- Transcript: `~/transkrypcja/out/qzXU390N3vs.md` (not included in this repository)
- Research citations: see [`references/evidence_base.md`](references/evidence_base.md)

## Contributing

Pull requests are welcome. Before submitting:

```bash
make validate
```

Guidelines:

- Keep claims sourced; add a citation or a timestamp.
- Do not add full transcripts, audio, or copyrighted material.
- Preserve the distinction between "Dorian said" and "research shows".
- Keep the tone practical and conservative.

## License

MIT for the original work in this repository. Quoted podcast excerpts and research abstracts remain the property of their respective owners and are used for commentary/education. See [`NOTICE.md`](NOTICE.md).

## Disclaimer

This is not medical advice. It does not diagnose, treat, or replace a clinician. Do not use it to justify doping, extreme dehydration, or unsafe rapid weight loss. If you have pain, an injury, a medical condition, or signs of an eating disorder, consult a qualified professional.
