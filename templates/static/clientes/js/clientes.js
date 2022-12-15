function add_computador(){

    container = document.getElementById("form-computador")

    html = " <br><div class='row'><div class='col-md'> <input type='text' placeholder='Computador' class='form-control' name='computador' ></div><div class='col-md'><input type='text' placeholder='Tipo' class='form-control' name='tipo' ></div><div class='col-md'><input type='text' placeholder='Modelo' class='form-control' name='modelo' ></div><div class='col-md'><input type='text' placeholder='Descricao' class='form-control' name='descricao' ></div></div>"

    container.innerHTML += html
}

function exibir_form(tipo){

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if(tipo == "1"){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    }else if(tipo == "2"){
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"

    }

}

function dados_cliente(){
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-cliente').style.display = 'block'

        id = document.getElementById('id')
        id.value = data['cliente_id']

        nome = document.getElementById('nome')
        nome.value = data['cliente']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['cliente']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['cliente']['cpf']

        email = document.getElementById('email')
        email.value = data['cliente']['email']

        div_computador = document.getElementById('computador')
        div_computador.innerHTML = ""

        for(i=0; i<data['computador'].length; i++){
            div_computador.innerHTML += "\<form action='/clientes/update_computador/" + data['computador'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control'  name='computador' type='text' value='" + data['computador'][i]['fields']['computador'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control'  name='tipo' type='text' value='" + data['computador'][i]['fields']['tipo'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control'  name='modelo' type='text' value='" + data['computador'][i]['fields']['modelo'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control'  name='descricao' type='text' value='" + data['computador'][i]['fields']['descricao'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-success' type='submit'>\
                        </div>\
                    </form>\
                    <div class='col-md'>\
                        <a class='btn btn-danger' href='/clientes/excluir_computador/" + data['computador'][i]['id'] + "'>excluir</a>\
                    </div>\
                </div><br>"



        }
    })
}

function update_cliente(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('id').value

    fetch('/clientes/update_cliente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,

        })
    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterados com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }


    })
}