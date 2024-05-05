$(document).on("ready", function(){

	$( "#guardar_farmacia" ).on("click", function(){
		$.each( $( "input[name='surtido[]']:checked" ), function (index, value) {
			var data = $(this).parents('tr:eq(0)');
			var pk = $(data).find('td:eq(5)').text();
        	Dajaxice.pagoproveedores.UpdateRecetaFarmacos(Dajax.process, {'pk': pk} );
		});
	});


	$( "#guardar_imagenologia" ).on("click", function(){
		var pk = $("#id-imagenologia").val();

		var check_procedimiento1 = $("#check-procedimiento1").is(":checked");
		var check_procedimiento2 = $("#check-procedimiento2").is(":checked");
		var check_procedimiento3 = $("#check-procedimiento3").is(":checked");

		var precio_1 = $("#id_precio_1").val();
		var precio_2 = $("#id_precio_2").val();
		var precio_3 = $("#id_precio_3").val();

		if ( check_procedimiento1 ) {
        	Dajaxice.pagoproveedores.UpdateAutorizacionImagenologia(
        		Dajax.process, {'pk': pk, 'procedimiento': 1, 'precio': precio_1}
        	);
		}

		if ( check_procedimiento2 ) {
        	Dajaxice.pagoproveedores.UpdateAutorizacionImagenologia(
        		Dajax.process, {'pk': pk, 'procedimiento': 2, 'precio': precio_2}
        	);
		}

		if ( check_procedimiento3 ) {
        	Dajaxice.pagoproveedores.UpdateAutorizacionImagenologia(
        		Dajax.process, {'pk': pk, 'procedimiento': 3, 'precio': precio_3}
        	);
		}
	});

	$( "#guardar_laboratorio" ).on("click", function(){
		var pk, data;
		$.each( $( "input[name='surtido[]']:checked" ), function (index, value) {
			data = $(this).parents('tr:eq(0)');
			pk = $(data).find('td:eq(4)').text();
        	Dajaxice.pagoproveedores.UpdateSolicitudLaboratorio(Dajax.process, {'pk': pk} );
		});
	});

});
