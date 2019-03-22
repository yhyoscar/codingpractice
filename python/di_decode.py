#2. Decode the encoded string
#i.e. "3[a]2[b]" return aaabb
#"2[ab]" return abab
#3[a2[bd]] return abdbdabdbdabdbd



def decode(s):
        """
        :type s: str
        :rtype: str
        """
        str_list = [""]
        count_list = [0]
        digit = ""
        for c in s:
            print(str_list)
            if c.isdigit():
                digit += c
            elif c == '[': 
                str_list.append("")
                count_list.append(int(digit))
                digit = ""
            elif c == ']':
                tmp_str, count = str_list.pop(), count_list.pop()
                str_list[-1] += tmp_str * count
            else:
                str_list[-1] += c
        print(str_list)
        return str_list[-1]

decode('adf3[a2[bd]]ef')

