var carrello = [];

function validateInput(x) {
    trimmed = x.trim();
    if (trimmed.length <= 0)
        return undefined;
    return trimmed;
}

function addProduct() {
    event.preventDefault(); // submit del form

    let nome = validateInput(prodottoTXT.value);
    if (nome == undefined) {
        alert("Nome prodotto non valido!");
        return;
    }

    let filtrato = carrello.filter(x => x.nome == nome);
    if (filtrato.length > 0) {
        increaseQuantity(filtrato);
    } else {
        addNewProduct(nome);
    }
    stampa();
}

function addNewProduct(nome) {
    let prodotto = {
        nome: nome,
        prezzo: 10,
        quantita: 1
    };
    carrello.push(prodotto);
}

function increaseQuantity(filtrato) {
    filtrato[0].quantita++;

    // copia = filtrato[0];
    // idx = carrello.indexOf(copia);
    // carrello[idx].quantita++;
}

function removeProduct(daRimuovere) {
    idx = -1;
    for (let i = 0; i < carrello.length; i++) {
        if (carrello[i].nome == daRimuovere)
            idx = i;
    }
    carrello.splice(idx, 1);
    stampa();
}

function subQuantity(daRimuovere) {
    for (let i = 0; i < carrello.length; i++) {
        if (carrello[i].nome == daRimuovere) {
            carrello[i].quantita--;
            if (carrello[i].quantita <= 0)
                removeProduct(daRimuovere);
        }
    }
    stampa();
}

function addQuantity(daRimuovere) {
    for (let i = 0; i < carrello.length; i++) {
        if (carrello[i].nome == daRimuovere)
            carrello[i].quantita++;
    }
    stampa();
}

function stampa() {
    carrelloUL.innerHTML = "";
    for (let prodotto of carrello) {
        let item = prodotto.nome;
        // carrelloUL.innerHTML = "<li>" + item + "</li>"
        carrelloUL.innerHTML += /*html*/ `
            <li>${item} - ${prodotto.quantita}
                <button onclick="removeProduct('${item}')">X</button>
                <button onclick="subQuantity('${item}')">-</button>
                <button onclick="addQuantity('${item}')">+</button>
            </li>`;
    }
}