import re

def analyze(text):
	out = [0, 0, 0]
	arr = text.split()
	operators = {"+", "-", "*", "x" ,"/", "divided", "times", "time" ,"into"}
	
	for i in range(1, len(arr) - 1):
		print(arr[i])
		if arr[i] in operators:
			out[0] = arr[i]
			out[1] = arr[i-1]
			out[2] = arr[i+1]
			if arr[i+1] in ["by"]:
				out[2] = arr[i+2]

			break
	print(arr)
	if "factorial" in arr:
		a = arr.index("factorial")
		if arr[a+1] != "of":
			out = ["factorial", "0", arr[a+1]]
		if arr[a+1] == "of":
			out = ["factorial", "0", arr[a+2]]
	return out
