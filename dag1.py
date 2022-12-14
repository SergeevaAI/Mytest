from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from hello_operator import HelloOperator
with DAG(
  dag_id="consume_new_data_from_pos",
  start_date = datetime(2020, 12, 1),
  schedule_interval=None
  ) as dag:
  hello = HelloOperator(task_id="hello")
  get_new_data = DummyOperator(task_id="get_new_data")
  parse_file = DummyOperator(task_id="parse_file")
  check_is_it_ne_customer = DummyOperator(task_id="check_is_it_ne_customer")
  create_new_customer = DummyOperator(task_id="create_new_customer")
  update_existed_customer = DummyOperator(task_id="update_existed_customer")
hello >> get_new_data >> parse_file >> check_is_it_ne_customer >> [create_new_customer, update_existed_customer]

