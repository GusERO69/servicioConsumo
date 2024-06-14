const { createServer } = require("node:http");
const hostname = "127.0.0.1";
const port = 8000;
const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");

  // let arreglo = [
  //   {
  //     nombre: "Gustavo",
  //     apellido: "Plasencia",
  //   },
  //   {
  //     nombre: "Pepe",
  //     apellido: "Lucho",
  //   },
  // ];
  let arreglo = [
    [0, 1],
    [0, 0],
    [1, 0],
    [1, 1],
  ];

  res.end(JSON.stringify(arreglo));

  // res.end("Soy el grupo 4");
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
