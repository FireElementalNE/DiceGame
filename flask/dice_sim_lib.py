import urllib.request
import random

class Player():
	def __init__(self, n):
		self.name = n
		self.wins = 0

class Game():
	def __init__(self, s, n1, n2):
		self.players = [Player(n1), Player(n2)]
		self.winning = 0
		self.losing = 1
		self.round_num = 1
		self.text = {}
		random.seed(s)
	
	def round(self):
		w_roll = random.randint(1,100)
		self.text[str(self.round_num)] = []
		self.text[str(self.round_num)].append("{} (the current winner) rolled a {}".format(self.players[self.winning].name, w_roll))
		game_over = False
		while not game_over:
			result = self.roll(w_roll)
			if result[0] == 1:
				tmp = self.winning
				self.winning = self.losing
				self.losing = tmp
				w_roll = result[1]
			elif result[0] == 0:
				self.players[self.winning].wins += 1
				game_over = True
			elif result[0] == -1:
				self.players[self.winning].wins += 1
				game_over = True
		self.text[str(self.round_num)].append("{} Wins!".format(self.players[self.winning].name))
		self.round_num += 1
		
	def roll(self, to_beat):
		new_roll = random.randint(1,100)
		self.text[str(self.round_num)].append("{} (the current loser) rolled a {}".format(self.players[self.losing].name, new_roll))
		if new_roll < to_beat:
			return [1, new_roll]
		elif new_roll == to_beat:
			return [0, new_roll]
		elif new_roll > to_beat:
			return [-1, new_roll]

def play(n1, n2, rounds):	
	url = 'https://www.random.org/integers/?num=1&min=-1000000000&max=1000000000&col=1&base=10&format=plain&rnd=new'
	s = int(urllib.request.urlopen(url).read())

	G = Game(s, n1, n2)
	for i in range(rounds):
		G.round()

	final_text = G.text
	final_text["result"] = []
	final_text["result"].append("{} has {} wins.".format(G.players[G.losing].name, G.players[G.losing].wins))
	final_text["result"].append("{} has {} wins.".format(G.players[G.winning].name, G.players[G.winning].wins))

	return final_text