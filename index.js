const { createServer } = require('node:http');
const { readFileSync } = require('node:fs');
const { resolve } = require('node:path');
const hostname = '0.0.0.0';
const port = 8094;
const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const htmlContent = readFileSync(resolve(__dirname, 'index.html'), 'utf8');
  res.end(htmlContent);
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});