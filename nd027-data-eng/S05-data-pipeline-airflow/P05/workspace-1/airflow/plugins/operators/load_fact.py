from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 select_query="",
                 truncate="",
                 *args, **kwargs):
        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.select_query = select_query
        self.truncate = truncate

    def execute(self, context):
        """
        transform staging tables into dimension table
        @args
            redshift_conn_id: redshift cluster connection
            table: dimension table name
            truncate: clean table before loading
            select_query: select query from SqlQueries
        """
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.truncate:
            redshift.run(f"TRUNCATE TABLE {self.table}")
        self.log.info(f'load {self.table}')
        load_sql = f"""
            INSERT INTO {self.table}
            {self.select_query}
        """
        redshift.run(load_sql)