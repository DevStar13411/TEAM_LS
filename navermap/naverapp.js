var http = require('http');
var fs = require('fs');
var port = "7890";


//var request = require('request');

//var express = require('express');
//var app = express();



var app = http.createServer(function(request,response){
    var url = request.url;
    if(request.url == '/'){
		url = '/naver.html';
    }
    if(request.url == '/favicon.ico'){
		response.writeHead(404);
		response.end();
		return;
    }
    response.writeHead(200);
    response.end(fs.readFileSync(__dirname + url));
 
});

/*
function getHeaders2(url){
	return new Promise(resolve=>{
		request.get({
			uri:url,
			headers:{
				'X-NCP-APIGW-API-KEY-ID':id,
				'X-NCP-APIGW-API-KEY':key
			}
		},function (error, response, body) {
			//console.log('Status', response.statusCode);
			//console.log('Headers', JSON.stringify(response.headers));
			var bdjs = JSON.parse(body); //json으로 파싱
			//console.log(bdjs);
			var bdstr = JSON.stringify(bdjs);
			console.log(bdstr);
			//console.log(bdjs.route.trafast);
			//distance = bdjs.route.trafast[0].summary.distance;
			//console.log(distance);
			
			//console.log(urlq);
			//resolve(distance);
		})	
	})
	
};
*/

var urlq2 = 'https://openapi.map.naver.com/openapi/v3/maps.js?'+encodeURIComponent('ncpClientId')+'='+encodeURIComponent('Yt6FGzcl6jcUKFesbBGnLdhZJTyljALlqEfP8D8F');

/*
console.log(
	getHeaders2(urlq2)
		.then(function(result){
		return result
}))
*/

app.listen(port, function() {
	console.log('server running at http://localhost:'+port);
});
