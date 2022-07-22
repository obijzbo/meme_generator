sudo apt install python3-virtualenv
sudo virtualenv venv
source venv/bin/activate
pip3 install spacy==3.2.0
python3 -m spacy download en_core_web_sm
pip3 install -r requirements.txt