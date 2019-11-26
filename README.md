# flask_practice

## Approach

The project is developed using Python 3.7.0.  
The core component of the solution is the __Reports__ class(implemented in reports.py).  
Inside, a class method will fetch an abstract report from database with respect to a report_id. Then the data entry fetched will be encapsulated and returned.  
The returned report object will be converted into pdf or xml object using two methods implemented in create_pdf.py and create_xml.py.  
A REST layer is implemented in app.py using Flask framework.

## Dependencies

1. __flask__, __flask_restful__ - web framework
2. __fpdf__ - pdf template and pdf object generation
3. __dicttoxml__ - xml object generation 
4. __pytest__ - unit test
5. __sqlalchemy__ - access to postgresql database

## Run unit test

Create a local postgresql test database using sql files located in <project directory>/db/migrations/

```
> cd <project directory>
> pytest test/
```

## Fire up local server

```
> python app.py
```

## Endpoints

Type in a browser:  
Generate pdf report
```
/<report_id>/pdf
```
Generate xml report
```
/<report_id>/xml
```
## Note

The project is development in a virtual environment using anaconda 2.
