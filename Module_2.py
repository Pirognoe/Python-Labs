x = "11111111"
z = -123.0
n = 4
m = 1
c = "A1Z"


def convert_n_to_m(x, n, m):
	DICT = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
        20: "K",
        21: "L",
        22: "M",
        23: "N",
        24: "O",
        25: "P",
        26: "Q",
        27: "R",
        28: "S",
        29: "T",
        30: "U",
        31: "V",
        32: "W",
        33: "X",
        34: "Y",
        35: "Z",
    }
	Reversed_dict = dict(zip(DICT.values(),DICT.keys()))
	i = 0 
	sum_10 = 0
	outcome = ""
	if type(x) == str or type(x) == int or type(x) == long or type(x) == complex:
		if x < 0:
			return False
		raw_input = str(x)
		raw_input = raw_input.upper()

		for element in raw_input[::-1]:
			sum_10 += Reversed_dict[element]*(n**i)
			i += 1
		
		if m == 1:
			for i in range(sum_10):
				outcome += "1"
		else:
			while (sum_10 // m) >= m:
				outcome += DICT[sum_10 % m]
				sum_10 = sum_10 // m
			outcome += DICT[sum_10 % m]
			outcome += DICT[sum_10 // m]
		
		return outcome[::-1]
	else:
		return False


print convert_n_to_m([1], 2, 2), 'False'
print convert_n_to_m(True, 1, 2), 'False'
print convert_n_to_m({1: 0}, 2, 2), 'False'
print convert_n_to_m(-777, 10, 2), 'False'
print convert_n_to_m(123123123123123123123.0, 11, 16), 'False'
print convert_n_to_m(100, 2, 1), '0000'
print convert_n_to_m(0, 10, 2), '0'
print convert_n_to_m(000, 10, 2), '0'
print convert_n_to_m(777, 10, 2), '1100001001'
print convert_n_to_m(777L, 10, 2), '1100001001'
print convert_n_to_m('000', 10, 2), '0'
print convert_n_to_m('ZZZZ', 36, 13), '46A672'
print convert_n_to_m('000ZZZZ', 36, 13), '46A672'
print convert_n_to_m('ZZZZ', 35, 13), 'False'
print convert_n_to_m('qweasd', 33, 36), 'HGPEYJ'
print convert_n_to_m('123123123123123123123', 11, 16), '2C09BC518E8048D23A'
print convert_n_to_m(123123123123123123123, 11, 16), '2C09BC518E8048D23A'
print convert_n_to_m(123123123123123123123, 10, 10), '123123123123123123123'
print convert_n_to_m('bnh34521', 31, 14), '119337DC2BC'
print convert_n_to_m('bnh34521', 11, 14), 'False'
