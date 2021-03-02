// valida se data está no formato PTBR
var ValidaData = function(str) {
    var arrdata = str.split('-');
    var data = arrdata[2] + '/' + arrdata[1] + '/' + arrdata[0];

    return data == 'dd/mm/yyyy' ||
           ( /^\d{2}\/\d{2}\/\d{4}$/.test(data));

}

// converte virgula em ponto nas casas decimais
function AjustaDecimal(valor) {
    return valor.replace(",",".")
}

function AjustaInteger(valor) {
    return parseInt(valor)
}

function AjustaDecimal(valor) {
    return valor.replace(",",".")
}

function Formata_Decimal(valor,casa) {
    valor = parseFloat(valor.toFixed(casa));

    return (valor).toLocaleString('pt-BR');
}
