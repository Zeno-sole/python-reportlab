#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.shapes import _DrawingEditorMixin, Drawing, Group, String
from reportlab.lib.colors import Color, CMYKColor, PCMYKColor

class ExplodedDrawing_Drawing(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		Drawing.__init__(self,width,height,*args,**kw)
		self.transform = (1,0,0,1,0,0)
		self.add(String(34,34,'Hello World',textAnchor='start',fontName='DarkGardenMK',fontSize=12,fillColor=Color(0,0,0,1)))
		self.add(String(42,42,'Hello World',textAnchor='start',fontName='DarkGardenMK',fontSize=16,fillColor=Color(0,0,0,1)))
		self.add(String(50,50,'Hello World',textAnchor='start',fontName='DarkGardenMK',fontSize=20,fillColor=Color(0,0,0,1)))
		self.add(String(58,58,'Hello World',textAnchor='start',fontName='DarkGardenMK',fontSize=24,fillColor=Color(0,0,0,1)))
		self.add(String(66,66,'Hello World',textAnchor='start',fontName='DarkGardenMK',fontSize=28,fillColor=Color(0,0,0,1)))
		self.add(String(74,74,'Hello World',textAnchor='start',fontName='DarkGardenMK',fontSize=32,fillColor=Color(0,0,0,1)))


if __name__=="__main__": #NORUNTESTS
	ExplodedDrawing_Drawing().save(formats=['pdf'],outDir='.',fnRoot=None)