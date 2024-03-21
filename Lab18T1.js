//TODO: Create a City class. It should take the name and the population as instance vars.
	//It should have an equals method that takes another city as a parameter
	//and returns true if this city's name and population match the other city's name and population
class City{
	constructor(name, population){
		this.name = name;
		this.population = population;
	}
	equals(city2){
		if((this.name === city2.name) && (this.population == city2.population)){
			return true;
		}
		else{
			return false;
		}
	}
}

class CityMap{
	//TODO: The programmer missed something in the constructor
	constructor(){
		this.adjacencyList = [];
	}
	addConnection(startCity, endCity, dist){
		//Adding first connection
		if(this.adjacencyList.length == 0){
			this.adjacencyList[0] = [startCity, [endCity], [dist]];
			this.adjacencyList[1] = [endCity, [startCity], [dist]];
		}
		else{
			//Check to see if startCity is in list
			let startCityFound = -1;
			for(let i = 0; i < this.adjacencyList.length; i++){
				if(this.adjacencyList[i][0].equals(startCity)){
					startCityFound = i;
					break;
				}
			}
			//startCity already registered in list
			if(startCityFound >= 0){
				this.adjacencyList[startCityFound][1][this.adjacencyList[startCityFound][1].length] = endCity;
				this.adjacencyList[startCityFound][2][this.adjacencyList[startCityFound][2].length] = dist;
			}
			//startCity is not registered
			else{
				this.adjacencyList[this.adjacencyList.length] = [startCity, [endCity], [dist]];
			}


			//TODO: Check to see if endCity is already in the adjacency list
				//If it is, add a connection to the startCity
				//If it is not, add it to the adjacency list then add its connection to startCity (could be one step)
				//Review the steps above to see how it is done with startCity instead of endCity
			//Check to see if endCity is in list
			let endCityFound = -1;
			if(startCityFound >= 0){
				for(let i = 0; i < this.adjacencyList.length; i++){
					if(this.adjacencyList[i][0].equals(endCity)){
						endCityFound = i;
						break;
					}
				}
				//startCity already registered in list
				if(endCityFound >= 0){
					this.adjacencyList[endCityFound][1][this.adjacencyList[endCityFound][1].length] = startCity;
					this.adjacencyList[endCityFound][2][this.adjacencyList[endCityFound][2].length] = dist;
				}
				//endCity is not registered
				else{
					this.adjacencyList[this.adjacencyList.length] = [endCity, [startCity], [dist]];
				}
			}	
		}
	}

	//TODO: Create a printMap() function that takes no parameters and prints the 
		//entire map. It should match the styling from the lab document.
	printMap(){
		for(let i = 0; i < this.adjacencyList.length; i++){
			console.log(this.adjacencyList[i][0].name);
			for(let j = 0; j < this.adjacencyList[i][1].length; j++){
				console.log("\t" + this.adjacencyList[i][1][j].name + " (" + this.adjacencyList[i][2][j] + "km)");
			}
		}
	}
}

//Main code goes here...

//TODO: Create the four cities listed on the lab document
let city1 = new City("Bathurst", 10000);
let city2 = new City("Miramichi", 3553);
let city3 = new City("Edmundston", 4545);
let city4 = new City("Campbellton", 4777);

//TODO: Create a map and add connections between Bathurst-Miramichi, Bathurst-Edmundston
	//Bathurst-Campbellton, and Edmundston-Campbellton
let map = new CityMap();
map.addConnection(city1, city2, 75.9);
map.addConnection(city1, city3, 248);
map.addConnection(city1, city4, 108);
map.addConnection(city3, city4, 200);

//TODO: Print the map using your the function you created
map.printMap();


