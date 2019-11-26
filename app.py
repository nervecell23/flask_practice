from flask import Flask, make_response
from flask_restful import Api, Resource
from lib.create_pdf import create_pdf
from lib.create_xml import create_xml
from lib.reports import Reports

app = Flask(__name__)
api = Api(app)

class ReportExportingPDF(Resource):
    def get(self, report_id):
        report = Reports.find(report_id)
        response = make_response(create_pdf(report))
        response.headers['content-type'] = 'application/pdf'
        return response

class ReportExportingXML(Resource):
    def get(self, report_id):
        report = Reports.find(report_id)
        response = make_response(create_xml(report))
        response.headers['content-type'] = 'application/xml'
        return response

api.add_resource(ReportExportingPDF, '/<report_id>/pdf')
api.add_resource(ReportExportingXML, '/<report_id>/xml')

if __name__ == '__main__':
    app.run(debug=True)
