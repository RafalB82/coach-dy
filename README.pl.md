# Coach-DY

> Praktyczny skill trenerski do treningu siłowego, regeneracji, redukcji i mindsetu — oparty na filozofii Doriana Yatesa (high-intensity, low-volume „Blood and Guts”), z jawną bazą dowodową.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Po co ten skill

Większość porad treningowych jest pisana dla ludzi z nieograniczonym czasem i regeneracją. Ten skill jest dla drugiej strony: osób z pracą, dziećmi, domem, słabym snem, stresem lub wiekiem — czyli takich, u których wąskim gardłem jest regeneracja.

Zachowuje rdzeń metody Doriana:

- 2×/tydz. full body, ~45 min
- 8–10 ćwiczeń na całe ciało
- jedna ciężka seria do upadku po rozgrzewce (druga tylko, jeśli pierwsza nie „siadła”)
- 2–3 min przerwy między seriami
- progresywne przeciążenie, choćby o pół funta lub jedno powtórzenie
- 5–6 tygodni mocno, potem lżej

…i jasno mówi, co nauka potwierdza, a co nie.

6× Mr. Olympia i obecne zdrowie Doriana to **argument z przypadku n=1**, nie dowód uniwersalnej optymalności. Genetyka, sterydy w karierze, dekady treningu i survivorship bias są confounderami.

## Zawartość

| Plik | Rola |
|---|---|
| `SKILL.md` | Główne instrukcje: zasady, framing dowodowy, intake, pętla decyzyjna, format odpowiedzi, kluczowe zasady, granice |
| `references/knowledge_base_dy.md` | Synteza podcastu Huberman Lab z Dorianem Yatesem, z timestampami i korektami |
| `references/knowledge_base_dy.json` | Wersja strukturalna: 20 zasad, 12 liczb, mapa dowodów, kontekst, granice |
| `references/evidence_base.md` | Mapa dowodów: 13 badań, werdykty, optymalizacja kontekstowa, zastrzeżenie n=1 |
| `agents/openai.yaml` | Minimalne metadane agenta |
| `scripts/validate.py` | Walidacja repo: JSON, frontmatter, wymagane pliki, brak plików multimedialnych |
| `.github/workflows/validate.yml` | CI uruchamiające walidację przy push i PR |

## Status dowodów w skrócie

| Twierdzenie | Werdykt |
|---|---|
| Przerwy 2–3 min | **Potwierdzone** (Schoenfeld 2016) |
| 2×/tydz. wystarczy przeciętnej osobie | **Potwierdzone jako minimum** (Schoenfeld 2016/2019) |
| Trening blisko upadku | **Częściowo** — mała przewaga u zaawansowanych (Grgic 2021; Robinson 2024) |
| Jedna seria do upadku jest optymalna | **Niepotwierdzone** — więcej serii zwykle daje więcej hipertrofii (Krieger 2010; Schoenfeld 2017) |
| Niska objętość HIT wystarcza | **Częściowo** — skuteczne i czasowo wydajne, ale nie optymalne dla maksymalnej hipertrofii (Giessing 2016) |
| 6 min HIIT ≈ 45 min steady cardio | **Potwierdzone dla zdrowia metabolicznego** (Gillen 2016) |
| 1 g białka/lb jest konieczne | **Niepotwierdzone** — plateau ~1,6 g/kg (Morton 2018) |
| 5–6 tyg. mocno + 2 tyg. lżej | **Częściowo** — bezpieczne/sensowne, ale nie wyraźnie lepsze dla hipertrofii (Moesgaard 2022; Coleman 2024) |

Pełne cytowania: [`references/evidence_base.md`](references/evidence_base.md).

## Instalacja

### OpenCode

```bash
git clone https://github.com/RafalB82/coach-dy.git ~/.config/opencode/skills/coach-dy
```

Zrestartuj OpenCode lub przeładuj skille. Skill rejestruje się nazwą z frontmattera: `Coach-DY`.

### Ręcznie

Skopiuj folder do:

```text
~/.config/opencode/skills/coach-dy/
```

Albo, z lokalnego klona:

```bash
make install
```

Plik `SKILL.md` musi być w katalogu głównym tego folderu — względne linki do `references/` na tym polegają.

## Użycie

Przykładowe prompty:

- „Ułóż plan HIT 2×/tydz. na 6 tygodni; mam 45 min i słaby sen.”
- „Czy 2×/tydz. wystarczy przy moim wieku i pracy?”
- „Oceń mój dziennik treningowy i zaproponuj jedną zmianę.”
- „Co mówią badania o treningu do upadku?”

Format odpowiedzi:

```text
Obserwacja:
Interpretacja:
Rekomendacja:
Monitoruj:
Ponowna ocena:
Źródło:
```

## Zasady projektowe

- **Świadomość dowodów:** oddziela twierdzenia z podcastu od wyników badań i oznacza status dowodów.
- **Kontekst przed uniwersalizmem:** „optymalne” zależy od czasu, regeneracji, wieku i adherencji.
- **Konserwatyzm:** żadnego dopingu, leków, diagnozowania; sygnały alarmowe do specjalisty.
- **Atrybucja:** timestampy dla Doriana, cytowania dla badań.
- **Bez pełnej transkrypcji:** repo nie redystrybuuje transkrypcji ani audio podcastu.

## Źródła

- Podcast Huberman Lab z Dorianem Yatesem: <https://youtu.be/qzXU390N3vs>
- Transkrypcja: `~/transkrypcja/out/qzXU390N3vs.md` (poza repo)
- Cytowania badań: [`references/evidence_base.md`](references/evidence_base.md)

## Współpraca

PR-y mile widziane. Przed wysłaniem:

```bash
make validate
```

Zasady:

- Każde twierdzenie ma źródło (cytat lub timestamp).
- Nie dodawaj pełnych transkrypcji, audio ani materiałów objętych prawem autorskim.
- Zachowaj rozróżnienie „Dorian powiedział” vs „badania pokazują”.
- Ton praktyczny i konserwatywny.

## Metadane repozytorium

Opis i tematy w sekcji About są wersjonowane w [`repo-about.json`](repo-about.json) i aplikowane przez:

```bash
make about
```

Podgląd bez zastosowania:

```bash
make about-dry
```

## Licencja

MIT dla oryginalnej treści repo. Cytaty z podcastu i abstrakty badań pozostają własnością ich autorów i są używane w celach komentarza/edukacji. Szczegóły: [`NOTICE.md`](NOTICE.md).

## Zastrzeżenie

To nie jest porada medyczna. Skill nie diagnozuje, nie leczy i nie zastępuje specjalisty. Nie używaj go do usprawiedliwiania dopingu, skrajnego odwodnienia ani niebezpiecznie szybkiej utraty wagi. Przy bólu, urazie, chorobie lub objawach zaburzeń odżywiania skonsultuj się z kwalifikowanym specjalistą.
