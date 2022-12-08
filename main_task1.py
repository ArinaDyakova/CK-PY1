# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
def dict_bin_dec_hex_oct(i):
    # for i in range(16):
        dict_bin = {'bin': bin(i)}
        dict_dec = {'dec': i}
        dict_hex = {'hex': hex(i)}
        dict_oct = {'oct': oct(i)}
        return {
            **dict_bin,
            **dict_dec,
            **dict_hex,
            **dict_oct
        }

result = [dict_bin_dec_hex_oct(i) for i in range(16)]
pprint(result)
