import os
import json
from sqlalchemy import create_engine
from datetime import datetime as dt

class Reports:

    def __init__(self, report_id, content, created_at):
        self.id = report_id
        self.content = content
        self.created_at = dt.strptime(created_at, "%Y-%m-%d")

    @classmethod
    def find(cls, report_id):
        if os.getenv('ENVIRONMENT') == 'test':
            engine = create_engine('postgresql://localhost/reports_test')
        else:
            engine = create_engine('postgresql://localhost/reports')

        connection = engine.connect()
        sql = "SELECT * FROM abstract WHERE id={};".format(report_id)
        query = connection.execute(sql)
        id, result = query.fetchone()
        result = json.loads(result)

        return Reports(id, 
                        result['content'],
                        result['created_at']
        )
