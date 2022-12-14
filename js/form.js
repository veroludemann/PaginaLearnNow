const $form = document.querySelector('#form')
const $buttonMailto = document.querySelector('#trucazo')

$form.addEventListener('submit', handleSubmit)

function handleSubmit(event){
    event.preventDefault()
    const form = new FormData (this)
    console.log(form.get('name'))
    $buttonMailto.setAttribute('href',`micaalfonzo98@gmail.com?subject= Nombre: ${form.get('name')} Apellido: ${form.get('name')} Correo: ${form.get('email')}&body=${form.get('message')}`)
    $buttonMailto.click()
}
