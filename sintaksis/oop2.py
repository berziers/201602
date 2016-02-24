class BujurSangkar():
	def __init__(self,sisi):
		self.sisi = sisi

	def hitung_luas_bujursangkar(self):
		hasil = self.sisi * self.sisi
		return hasil

bs1 = bujursangkar(10)
print(bs1.hitung_luas_bujursangkar())