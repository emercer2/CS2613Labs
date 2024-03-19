from abc import ABC, abstractmethod

class TradingCard(ABC):
	def __init__(self, ident, rare, year):
		self.ID = ident
		self.rarity = rare
		self.releaseYear = year

	@abstractmethod
	def cost(self):
		pass

	def getID(self):
		return str(self.ID)
		
	def getRarity(self):
		return str(self.rarity)

	def getReleaseYear(self):
		return str(self.releaseYear)
		
	def setRarity(self, newRarity):
		if(10 < newRarity or newRarity < 1):
			return "-1"
		else:
			self.rarity = newRarity
			return str(self.rarity)
			
	def to_string(self):
		return "#" + str(self.ID) + " (" + str(self.releaseYear) + "): Rarity: " + str(self.rarity)
		
class HockeyCard(TradingCard):

	def __init__(self, ident, rare, releaseYr, playerNm, jerseyNm, gamesW):
		super().__init__(ident, rare, releaseYr)
		self.playerName = playerNm
		self.jerseyNum = jerseyNm
		self.gamesWon = gamesW

	def cost(self):
		return str(format (int(self.gamesWon) * (2023 - int(super().getReleaseYear()))/10*(0.15+int(super().getRarity())), ".2f"))
		
	def getPlayerName(self):
		return str(self.playerName)
		
	def getJerseyNum(self):
		return str(self.jerseyNum)

	def getGamesWon(self):
		return str(self.gamesWon)
		
	def to_string(self):
		return super().to_string() + " Cost: $" + str(self.cost() + "\n" + str(self.playerName) + " " + str(self.jerseyNum) + " - " + str(self.gamesWon) + " Games Won")


class PlayingCard(TradingCard):

	def __init__(self, ident, rare, releaseYr, holo, cond):
		super().__init__(ident, rare, releaseYr)
		self.holographic = holo
		self.condition = cond
				
	def getHolographic(self):
		return str(self.holographic)
		
	def getCondition(self):
		return str(self.condition)
		
	def setCondition(self, newCond):
		if(newCond == "Mint" or newCond == "Good" or newCond == "Poor"):
			self.condition = newCond
			return str(self.condition)
		else:
			return "-1"
			
	def cost(self):
		value = 0
		if(self.holographic):
			value = 5
		else:
			value = 1
		if(self.condition == "Mint"):
			value = value * 5.15 * (int(super().getRarity())/2)
		elif(self.condition == "Good"):
			value = value * 2.15 * (int(super().getRarity())/2)
		elif(self.condition == "Poor"):
			value = value * 0.5 * (int(super().getRarity())/2)
		return str(format(value, ".2f"))
		
	def to_string(self):
		return super().to_string() + " Cost: $" + str(self.cost() + "\nHolographic: " + str(self.holographic) + " Condition: " + str(self.condition))

#Driver
cardLst = []

#Hockey Cards
hc1 = HockeyCard(1, 1, 2001, "Fake Name1", 10, 1)
hc2 = HockeyCard(12, 10, 2012, "Fake Name12", 11, 13)
hc3 = HockeyCard(123, 8, 2013, "Fake Name123", 12, 1)
hc4 = HockeyCard(1234, 1, 2021, "Fake Name1234", 13, 3)
hc4.setRarity(50)
hc5 = HockeyCard(12345, 7, 2011, "Fake Name12345", 14, 100)
hc5.setRarity(5)

cardLst.append(hc1)
cardLst.append(hc2)
cardLst.append(hc3)
cardLst.append(hc4)
cardLst.append(hc5)

#Playing Cards
pc1 = PlayingCard(134, 10, 2010, True, "Poor")
pc2 = PlayingCard(1346, 1, 2012, False, "Mint")
pc3 = PlayingCard(1345, 3, 2013, True, "Good")
pc4 = PlayingCard(13456, 8, 2016, False, "Poor")
pc4.setCondition("Hello")
pc5 = PlayingCard(14567, 2, 2010, True, "Mint")
pc5.setCondition("Poor")

cardLst.append(pc1)
cardLst.append(pc2)
cardLst.append(pc3)
cardLst.append(pc4)
cardLst.append(pc5)

def topThree(lst):
	results = []

	for i in range(0, 3):
		if(len(lst) > 0):
			curMax = lst[0];
			for item in lst:
				if float(item.cost()) > float(curMax.cost()):
					curMax = item
			lst.remove(curMax)
			results.append(curMax)
	for item in results:
		print(item.to_string())

totValue = 0
costs = []
for item in cardLst:
	totValue = totValue + float(item.cost())

print("Total Value: " +  str(totValue) + "\n")
topThree(cardLst)







