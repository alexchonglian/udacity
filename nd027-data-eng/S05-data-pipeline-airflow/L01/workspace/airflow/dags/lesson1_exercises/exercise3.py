import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def hello_world():
    logging.info("Hello World")


def addition():
    logging.info(f"2 + 2 = {2+2}")


def subtraction():
    logging.info(f"6 -2 = {6-2}")


def division():
    logging.info(f"10 / 2 = {int(10/2)}")


dag = DAG(
    "lesson1.exercise3",
    schedule_interval='@hourly',
    start_date=datetime.datetime.now() - datetime.timedelta(days=1))

def PyOp(func):
    return PythonOperator(
        task_id=func.__name__,
        python_callable=func,
        dag=dag
    )

# TODO: Define an hello world task that calls the `hello_world` function above
# TODO: Define an addition task that calls the `addition` function above
# TODO: Define a subtraction task that calls the `subtraction` function above
# TODO: Define a division task that calls the `division` function above

hello_world_task = PyOp(hello_world)
addition_task    = PyOp(addition)
subtraction_task = PyOp(subtraction)
division_task    = PyOp(division)

"""
hello_world_task = PythonOperator(task_id="hello_world",   python_callable=hello_world,dag=dag)
addition_task    = PythonOperator(task_id="addition",      python_callable=addition,   dag=dag)
subtraction_task = PythonOperator(task_id="subtraction",   python_callable=subtraction,dag=dag)
division_task    = PythonOperator(task_id="division",      python_callable=division,   dag=dag)
"""

# TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_task
#                   /                 \
#   hello_world_task                   -> division_task
#                   \                 /
#                    ->subtraction_task

hello_world_task >> addition_task
hello_world_task >> subtraction_task

addition_task    >> division_task
subtraction_task >> division_task