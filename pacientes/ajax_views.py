from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from pacientes.models import EstudioSubcategoria


def EstudioSubcategorias(request):
    if request.POST.has_key('categoria') and request.is_ajax():
        caterogia = request.POST['categoria']
        y = EstudioSubcategoria.objects.filter(id_estudios=categoria)
        print y
        formulario = serializers.serialize('json', y)
        return HttpResponse(formulario, content_type='application/json')
    else:
        return render_to_response(
            'registro_pacientes.html',
            context_instance=RequestContext(request))
