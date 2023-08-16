def timeToMs(time):
	time = time.split(':')
	if len(time) > 2:
		return int((float(time[0]) * 3600 + float(time[1]) * 60 + float(time[2])) * 1000)
	else:
		return int((float(time[0]) * 60 + float(time[1])) * 1000)