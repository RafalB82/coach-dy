.PHONY: validate install about about-dry

validate:
	python3 scripts/validate.py

install:
	mkdir -p $(HOME)/.config/opencode/skills/coach-dy/references
	mkdir -p $(HOME)/.config/opencode/skills/coach-dy/agents
	cp SKILL.md README.md README.pl.md LICENSE NOTICE.md $(HOME)/.config/opencode/skills/coach-dy/
	cp references/*.md references/*.json $(HOME)/.config/opencode/skills/coach-dy/references/
	cp agents/*.yaml $(HOME)/.config/opencode/skills/coach-dy/agents/
	@echo "Installed to $(HOME)/.config/opencode/skills/coach-dy"

about:
	python3 scripts/set_repo_about.py

about-dry:
	python3 scripts/set_repo_about.py --dry-run
