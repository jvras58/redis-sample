SHELL := /bin/zsh
.PHONY: venv

venv:
    @poetry run poetry install

commit:
    @echo "Revisar mudanças para este commit: "
    @echo "-------------------------------------"
    @git status -s 
    @echo "-------------------------------------"
    @read -p "Commit msg: " menssagem ; \
    git add . ;\
    git commit -m "$$menssagem" ;\

update:
    @git fetch origin
    @git pull
    @$(MAKE) venv

run:
    export PYTHONPATH=src && poetry run python src/semple/redis_raw.py