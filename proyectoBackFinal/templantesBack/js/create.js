function guardar() {
 
    let n = document.getElementById("txtNombre").value
    let p = parseFloat(document.getElementById("txtPrecio").value)
    let d = document.getElementById("txtDescripcion").value
    let i = document.getElementById("txtImagen").value
 
    let curso = {
        nombre: n,
        precio: p,
        descripcion: d,
        imagen: i

    }
    let url = "http://verolude1987.pythonanywhere.com/cursos"
    var options = {
        body: JSON.stringify(curso),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            window.location.href = "./index.html";  //NUEVO  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
 
}
