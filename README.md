# Digital-Hunter
The system build up from 3 consumers:
1. Intel consumer:
    He response to get signals intellegent(sigint,humint,visint)
    he updated locations and priority in the bank 

2. Attack consumer:
    get reports from the air force 
    check if the target exist and write that

3. Damage consumer:
    get the damage values updated the attack result

and he recive the data and keep it in sql

to get started:
run in the cmd:
create a virtual invairmentby :
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

docker-compose up-d

and run the main file:
python .\recive_data_info.main.py