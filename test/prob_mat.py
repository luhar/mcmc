import numpy as np

note_dict = {}
note_dict["0"] = [1,2,3]
note_dict["1"] = [3,4,5]
note_dict["2"] = [2,3]
note_dict["3"] = [1,2,7]
note_dict["4"] = [3,4,5]
note_dict["5"] = [1]

def generate(n, note_dict):

	shape = (n, n)
	mat = np.zeros(shape)

	for i in range(n-1): #for reference
		for j in range(n): #source
			if not(i % 3 == 2 or j == i+1):
				mat[j][i+1] = similarity(note_dict[str(j)], note_dict[str(i)])
	for i in range(n):
		if i % 3 != 2:
			mat[i][i+1] = 1

	return mat

def similarity(arr1, arr2):

	l1 = len(arr1)
	l2 = len(arr2)

	if l1 < l2:
		arr1.extend([0 for _ in range(l2-l1)])
	elif l1 > l2:
		arr2.extend([0 for _ in range(l1-l2)])

	dot = np.dot(arr1, arr2)
	normalization = np.linalg.norm(arr1) * np.linalg.norm(arr2)
	return dot / normalization


print(generate(6, note_dict))
