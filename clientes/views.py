# -*- coding: utf-8 -*-
from io import BytesIO

from django.http import HttpResponse
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from .models import Clientes


class IndexView(ListView):
    template_name = "index.html"
    model = Clientes
    context_object_name = "c"


def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"
    # la linea 31 es por si deseas descargar el pdf
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    catalog = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Clientes", styles['Heading1'])
    catalog.append(header)
    headings = ('Nombre', 'Email', 'Edad', 'Dirección')
    allclientes = [(p.nombre, p.email, p.edad, p.direccion) for p in Clientes.objects.all()]
    print allclientes

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    catalog.append(t)
    doc.build(catalog)
    response.write(buff.getvalue())
    buff.close()
    return response

