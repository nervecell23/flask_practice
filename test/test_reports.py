import pytest
import json
from ..lib.reports import Reports
from sqlalchemy import create_engine

def test_constructor():
    subject = Reports(1, 'test_content', '2001-02-12')

    assert subject.id == 1
    assert subject.content = 'test_content'
    assert subject.created_at = '2001-02-12'
    
def test_find(monkeypatch):
    monkeypatch.setenv('ENVIRONMENT', 'test')
    engine = create_engine('postgresql://localhost/reports_test')
    connection = engine.connect()
    connection.execute('DROP TABLE IF EXISTS abstract')
    connection.execute('CREATE TABLE abstract(id SERIAL PRIMARY KEY, content VARCHAR)')
    content = {'content': 'test_content', 'created_at': '2011-01-11'}
    content = json.dumps(content)
    connection.execute("INSERT INTO abstract(content) VALUES('{}');".format(content))

    query = Reports.find(1)

    assert query.id == 1
    assert query.content == 'test_content'
    assert query.created_at = dt(2011,1,11).date()
