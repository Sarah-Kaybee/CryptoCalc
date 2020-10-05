const http = require('http');
const api_key = "AIzaSyAnVo_7xUrGaiD3WJcEVXoFp8eB_UZ2lwM";

var options = {
  'method': 'GET',
  'hostname': 'mainnet.staked.cloud',
  'path': '/api/yields?api_key=${api_key}&extended=true&by_key=false'
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function (chunk) {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });

  res.on("error", function (error) {
    console.error(error);
  });
});

req.end();
