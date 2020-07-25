from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_id='',
                 sql='',
                 table_name='',
                 *args, **kwargs):
        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_id=redshift_id
        self.sql=sql
        self.table_name=table_name
        
    def execute(self, context):
        self.log.info("Setting.")
        redshift=PostgresHook(postgres_conn_id=self.redshift_id)
        self.log.info('Deleting existed data.')
        redshift.run("DELETE FROM {tablename}".format(tablename=self.table_name))
        self.log.info('Importing data.')
        insert_sql="INSERT INTO {tablename} ".format(tablename=self.table_name) + self.sql
        redshift.run(insert_sql)
            
