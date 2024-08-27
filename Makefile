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

playground:
    export PYTHONPATH=src && streamlit run src/semple/playground.py

quiz:
    export PYTHONPATH=src && streamlit run src/quiz/quizz.py

login:
    export PYTHONPATH=src && streamlit run src/login/login.py
