from django.http import HttpResponse

def test(request, *args, **kwargs):
	return HttpResponse(status = 200)
