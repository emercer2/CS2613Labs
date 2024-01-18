const prompt = require('prompt-sync')({sigint: true});

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

console.log("Select a command:\n\tn: Check a value\n\tq: Quit");
let input = prompt("");
while(input != "q"){
	if(input == "n"){
		let numInput = prompt("");
			var result = is_factorial(numInput);	
			if(result == 0){
				console.log(numInput + " is not the factorial of another number.");
			}
			else if(result == -1){
				console.log(numInput + " is a negative number.");
			}
			else{
				console.log(numInput + " is the factoiral of: " +  result);
			}
	}
	input = prompt("New command: ");
}

