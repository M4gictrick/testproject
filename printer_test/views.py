from django.shortcuts import render
from printer_test.models import Printer

# Create your views here.

def printer_index(request):
	printer_test = Printer.objects.all()
	context = {
		'printer_test' : printer_test
	}
	return render(request, 'printer_index.html', context)

def printer_detail(request, pk):
	printer = Printer.objects.get(pk=pk)
	context = {
		'printer' : printer
	}
	return render(request, 'printer_detail.html', context)