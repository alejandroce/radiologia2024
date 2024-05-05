import smtplib
from email.mime.multipart import MIMEMultipart
import datetime
import pdfkit
from django.core.files.base import File
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from django.db import transaction

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.views.generic import FormView, ListView, UpdateView, DetailView

from pacientes.forms import RegistroPacientesForm, FiltrosForm,\
    EstudiosInterpretacionesForm, CrearInterpretacionForm, QueryInterpretaciones
from pacientes.models import Paciente, Estudios, Interpretaciones, Medico, ArchivosInterpretacion, \
    ArchivoPDFInterpretacion
from django.http import HttpResponseRedirect, request
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from braces.views import PermissionRequiredMixin
from wkhtmltopdf.views import PDFTemplateView
from settings.base import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


@login_required(login_url='/ingresar')
def index(request):
    success_url = reverse('pacientesregistrados')
    return HttpResponseRedirect(success_url)


def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/')
                else:
                    return render(
                        request,
                        'noexisteusuario.html',
                        {}
                    )
            else:
                messages.success(
                    request,'USUARIO Y CONTRASENA NO EXISTEN,\
                    INTENTE DE NUEVO.')
                return render(
                    request,
                    'login.html',
                    {}
                )
    else:
        formulario = AuthenticationForm()
    return render(
        request,
        'login.html',
        {'formulario': formulario},
    )


class RegistroPacientesView(FormView):
    form_class = RegistroPacientesForm
    template_name = 'registro_pacientes.html'
    success_url = '/pacientes-registrados'

    def get_context_data(self, **kwargs):
        context = super(RegistroPacientesView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print ('#' * 10, 'invalido')
        print (form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class PacientesRegistrados(ListView):
    template_name = 'pacientes_lista.html'
    paginate_by = 15

    def dispatch(self, *args, **kwargs):
        return super(
            PacientesRegistrados, self).dispatch(*args, **kwargs)

    def get_nombre(self):
        try:
            return self.request.GET['nombre']
        except:
            return ''

    def get_hospital(self):
        try:
            return self.request.GET['hospital']
        except:
            return ''

    def get_adicional(self):
        try:
            return self.request.GET['adicional']
        except:
            return ''

    def get_queryset(self):
        nombre = self.get_nombre()
        hospital = self.get_hospital()
        adicional = self.get_adicional()

        user = self.request.user
        if user.username == 'alex':
            queryset = Paciente.objects.all().order_by('-pk')
        elif user.has_perm('pacientes.change_paciente'):
             queryset = Paciente.objects.filter(hospital="CENTRO").order_by('-pk')
        elif user.has_perm('pacientes.change_interpretaciones'):
            queryset = Paciente.objects.filter(hospital="GUADALAJARA").order_by('-pk')
        elif user.has_perm('pacientes.delete_interpretaciones'):
            queryset = Paciente.objects.filter(hospital="PRADO").order_by('-pk')
        elif user.has_perm('pacientes.add_paciente'):
            queryset = Paciente.objects.filter(hospital="CRUZ ROJA").order_by('-pk')
        else:
            queryset = Paciente.objects.all()

        if nombre:
            queryset = queryset.filter(
                Q(nombre__icontains=nombre) |
                Q(apellido_paterno__icontains=nombre) |
                Q(apellido_materno__icontains=nombre)).order_by('-pk')

        if hospital:
            queryset = queryset.filter(
                hospital=hospital).order_by('-pk')
        if adicional:
            queryset = queryset.filter(estudio_adicional='True')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(
            PacientesRegistrados, self).get_context_data(**kwargs)
        context['form'] = FiltrosForm(self.request.GET or None)
        context['nombre'] = self.get_nombre()
        context['hospital'] = self.get_hospital()
        context['adicional'] = self.get_adicional()
        return context


class EstudiosInterpretacion(PermissionRequiredMixin, FormView):
    permission_required = 'pacientes.add_interpretaciones'
    form_class = EstudiosInterpretacionesForm
    template_name = 'intepretacion_default.html'
    success_url = '/estudios-default'

    def get_context_data(self, **kwargs):
        context = super(EstudiosInterpretacion, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print '#' * 10, 'invalido'
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))


class EstudiosRegistrados(PermissionRequiredMixin, ListView):
    permission_required = 'pacientes.add_interpretaciones'
    template_name = 'estudios_registrados.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(
            EstudiosRegistrados, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = Estudios.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(
            EstudiosRegistrados, self).get_context_data(**kwargs)
        return context


class PerfilPaciente(ListView):
    template_name = 'perfil.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(
            PerfilPaciente, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        pk = self.kwargs.get('id')
        queryset = Paciente.objects.filter(pk=pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(
            PerfilPaciente, self).get_context_data(**kwargs)
        pk = self.kwargs.get('id')
        context['paciente_interpretaciones'] = Interpretaciones.objects.filter(id_paciente=pk)
        return context


class CrearInterpretacion(PermissionRequiredMixin, FormView):
    permission_required = 'pacientes.add_interpretaciones'
    form_class = CrearInterpretacionForm
    template_name = 'registro_pacientes.html'
    success_url = '/registro'

    def get_context_data(self, **kwargs):
        context = super(CrearInterpretacion, self).get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super(CrearInterpretacion, self).get_form_kwargs()
        paciente = Paciente.objects.get(pk=self.kwargs.get('id'))
        estudio = Estudios.objects.get(pk=self.kwargs.get('est'))
        kwargs.update({
                      'paciente': paciente}),
        kwargs.update({
                      'estudio': estudio}),
        return kwargs

    def form_valid(self, form, **kwargs):
        self.object = form.save()
        archivos_interpretacion = self.request.FILES.getlist('archivos_interpretacion')
        imagenes = []
        today_date = datetime.date.today()
        nombre_archivo = self.object.id_paciente.apellido_paterno + '-' + self.object.id_paciente.apellido_materno +\
            '-' + self.object.nombre_estudio + '-' + str(today_date)
        for archivo_inter in archivos_interpretacion:
            imagenes.append(archivo_inter)
            with transaction.atomic():
                archivo_many = ArchivosInterpretacion.objects.create(
                    archivo=archivo_inter
                )
            self.object.archivos.add(archivo_many)
        context = super(CrearInterpretacion, self).get_context_data(**kwargs)
        user = self.request.user
        context['img'] = imagenes
        context['interpretacion'] = self.object
        context['medico'] = Medico.objects.get(usuario=user)
        config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
        # config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
        contract_page = render_to_string('text_interpretacion.html', context)
        css = ['static/pdf/css/psg_portada.css', 'static/pdf/css/psg_segunda.css', 'static/pdf/css/psg_tercera.css', 'static/pdf/css/psg_cuarta.css']
        File(pdfkit.from_string(contract_page, 'media/interpretaciones/%s.pdf' %nombre_archivo, configuration=config))
        nombre_archivo_pdf = str(nombre_archivo)+'.pdf'
        ArchivoPDFInterpretacion.objects.create(
            nombre_archivo=nombre_archivo_pdf,
            interpretacion=self.object
        )
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print '#' * 10, 'invalido'
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse(
            "perfilpaciente",
            args=([self.object.id_paciente.pk])
        )


class Detalle(PermissionRequiredMixin, ListView):
    permission_required = 'pacientes.add_interpretaciones'
    template_name = 'detalle.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(
            Detalle, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        pk = self.kwargs.get('id')
        queryset = Interpretaciones.objects.filter(pk=pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(
            Detalle, self).get_context_data(**kwargs)
        return context


class EditarPaciente(PermissionRequiredMixin, UpdateView):
    permission_required = 'pacientes.add_interpretaciones'
    form_class = RegistroPacientesForm
    template_name = 'registro_pacientes.html'
    success_url = '/pacientes-registrados'

    def get_object(self, queryset=None):
        obj = Paciente.objects.get(pk=self.kwargs.get('id'))
        return obj


class EditarInterpretacion(PermissionRequiredMixin, UpdateView):
    permission_required = 'pacientes.add_interpretaciones'
    form_class = CrearInterpretacionForm
    template_name = 'registro_pacientes.html'

    def get_object(self, queryset=None):
        obj = Interpretaciones.objects.get(pk=self.kwargs.get('id'))
        return obj

    def get_form_kwargs(self):
        kwargs = super(EditarInterpretacion, self).get_form_kwargs()
        paciente = self.get_object().id_paciente
        # estudio = Estudios.objects.get(pk=self.kwargs.get('est'))
        kwargs.update({'paciente': paciente}),
        kwargs.update({'estudio': None}),
        return kwargs

    def get_success_url(self):
        return reverse(
            "perfilpaciente",
            args=([self.object.id_paciente.pk])
        )


class EditarInterpretacionDefault(PermissionRequiredMixin, UpdateView):
    permission_required = 'pacientes.add_interpretaciones'
    form_class = EstudiosInterpretacionesForm
    template_name = 'registro_pacientes.html'
    success_url = '/estudios-default'

    def get_object(self, queryset=None):
        obj = Estudios.objects.get(pk=self.kwargs.get('id'))
        return obj


class ImprimirExcel(PermissionRequiredMixin, ListView):
    permission_required = 'pacientes.add_interpretaciones'
    template_name = 'print.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(
            ImprimirExcel, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        id = self.kwargs.get('id')
        queryset = Interpretaciones.objects.filter(pk=id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(
            ImprimirExcel, self).get_context_data(**kwargs)
        return context


class Imprimir(PermissionRequiredMixin, PDFTemplateView):
    permission_required = 'pacientes.add_interpretaciones'
    template_name = 'imprimir_estudio.html'
    cmd_options = {
        'margin-top': "1cm",
        'margin-right': "1cm",
        'margin-bottom': "0.9cm",
        'margin-left': "1cm",
        'page-size': 'Letter',
        'footer-right': '[page] / [topage]',
        'encoding': 'utf-8',
        'disable-smart-shrinking': True,
        # 'zoom': 1.3
    }
    show_content_in_browser = True

    def get_queryset(self):
        id = self.kwargs.get('id')
        queryset = Interpretaciones.objects.filter(pk=id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Imprimir, self).get_context_data(**kwargs)
        user = self.request.user
        context['medico'] = Medico.objects.get(usuario=user)
        context['object_list'] = self.get_queryset()
        return context


class EstudiosDefaultList(PermissionRequiredMixin, ListView):
    permission_required = 'pacientes.add_interpretaciones'
    template_name = 'list_interpretaciones_default.html'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(
            EstudiosDefaultList, self).dispatch(*args, **kwargs)

    def get_nombre(self):
        try:
            return self.request.GET['nombre']
        except:
            return ''

    def get_hospital(self):
        try:
            return self.request.GET['hospital']
        except:
            return ''

    def get_adicional(self):
        try:
            return self.request.GET['adicional']
        except:
            return ''

    def get_queryset(self):
        nombre = self.get_nombre()
        queryset = Estudios.objects.all().order_by('-pk')

        if nombre:
            queryset = queryset.filter(
                Q(nombre_estudio__icontains=nombre) |
                Q(categoria__icontains=nombre)).order_by('-pk')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(
            EstudiosDefaultList, self).get_context_data(**kwargs)
        context['form'] = QueryInterpretaciones(self.request.GET or None)
        context['nombre'] = self.get_nombre()
        return context


@permission_required('pacientes.add_interpretaciones')
def EliminarPaciente(request, id):
    """ Eliminar Otros """
    compania = Paciente.objects.get(pk=id)
    compania.delete()
    form = FiltrosForm
    return HttpResponseRedirect('/pacientes-registrados')


@permission_required('pacientes.add_interpretaciones')
def EliminarInterpretacion(request, id):
    interpretacion = Interpretaciones.objects.get(pk=id)
    paciente = interpretacion.id_paciente
    id = paciente.pk
    interpretacion.delete()
    return HttpResponseRedirect('/perfil/%i' % id)


@permission_required('pacientes.add_interpretaciones')
def EliminarMachotes(request, id):
    """ Eliminar Otros """
    machote = Estudios.objects.get(pk=id)
    machote.delete()
    return HttpResponseRedirect('/estudios-default')


def sendinterpretation(request, id):
    if request.method == 'POST':
        interpretacion = Interpretaciones.objects.get(pk=id)
        send_to = interpretacion.id_paciente.email
        nombre_archivo_pdf = ArchivoPDFInterpretacion.objects.get(interpretacion=interpretacion)
        nombre_archivo = nombre_archivo_pdf.nombre_archivo
        new_message = render_to_string('mail_content.html')
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        msg = EmailMessage("Resultados Estudios Radiologicos", new_message, 'Radiologia Aguilar <davidaguilar33@gmail.com>', [send_to, 'mcalejandrocontreras@gmail.com'])
        msg.content_subtype = "html"
        # We assume that the image file is in the same directory that you run your Python script from
        fp = open('/var/www/project/radiologia2020/static/img/logo_dr.png', 'rb')
        image = MIMEImage(fp.read())
        fp.close()
        msg.attach_file('media/interpretaciones/%s' % nombre_archivo)
        image.add_header('Content-ID', '<Mailtrapimage>')
        msg.attach(image)
        msg.send()
        return HttpResponseRedirect('/')


def sendinterpretationall(request, patient_id):
    if request.method == 'POST':
        paciente = Paciente.objects.get(pk=patient_id)
        print paciente
        interpretacion = Interpretaciones.objects.filter(id_paciente=paciente.pk)
        send_to = paciente.email
        new_message = render_to_string('mail_content.html')
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        msg = EmailMessage("Resultados Estudios Radiologicos", new_message, 'Radiologia Aguilar <davidaguilar33@gmail.com>', [send_to, 'mcalejandrocontreras@gmail.com'])
        msg.content_subtype = "html"
        # We assume that the image file is in the same directory that you run your Python script from
        fp = open('/var/www/project/radiologia2020/static/img/logo_dr.png', 'rb')
        image = MIMEImage(fp.read())
        fp.close()
        for inter in interpretacion:
            for ar in inter.archivopdfinterpretacion_set.all():
                 msg.attach_file('media/interpretaciones/%s' % ar.nombre_archivo)
                 # Specify the  ID according to the img src in the HTML part
        image.add_header('Content-ID', '<Mailtrapimage>')
        msg.attach(image)
        msg.send()
        return HttpResponseRedirect('/')