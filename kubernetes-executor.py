def use_airflow_binary():
    rc = os.system("airflow -h")
    assert rc == 0


# You don't have to use any special KubernetesExecutor configuration if you don't want to
start_task = PythonOperator(
    task_id="start_task", python_callable=print_stuff, dag=dag
)

# But you can if you want to
one_task = PythonOperator(
    task_id="one_task", python_callable=print_stuff, dag=dag,
    executor_config={"KubernetesExecutor": {"image": "airflow:latest"}}
)

# Use the airflow -h binary
two_task = PythonOperator(
    task_id="two_task", python_callable=use_airflow_binary, dag=dag,
    executor_config={"KubernetesExecutor": {"image": "airflow:latest"}}
)
