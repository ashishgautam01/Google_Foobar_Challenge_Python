def solution(area):
	
	final = res = []
	calc_area = 0

	def inner_looper(area):
		inc_area = 0
		temp_sq = 0

		for x in range(area,0,-1):
			temp_sq = x**2

			if temp_sq <= area and isinstance(temp_sq,int):
				inc_area += temp_sq
				area = area - temp_sq
				return temp_sq
	

	temp_value = inner_looper(area)
	final.append(temp_value)
	print("First final : ",final)

	calc_area = area - temp_value
	print("calc_area : ",calc_area)

	while temp_value != area :
		loop_temp = inner_looper(calc_area)
		calc_area =calc_area - loop_temp
		print("loop_temp : ",loop_temp)
		if loop_temp == None:
			return final
		else :	
			temp_value += loop_temp
			final.append(loop_temp)

	return final

z = solution(12)
print(z)
