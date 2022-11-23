from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import datetime as dt
default_args = {
  'owner': 'airflow',
  'start_date': dt.datetime(2020, 4, 1, 1, 00, 00),
  'retries': 1
}
dag = DAG('covid', 
  default_args=default_args,
  schedule_interval='0 1 * * *',
  catchup=False
  )
command_t1='python /home/sergeeva/airflow/dags/covid_func.py '
t1 = BashOperator(
  task_id= 'covidPlots',
  bash_command = command_t1,
  dag = dag
)
from git import Repo
import os
os.chdir('/home/sergeeva/Mytest/Mytest')
PATH_OF_GIT_REPO = r'/home/sergeeva/Mytest/Mytest/.git'
COMMIT_MESSAGE = 'daily update'

def git_push():
  repo = Repo(PATH_OF_GIT_REPO)
  repo.git.add('--all')
  repo.index.commit(COMMIT_MESSAGE)
  origin = repo.remote(name='origin')
  origin.push()
git_push()

command_t2='python /home/sergeeva/airflow/dags/covid_func.py '
t2 = BashOperator(
  task_id= 'gitPush',
  bash_command = command_t2,
  dag = dag
)

command_t3='python /home/sergeeva/airflow/dags/covid_func.py '
t3 = BashOperator(
  task_id= 'gitPush_repit',
  bash_command = command_t3,
  dag = dag
)

t1 >> t2 >> t3



