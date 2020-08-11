mkdir ~/venvs
cd ~/venvs
python3 -m venv searing-frost
cd searing-frost
ls

source ./bin/activate

deactivate

pip install numpy
pip show numpy
pip list

pip freeze
pip freeze > ~/searing-frost-project/requirements.txt
cat ~/searing-frost-project/requirements.txt