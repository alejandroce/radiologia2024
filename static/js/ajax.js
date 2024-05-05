function objetoAjax() {
  var xmlhttp = false;
  try {
    xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
  } catch (e) {
    try {
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (E) {
      xmlhttp = false;
    }
  }
  if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
    xmlhttp = new XMLHttpRequest();
  }
  return xmlhttp;
}

function ConsultaFiltrado(Pag, objId, objIdVacio) {
  divVacios = document.getElementById(objIdVacio);
  if (document.formulario.e2.value === "") {
    divVacios.innerHTML = "<div class='mensaje' align='justify'>Complete la informacion</div>";
  } else {
    divResultado = document.getElementById(objId);
    valor = document.formulario.e2.value;
    ajax = objetoAjax();
    ajax.open("POST", Pag+"?e2="+valor);
    ajax.onreadystatechange = function() {
      if (ajax.readyState == 4) {
        divResultado.innerHTML = ajax.responseText;
        divVacios.innerHTML = "";
      }
    };
    ajax.send(null);
  }
}

function ConsultaFiltrado(Pag, objId, objIdVacio) {
  divVacios = document.getElementById(objIdVacio);
  if (document.formulario.qp.value === "") {
    divVacios.innerHTML = "<div class='mensaje' align='justify'>Complete la informacion</div>";
  } else {
    divResultado = document.getElementById(objId);
    valor = document.formulario.qp.value;
    ajax = objetoAjax();
    ajax.open("POST", Pag+"?qp="+valor);
    ajax.onreadystatechange = function() {
      if (ajax.readyState == 4) {
        divResultado.innerHTML = ajax.responseText;
        divVacios.innerHTML = "";
      }
    };
    ajax.send(null);
  }
}
