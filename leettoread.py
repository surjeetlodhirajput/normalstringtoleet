leet_words={'a': ['/-\\', '@', '/*\\', '/=\\', '/\\', '^', 'aye', 'λ', 'ci', 'Z', '(L', '∂', '4'],
		'b': ['|3', 'I3', '!3', 'ß', '(3', '/3', ')3', '|-]', ']3', 'j3', '6', '13', '8'],
		'c': ['[', '(', '<', '¢', '{', '©©', 'sea', 'see', '5'],
		'd': [')', '|)', '[)', '(|', '∂', '])', '|}', '|]', 'I>', '|>', '?', 'T)', 'I7',
			'0', 'ð', 'cl', '2'],
		'e': ['[-', '£', '&', '€', 'ə', 'ë', '|=-', '3'],
		'f': ['|=', 'ʃ’', '|#', ']=', '/=', '}', 'ph', '(=', 'ƒ', 'v', '7'],
		'g': ['[,', '&', '(_+', 'C-', 'gee', 'jee', 'cj', '(?,', '{,', '<-', '(.','6','9'],
		'h': ['|-|', '\\-/', '/-/', '#', ']-[', '[-]', ')-(', '(-)', '|~|', '|-|', ']~[',
			'!-!', '1-1', ':-:', '}{', '}-{', 'I+I', '{-}', '\\=\\', '|=|', '|.|', '|=|',
			'|*|', 'aych', '?', '6'],
		'i': ['!', '|', 'eye', '3y3', 'ai', '¡', '1'],
		'j': ['_|', '_/', ',_|', '_]', ',_]', '._|', '._]', ']', '¿', '</', '_)', 'ʝ', '01'],
		'k': ['|<', '>|', '1<', 'X', '|c', '|(', '|X', '|{', '05'],
		'l': ['|_', 'ВЈ', '|', '|_', 'lJ', '£', '¬', '1', '7', '07'],
		'm': ['/\\/\\', '|\\/|', 'em', '|v|', 'IYI', 'IVI', '[V]', '^^', 'nn',
			'//\\\\//\\\\', '(V)', '(v)', '{V}', '(\\/)', '|\\|\\', '/|\\', '/|/|',
			'<\\/>', '.\\\\', '/^^\\', '/V\\', '|^^|', 'AA', '44', '02'],
		'n': ['|\\|', '^/', '/\\/', '//\\\\//', '₪', '[\]', '<\\>', '{\\}', '/V', '//', 'ท',
			'И', '[]\\[]', ']\\[', '~', '03'],
		'o': ['()', 'oh', 'p', '<>', '[]', 'Ω', 'Ω', '¤', '0', '08'],
		'p': ['|*', '|o', '|º', '|>', '|"', '|^', '?', '9', '[]D', '|7', 'q', '¶', '℗',
			'þ', '|D', '66'],
		'q': ['0_', '0,', '(,)', '<|', 'cue', '&', '9', '2', '99'],
		'r': ['|2', '|9', '|?', '/2', 'I2', '|^', '|~', '|-', 'lz', 'В', 'I2', '[z',
			'|`', 'l2', 'ʁ', '.-', 'Я', '®', '2', '44'],
		's': ['$', 'z', '§', 'ehs', 'es', '5', '2', '55'],
		't': ['+', '-|-', '\'][\'', '†', '~|~', '«|»', '7', '1', '77'],
		'u': ['|_|', '(_)', 'Y3W', 'M', '[_]', '\_/', '\_\\', '/_/', 'L|', 'v', 'µ', 'บ', '88'],
		'v': ['\\/', '√', '\\\\//', '007'],
		'w': ['\\/\\/', 'vv', '\'//', '\\\\\'', '\\^/', '(n)', '\\X/', '\\|/', '\\_|_/',
			'\\\\//\\\\//', '\\_:_/', ']I[', 'UU', 'dubya', '\\V/', '\\X/', 'UU', '2u',
			'Ш', 'ɰ', '￦', 'JL', '008'],
		'x': ['><', '%', 'Р–', '}{', 'ecks', 'Г—', '*', ')(', '][', 'ex', '001'],
		'y': ['`/', 'j', '`(', '-/', '\'/', '\\//', 'φ', 'λ', 'Ч', '¥', 'Ψ', 7, '002'],
		'z': ['≥', '-/_', '~/_', '-\\_', '-|_', '>_', 's', '%', '7_', 'ʒ', 2, '003']
	}

"""
english_word={'/-\\': 'a', '@': 'a', '/*\\': 'a', '/=\\': 'a', '/\\': 'a', '^': 'a', 'aye': 'a', 'λ': 'a', 'ci': 'a', 'Z': 'a', '(L': 'a', '∂': 'a', '4': 'a',
'|3': 'b', 'I3': 'b', '!3': 'b', 'ß': 'b', '(3': 'b', '/3': 'b', ')3': 'b', '|-]': 'b', ']3': 'b', 'j3': 'b', '6': 'b', '13': 'b', '8': 'b',
'[': 'c', '(': 'c', '<': 'c', '¢': 'c', '{': 'c', '©©': 'c', 'sea': 'c', 'see': 'c', '5': 'c',
')': 'd', '|)': 'd', '[)': 'd', '(|': 'd', '∂': 'd', '])': 'd', '|}': 'd', '|]': 'd', 'I>': 'd', '|>': 'd', '?': 'd', 'T)': 'd', 'I7': 'd', '0': 'd', 'ð': 'd', 'cl': 'd', '2': 'd',
'[-': 'e', '£': 'e', '&': 'e', '€': 'e', 'ə': 'e', 'ë': 'e', '|=-': 'e', '3': 'e',
'|=': 'f', 'ʃ’': 'f', '|#': 'f', ']=': 'f', '/=': 'f', '}': 'f', 'ph': 'f', '(=': 'f', 'ƒ': 'f', 'v': 'f', '7': 'f',
'[,': 'g', '&': 'g', '(_+': 'g', 'C-': 'g', 'gee': 'g', 'jee': 'g', 'cj': 'g', '(?,': 'g', '{,': 'g', '<-': 'g', '(.': 'g', '6': 'g', '9': 'g',
'|-|': 'h', '\\-/': 'h', '/-/': 'h', '#': 'h', ']-[': 'h', '[-]': 'h', ')-(': 'h', '(-)': 'h', '|~|': 'h', ']~[': 'h', '!-!': 'h', '1-1': 'h', ':-:': 'h', '}{': 'h', '}-{': 'h', 'I+I': 'h', '{-}': 'h', '\\=\\': 'h', '|=|': 'h', '|.|': 'h', '|*|': 'h', 'aych': 'h', '?': 'h', '6': 'h',
'!': 'i', '|': 'i', 'eye': 'i', '3y3': 'i', 'ai': 'i', '¡': 'i', '1': 'i',
'_|': 'j', '_/': 'j', ',_|': 'j', '_]': 'j', ',_]': 'j', '._|': 'j', '._]': 'j', ']': 'j', '¿': 'j', '</': 'j', '_)': 'j', 'ʝ': 'j', '01': 'j',
'|<': 'k', '>|': 'k', '1<': 'k', 'X': 'k', '|c': 'k', '|(': 'k', '|X': 'k', '|{': 'k', '05': 'k',
'|_': 'l', 'ВЈ': 'l', '|': 'l', 'lJ': 'l', '£': 'l', '¬': 'l', '1': 'l', '7': 'l', '07': 'l',
'/\\/\\': 'm', '|\\/|': 'm', 'em': 'm', '|v|': 'm', 'IYI': 'm', 'IVI': 'm', '[V]': 'm', '^^': 'm', 'nn': 'm', '//\\\\//\\\\': 'm', '(V)': 'm', '(v)': 'm', '{V}': 'm', '(\\/)': 'm', 
'|\\|\\': 'm', '/|\\': 'm', '/|/|': 'm', '<\\/>': 'm', '.\\\\': 'm', '/^^\\': 'm', '/V\\': 'm', '|^^|': 'm', 'AA': 'm', '44': 'm', '02': 'm'
,'|\\|': 'n', '^/': 'n', '/\\/': 'n', '//\\\\//': 'n', '₪': 'n', '[\\]': 'n', '<\\>': 'n', '{\\}': 'n', '/V': 'n', '//': 'n', 'ท': 'n', 'И': 'n', '[]\\[]': 'n', ']\\[': 'n', '~': 'n', "03": "n",
'()': 'o', 'oh': 'o', 'p': 'o', '<>': 'o', '[]': 'o', 'Ω': 'o', '¤': 'o', '0': 'o', '08': 'o',
'|*': 'p', '|o': 'p', '|º': 'p', '|>': 'p', '|"': 'p', '|^': 'p', '?': 'p', '9': 'p', '[]D': 'p', '|7': 'p', 'q': 'p', '¶': 'p', '℗': 'p', 'þ': 'p', '|D': 'p', '66': 'p',
'0_': 'q', '0,': 'q', '(,)': 'q', '<|': 'q', 'cue': 'q', '&': 'q', '9': 'q', '2': 'q', '99': 'q',
'|2': 'r', '|9': 'r', '|?': 'r', '/2': 'r', 'I2': 'r', '|^': 'r', '|~': 'r', '|-': 'r', 'lz': 'r', 'В': 'r', '[z': 'r', '|`': 'r', 'l2': 'r', 'ʁ': 'r', '.-': 'r', 'Я': 'r', '®': 'r', '2': 'r', '44': 'r',
'$': 's', 'z': 's', '§': 's', 'ehs': 's', 'es': 's', '5': 's', '2': 's', '55': 's',
'+': 't', '-|-': 't', "']['": 't', '†': 't', '~|~': 't', '«|»': 't', '7': 't', '1': 't', '77': 't',
'|_|': 'u', '(_)': 'u', 'Y3W': 'u', 'M': 'u', '[_]': 'u', '\\_/': 'u', '\\_\\': 'u', '/_/': 'u', 'L|': 'u', 'v': 'u', 'µ': 'u', 'บ': 'u', '88': 'u',
'\\/': 'v', '√': 'v', '\\\\//': 'v', '007': 'v',
'\\/\\/': 'w', 'vv': 'w', "'//": 'w', "\\\\'": 'w', '\\^/': 'w', '(n)': 'w', '\\X/': 'w', '\\|/': 'w', '\\_|_/': 'w', '\\\\//\\\\//': 'w', '\\_:_/': 'w', ']I[': 'w', 'UU': 'w', 'dubya': 'w', '\\V/': 'w', '2u': 'w', 'Ш': 'w', 'ɰ': 'w', '￦': 'w', 'JL': 'w', '008': 'w',
'><': 'x', '%': 'x', 'Р–': 'x', '}{': 'x', 'ecks': 'x', 'Г—': 'x', '*': 'x', ')(': 'x', '][': 'x', 'ex': 'x', '001': 'x',
'`/': 'y', 'j': 'y', '`(': 'y', '-/': 'y', "'/": 'y', '\\//': 'y', 'φ': 'y', 'λ': 'y', 'Ч': 'y', '¥': 'y', 'Ψ': 'y', 7: 'y', '002': 'y',
'≥': 'z', '-/_': 'z', '~/_': 'z', '-\\_': 'z', '-|_': 'z', '>_': 'z', 's': 'z', '%': 'z', '7_': 'z', 'ʒ': 'z', 2: 'z', '003': 'z'}
"""
from constant import leet_words
import random 
def word_to_leet(string="",leet_len=0):
    if(len(string)==leet_len):
        return '\0'
    if string[leet_len] not in leet_words.keys():
        return "   "+word_to_leet(string,leet_len+1)
    return leet_words[string[leet_len]][random.randint(0,(len(leet_words[string[leet_len]]))-1)]+word_to_leet(string,leet_len+1)

def leet_to_word(string="z/_/|?_/3|=-~|~   7()T)|=|¡   [z(Lʝ℗[_]-|-"):
    leet_wordlist=string.split(' ')
    for i in leet_words.keys():
    	print("s")


if __name__=="__main__":
    string=input(">>Enter the words to convert into the leet language  ")
    leet=word_to_leet(string=string)
    flag=True
    while flag:
        inp=input(">>Want to save into the file or not 1 for True 0 for False  ")
        if  inp=='1':
            file=input("Enter the file name in which you want to save the leet string  ")
            f=open(file,'wb')
            f.write(leet.encode())
            f.close()
            flag=False

        if inp=='0':
            flag=False

	