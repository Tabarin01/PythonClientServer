var carrello = [];

function salva() {
  stringaJSON = JSON.stringify(carrello);
  localStorage.setItem("carrello", stringaJSON);
}
function carica() {
  stringaJSON = localStorage.getItem("carrello");
  oggetto = JSON.parse(stringaJSON);
  if (oggetto) carrello = oggetto;
  stampa();
}
function addProduct() {
  let filtrato = carrello.filter((x) => x.nome == prodottoTXT.value);
  if (filtrato.length > 0) {
    increaseQuantity(filtrato);
  } else {
    addNewProduct();
  }
  stampa();
  event.preventDefault(); // submit del form
}
function addNewProduct() {
  let prodotto = {
    nome: prodottoTXT.value,
    prezzo: 10,
    quantita: 1,
  };
  carrello.push(prodotto);
}
function increaseQuantity(nomeProdotto) {
  let prodotto = carrello.filter((x) => x.nome == nomeProdotto);
  if (prodotto.length > 0) {
    prodotto[0].quantita++;
  }
  stampa();
}

function decreaseQuantity(nomeProdotto) {
  let prodotto = carrello.filter((x) => x.nome == nomeProdotto);
  if (prodotto.length > 0) {
    prodotto[0].quantita--;
    if (prodotto[0].quantita <= 0) {
      removeProduct(nomeProdotto);
    }
  }
  stampa();
}
function removeProduct(daRimuovere) {
  idx = -1;
  for (let i = 0; i < carrello.length; i++) {
    if (carrello[i].nome == daRimuovere) idx = i;
  }
  carrello.splice(idx, 1);

  stampa();
}

function stampa() {
  carrelloUL.innerHTML = "";
  for (let prodotto of carrello) {
    let item = prodotto.nome;
    carrelloUL.innerHTML += /*html*/ `
      <li>
        ${item} - ${prodotto.quantita}
        <button onclick="increaseQuantity('${item}')">+</button>
        <button onclick="decreaseQuantity('${item}')">-</button>
        <button onclick="removeProduct('${item}')">X</button>
      </li>
    `;
  }
}
