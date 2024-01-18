const readline = require("readline");

function is_factorial(num){
	var factorialOf = 0;
	if(num < 0){
		return -1;
	}
	for(var i = 1; i <= num ; i++){
		if(num % i == 0){
			//n is divisible by i
			num = num/i;
			factorialOf = i;
		}
		else{
			return 0;
		}
	}
	if(num == 1){
		return factorialOf;
	}
	else{
		return 0;
	}
}

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question("", function(line) {
	result = is_factorial(line);
	console.log("is_factorial(" + line + ") = " + result);
	rl.close();
});
