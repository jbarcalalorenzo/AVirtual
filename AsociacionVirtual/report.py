from django.utils.translation import ugettext_lazy as _
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import SampleHorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table,\
    TableStyle,Image
from AsociacionVirtual import models


def get_percentage(values):
    total = sum(values)
    percentage = []
    for value in values:
        v = round(value*100.0/total, 2)
        percentage.append(str(v)+" %")
    return percentage

class PdfPrint:

    # initialize class
    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        # default format is A4
        if pageSize == 'A4':
            self.pageSize = A4
        elif pageSize == 'Letter':
            self.pageSize = letter
        self.width, self.height = self.pageSize

    def pageNumber(self, canvas, doc):
        number = canvas.getPageNumber()
        canvas.drawCentredString(100*mm, 15*mm, str(number))

    def title_draw(self, x, y, text):
        chart_title = Label()
        chart_title.x = x
        chart_title.y = y
        chart_title.fontName = 'FreeSansBold'
        chart_title.fontSize = 16
        chart_title.textAnchor = 'middle'
        chart_title.setText(text)
        return chart_title

    def line_chart_draw(self, values, days):
        nr_days = len(days)
        min_temp = min(min(values[0]), min(values[1]))
        d = Drawing(0, 170)
        # draw line chart
        chart = SampleHorizontalLineChart()
        # set width and height
        chart.width = 350
        chart.height = 135
        # set data values
        chart.data = values
        # use(True) or not(False) line between points
        chart.joinedLines = True
        # set font desired
        chart.lineLabels.fontName = 'FreeSans'
        # set color for the plot area border and interior area
        chart.strokeColor = colors.white
        chart.fillColor = colors.lightblue
        # set lines color and width
        chart.lines[0].strokeColor = colors.red
        chart.lines[0].strokeWidth = 2
        chart.lines[1].strokeColor = colors.blue
        chart.lines[1].strokeWidth = 2
        # set symbol for points
        chart.lines.symbol = makeMarker('Square')
        # set format for points from chart
        chart.lineLabelFormat = '%2.0f'
        # for negative axes intersect should be under zero
        chart.categoryAxis.joinAxisMode = 'bottom'
        # set font used for axes
        chart.categoryAxis.labels.fontName = 'FreeSans'
        if nr_days > 7:
            chart.categoryAxis.labels.angle = 45
            chart.categoryAxis.labels.boxAnchor = 'e'
        chart.categoryAxis.categoryNames = days
        # change y axe format
        chart.valueAxis.labelTextFormat = '%2.0f °C'
        chart.valueAxis.valueStep = 10
        if min_temp > 0:
            chart.valueAxis.valueMin = 0
        llabels = ['Max temp', 'Min temp']
        d.add(self.title_draw(250, 180, _('Temperatures statistics')))
        d.add(chart)
        return d

    def pie_chart_draw(self, values, llabels):
        d = Drawing(10, 150)
        # chart
        pc = Pie()
        pc.x = 0
        pc.y = 50
        # set data
        pc.data = values
        # set labels
        pc.labels = get_percentage(values)
        # set the link line between slice and it's label
        pc.sideLabels = 1
        # set width and color for slices
        pc.slices.strokeWidth = 0
        pc.slices.strokeColor = None
        d.add(self.title_draw(250, 180,
                              _('Precipitation probability statistics')))
        d.add(pc)
        d.add(self.legend_draw(llabels, pc, x=300, y=150, boxAnchor='ne',
                               columnMaximum=12, type='pie'))
        return d

    def vertical_bar_chart_draw(self, values, days, llabels):
        d = Drawing(0, 170)
        #  chart
        bc = VerticalBarChart()
        # set width and height
        bc.height = 125
        bc.width = 470
        # set data
        bc.data = values
        # set distance between bars elements
        bc.barSpacing = 0.5

        # set labels position under the x axe
        bc.categoryAxis.labels.dx = 8
        bc.categoryAxis.labels.dy = -2
        # set name displayed for x axe
        bc.categoryAxis.categoryNames = days

        # set label format for each bar
        bc.barLabelFormat = '%d'
        # set distance between top of bar and it's label
        bc.barLabels.nudge = 7

        # set some charactestics for the Y axe
        bc.valueAxis.labelTextFormat = '%d km/h'
        bc.valueAxis.valueMin = 0

        d.add(self.title_draw(250, 190, _('Wind speed statistics')))
        d.add(bc)
        d.add(self.legend_draw(llabels, bc, x=480, y=165, boxAnchor='ne',
                               columnMaximum=1, type='bar'))
        # d.add(bcl)
        return d

    def report(self,title,tipo=None,logopath=None):
        # set some characteristics for pdf document
        if tipo is not None:
            doc = SimpleDocTemplate(
                self.buffer,
                rightMargin=72,
                leftMargin=72,
                topMargin=30,
                bottomMargin=72,
                pagesize=self.pageSize)
            if logopath is not None:
                im = Image(logopath, 2 * inch, 2 * inch)
                doc.append(im)
            # a collection of styles offer by the library
            styles = getSampleStyleSheet()
            # add custom paragraph style
            styles.add(ParagraphStyle(
                name="TableHeader", fontSize=11, alignment=TA_CENTER))
            styles.add(ParagraphStyle(
                name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,))
            styles.add(ParagraphStyle(
                name="Justify", alignment=TA_JUSTIFY))
            #GET DATA
            if tipo == 'Socio':
                modelos = models.Socio.objects.all()
            if tipo == 'Evento':
                modelos = models.Evento.objects.all()
            if tipo == 'Alquiler':
                modelos = models.Alquila.objects.all()
            # list used for elements added into document
            data = []
            data.append(Paragraph(title, styles['Title']))
            # insert a blank space
            data.append(Spacer(1, 12))
            table_data = []
            # table header
            if tipo == "Socio":
                table_data.append([
                    Paragraph('Nombre', styles['TableHeader']),
                    Paragraph('Email', styles['TableHeader'])
                ])
            if tipo == "Evento":
                table_data.append([
                    Paragraph('Nombre', styles['TableHeader']),
                    Paragraph('Fecha Inicio', styles['TableHeader']),
                    Paragraph('Fecha Fin', styles['TableHeader']),
                    Paragraph('Coste', styles['TableHeader']),
                    Paragraph('Beneficio', styles['TableHeader'])
                ])
            if tipo == "Alquiler":
                table_data.append([
                    Paragraph('Nombre', styles['TableHeader']),
                    Paragraph('Fecha alquiler', styles['TableHeader']),
                    Paragraph('Fecha devolución', styles['TableHeader'])
                ])
            for i, modelo in enumerate(modelos):
                # Add a row to the table
                if tipo == "Socio":
                    table_data.append([modelo.nombre,modelo.mail])
                if tipo == "Evento":
                    table_data.append([modelo.nombre,modelo.fecha_alta,modelo.fecha_baja,modelo.coste,modelo.beneficio])
                if tipo == "Alquiler":
                    table_data.append([modelo.nombre,modelo.fecha_alquiler,modelo.fecha_devolucion])
            # create table
            wh_table = Table(table_data, colWidths=[doc.width/7.0]*7)
            wh_table.hAlign = 'LEFT'
            wh_table.setStyle(TableStyle(
                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                 ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
                 ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
                 ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
            data.append(wh_table)
            data.append(Spacer(1, 48))
            # create document
            doc.build(data, onFirstPage=self.pageNumber,
                      onLaterPages=self.pageNumber)
            pdf = self.buffer.getvalue()
            self.buffer.close()
            return pdf
        else:
            return None