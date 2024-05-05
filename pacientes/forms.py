# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, \
    ButtonHolder, Button, Div, Submit
from crispy_forms.bootstrap import FormActions
from pacientes.models import Paciente, Estudios, Interpretaciones


class RegistroPacientesForm(ModelForm):
    """
    FORMA PARA DAR DE ALTA LA BITACORA
    """
    fecha_hoy = forms.DateField(required=False)

    class Meta:
        model = Paciente
        exclude = ()

    fecha = forms.DateField(required=False)
    hora = forms.DateField(required=False)
    estudio_categoria = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(RegistroPacientesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                'REGISTRO DE PACIENTES',
                Field('hospital', wrapper_class="col-md-6"),
                Field('numero_seguro', wrapper_class="col-md-6"),
                Field('apellido_paterno', wrapper_class="col-md-3"),
                Field('apellido_materno', wrapper_class="col-md-3",
                      placeholder="Capturar Solo Si Tiene"),
                Field('nombre', wrapper_class="col-md-3"),
                Field('fecha_nacimiento', wrapper_class="col-md-3"),
                Field('edad', wrapper_class="col-md-3"),
                Field('sexo', wrapper_class="col-md-3"),
                Field('telefono', wrapper_class="col-md-3"),
                Field('email', wrapper_class="col-md-3"),
                Field('medico_referencia',wrapper_class="col-md-12"),
                Field('fecha_elaboracion_estudio', wrapper_class="col-md-6"),
                Field('hora_elaboracion_estudio', wrapper_class="col-md-6"),
                Field('estudio_adicional', wrapper_class="col-md-6")
                ),
            Fieldset(
                'ESTUDIOS SOLICITADOS',
                Field('estudio_1', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo1" value="Nuevo" class="btn btn-default">'''),
                Field('estudio_2', wrapper_class="col-md-6"),
                HTML('''<input type=button id="nuevo2" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_3', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo3" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_4', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo4" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_5', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo5" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_6', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo6" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_7', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo7" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_8',wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo8" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_9', wrapper_class="col-md-3"),
                HTML('''<input type=button id="nuevo9" value="Nuevo" class="btn btn-success">'''),
                Field('estudio_10', wrapper_class="col-md-3"),
                ),
        )
        self.fields['nombre'].label = 'Nombre:'
        self.fields['numero_seguro'].label = 'NSS:'
        self.fields['apellido_materno'].label = 'Apellido Materno:'
        self.fields['apellido_paterno'].label = 'Apellido Paterno:'
        self.fields['fecha_nacimiento'].label = 'Fecha de nacimiento:'
        self.fields['telefono'].label = 'Telefono Paciente:'
        self.fields['contacto_nombre'].label = 'Nombre Contacto:'
        self.fields['contacto_telefono'].label = 'Telefono Contacto:'
        self.fields['email'].label = 'Correo Electrónico:'
        self.fields['edad'].label = 'Edad:'
        self.fields['sexo'].label = 'Sexo:'
        self.fields['celular'].label = 'Celular Paciente:'
        self.fields['fecha_nacimiento'].label = 'Fecha De Nacimiento:'
        self.fields['medico_referencia'].label = 'Médico De Referencia:'
        self.fields['fecha_elaboracion_estudio'].label = 'Fecha De Elaboración Del Estudio:'
        self.fields['estudio_adicional'].label = 'Adicional'


class FiltrosForm(forms.Form):
    CENTRO = 1
    IMSS = 2
    PRADO = 3
    PERSONAL = 4
    NUCLEO = 5
    hospitales =(
                ('',''),
                ('CENTRO','Centro Medico Excel'),
                ('IMSS','IMSS NO.1'),
                ('PRADO','Centro Medico Del Prado'),
                ('NUCLEO','Nucleo Radiologico'),
                ('PERSONAL','Dr.David Aguilar Obeso'),
                ('ECO','Ecodiagnostica Portatil Del Rio'),
                ('INT','Instituto Nefrologico De Tijuana'),
                ('GUADALAJARA', 'Hospital Guadalajara'),
                ('CEMIQ', 'CEMIQ'),
                ('CRUZ ROJA', 'Cruz Roja'),
                ('AGEcography" Diagnostico Medico', 'AGEcography" Diagnostico Medico'),
                ('PREMIER Centro Medico', 'PREMIER Centro Medico'),
                ("SIMSA", "SIMSA")
    )
    adicionales =(('',''),
                    ('si','Si'))

    nombre = forms.CharField()
    hospital = forms.ChoiceField(choices=hospitales)
    adicional = forms.ChoiceField(choices=adicionales)

    def __init__(self, *args, **kwargs):
        super(FiltrosForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('nombre',
                      wrapper_class='col-md-3',
                      placeholder="Nombre, Apellidos"),
                Field('hospital', wrapper_class='col-md-3'),
                Field('adicional', wrapper_class='col-md-3'),

            ),
            FormActions(
                    Submit(
                        'Filtrar',
                        'Filtrar'
                    ),
                    HTML('<a class="btn btn-info"'),
                    HTML('''id="limpiar" href="/pacientes-registrados">
                     Limpiar</a>'''),
                )
        )
        self.fields['nombre'].required = False
        self.fields['hospital'].required = False
        self.fields['adicional'].required = False


class EstudiosInterpretacionesForm(ModelForm):
    class Meta:
        model = Estudios
        exclude = ()
        widgets = {
            'interpretacion_default': SummernoteWidget(attrs={
                'width': '50%', 'height': '400px'})}

    def __init__(self, *args, **kwargs):
        super(EstudiosInterpretacionesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Capturar Interpretacion Por Estudio',
                Field('nombre_estudio', wrapper_class='col-md-12'),
                Field('categoria', wrapper_class='col-md-12'),
                Field('interpretacion_default', wrapper_class='col-md-12'),
            ),
        )
        self.fields["interpretacion_default"].label = "Intrepretación"


class CrearInterpretacionForm(ModelForm):
    nombre = forms.CharField(required=False)
    sexo = forms.CharField(required=False)
    edad = forms.CharField(required=False)
    fecha_nacimiento = forms.CharField(required=False)
    nombre_estudio = forms.CharField(required=False)
    archivos_interpretacion = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Interpretaciones
        exclude = ('archivos',)
        widgets = {
            'interpretacion_creada': SummernoteWidget(attrs={
                'width': '1500px', 'height': '400px'})}

    def __init__(self, paciente, estudio, *args, **kwargs):
        super(CrearInterpretacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Datos Paciente',
                Field('nombre', wrapper_class='col-md-12'),
                Field('sexo', wrapper_class='col-md-4'),
                Field('edad', wrapper_class='col-md-4'),
                Field('fecha_nacimiento', wrapper_class='col-md-4'),
                Field('id_paciente', wrapper_class='col-md-4')
            ),
            Fieldset(
                'Intepretacion',
                Field('nombre_estudio', wrapper_class='col-md-12'),
                Field('archivos_interpretacion', wrapper_class='col-md-12'),
                Field('interpretacion_creada', wrapper_class='col-md-12'),
            ),
        )
        if estudio:
            self.fields['nombre_estudio'].initial = estudio.nombre_estudio
            self.fields['interpretacion_creada'].initial = estudio.interpretacion_default
        self.fields['nombre'].initial = paciente.nombre+' ' + paciente.apellido_paterno+' '+paciente.apellido_materno
        self.fields['sexo'].initial = paciente.sexo
        self.fields['edad'].initial = paciente.edad
        self.fields['fecha_nacimiento'].initial = paciente.fecha_nacimiento
        self.fields['id_paciente'].initial = paciente.pk
        self.fields['interpretacion_creada'].label = ''
        self.fields['archivos_interpretacion'].label = 'Imagenes'


# class EditarInterpretacionForm(ModelForm):
#     class Meta:
#         model = Interpretaciones
#         exclude = ()
#         widgets = {
#             'interpretacion_creada': SummernoteWidget(attrs={
#             'width': '50%', 'height': '400px'})}
#
#     def __init__(self, *args, **kwargs):
#         super(EditarInterpretacionForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Fieldset(
#                 'Intepretacion',
#                 Field('id_paciente', wrapper_class='col-md-12'),
#                 Field('nombre_estudio', wrapper_class='col-md-12'),
#                 Field('interpretacion_creada', wrapper_class='col-md-12'),
#             ),
#         )


class QueryInterpretaciones(forms.Form):
    nombre = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(QueryInterpretaciones, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('nombre',
                      wrapper_class='col-md-3',
                      placeholder="Nombre Estudios"),
            ),
            FormActions(
                    Submit(
                        'Filtrar',
                        'Filtrar'
                    ),
                    HTML('<a class="btn btn-info"'),
                    HTML('''id="limpiar" href="/estudios-default">
                     Limpiar</a>'''),
                )
        )
        self.fields['nombre'].required = False
