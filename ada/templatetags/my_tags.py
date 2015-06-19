from django import template
import os
register = template.Library()
Base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def contador(request):
	if request.session.get('contador', False):
		contador = GetContador()
		return str(contador)
	request.session['contador'] = True
	contador = GetContador()
	contador = contador + 1
	SetContador(str(contador))
	return str(contador)
	
def GetContador():
	f_contador = open(Base + '/templatetags/contador', 'r')
	contador = f_contador.read()
	return int(contador)

def SetContador(contador):

	f_contador = open(Base + '/templatetags/contador', 'w')
	f_contador.write(contador)
	f_contador.close()

register.simple_tag(contador)