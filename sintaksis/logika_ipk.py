ipk = 12.4

if ipk > 4 or ipk < 0:
	print('IPK tidak valid')
	if ipk > 4:
		print('nilai IPK di atas normal')
	else:
		print('nilai IPK tidak boleh minus')
elif ipk >= 3.5 and ipk <= 4:
	print('Cumlaude')
elif ipk >= 2 and ipk < 3.5:
	print('Lulus')
else:
	print('Gagal')