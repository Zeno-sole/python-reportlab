#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, Polygon, PolyLine, Line, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=400,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(Polygon(points=[108.3032,252.9412,200,288.2353,291.6968,252.9412,306.9796,138.2353,200,58.82353,93.02039,138.2353,108.3032,252.9412],fillColor=Color(1,.972549,.862745,1),fillOpacity=None,strokeColor=None,strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Polygon(points=[85.37899,266.1765,200,252.9412,261.1312,235.2941,276.414,155.8824,200,94.11765,131.2274,160.2941,85.37899,266.1765],fillColor=Color(0,1,1,1),fillOpacity=None,strokeColor=None,strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Polygon(points=[138.8688,235.2941,200,261.7647,261.1312,235.2941,329.9038,125,200,164.7059,108.3032,147.0588,138.8688,235.2941],fillColor=Color(.596078,.984314,.596078,1),fillOpacity=None,strokeColor=None,strokeWidth=0,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(PolyLine(points=[108.3032,252.9412,200,288.2353,291.6968,252.9412,306.9796,138.2353,200,58.82353,93.02039,138.2353,108.3032,252.9412],strokeColor=Color(1,.972549,.862745,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(PolyLine(points=[85.37899,266.1765,200,252.9412,261.1312,235.2941,276.414,155.8824,200,94.11765,131.2274,160.2941,85.37899,266.1765],strokeColor=Color(0,1,1,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(PolyLine(points=[138.8688,235.2941,200,261.7647,261.1312,235.2941,329.9038,125,200,164.7059,108.3032,147.0588,138.8688,235.2941],strokeColor=Color(.596078,.984314,.596078,1),strokeWidth=1,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=None,strokeOpacity=None))
		self.add(Line(200,200,200,350,strokeColor=Color(0,0,0,1),strokeWidth=.5,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=(2,2),strokeOpacity=None))
		self.add(Line(200,200,329.9038,275,strokeColor=Color(0,0,0,1),strokeWidth=.5,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=(2,2),strokeOpacity=None))
		self.add(Line(200,200,329.9038,125,strokeColor=Color(0,0,0,1),strokeWidth=.5,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=(2,2),strokeOpacity=None))
		self.add(Line(200,200,200,50,strokeColor=Color(0,0,0,1),strokeWidth=.5,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=(2,2),strokeOpacity=None))
		self.add(Line(200,200,70.09619,125,strokeColor=Color(0,0,0,1),strokeWidth=.5,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=(2,2),strokeOpacity=None))
		self.add(Line(200,200,70.09619,275,strokeColor=Color(0,0,0,1),strokeWidth=.5,strokeLineCap=0,strokeLineJoin=0,strokeMiterLimit=0,strokeDashArray=(2,2),strokeOpacity=None))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,200,357.5)
		v0.add(String(-2.22,-4,'a',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,336.399,278.75)
		v0.add(String(-2.5,-4,'b',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,336.399,121.25)
		v0.add(String(-2.22,-4,'c',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,200,42.5)
		v0.add(String(-2.5,-4,'d',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,63.601,121.25)
		v0.add(String(-2.22,-4,'e',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))
		v0=self._nn(Group())
		v0.transform = (1,0,0,1,63.601,278.75)
		v0.add(String(-1.665,-4,'f',textAnchor='start',fontName='Times-Roman',fontSize=10,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)