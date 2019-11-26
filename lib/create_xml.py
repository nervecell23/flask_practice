import dicttoxml

def create_xml(report):
    dict = {'content': report.content,
            'created_at': report.created_at
    }
    return dicttoxml.dicttoxml(dict)
