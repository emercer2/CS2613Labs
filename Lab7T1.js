const fs = require('fs');
var res = [{"calc" : 0, "performer" : ""}, {"calc" : 0, "performer" : ""}, {"calc" : 0, "performer" : ""}];
var names = [];

var fileCount = 0;
while(true){
	try{
		fileCount++;
		let fileString = 'calculations' + fileCount + '.json';
		let jsonData = fs.readFileSync(fileString, 'utf8');
		let currentData = JSON.parse(jsonData).data.calculations;
		
		let trueVal = parseFloat(currentData[0].calc);

		
		temp = []
		temp[0] = currentData[1];
		temp[1] = currentData[2];
		temp[2] = currentData[3];
		
		for(let i=0; i<temp.length; i++){
			res[i].calc += Math.abs(parseFloat(temp[i].calc) - trueVal);
			res[i].performer = temp[i].performer;
		}
	} 
	catch (error) {
		break;
	}
}

res = res.sort((a,b) => (a.calc > b.calc) ? 1 : ((b.calc > a.calc) ? -1 : 0));
for(let i=0; i<res.length; i++){
	console.log(i+1 + ".\t" + res[i].performer + "\t(" + parseFloat(res[i].calc) + ")")
}
