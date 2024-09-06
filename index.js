const fs = require("fs");

processComponents = JSON.parse(fs.readFileSync("itens.json"))["pedidos"];

processComponents = processComponents.sort(
  (a, b) => a.data - b.data || a.quantidade - b.quantidade
)[0];
