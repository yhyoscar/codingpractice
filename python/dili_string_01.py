
# max length string with same first and last character
def max_string(string):
    if len(string) > 1:
        low = 0; high = len(string)-1
        listlow = {}; listhigh = {}
        count = 1
        while low < high:
            print(count, low, list(listlow.keys()), high, list(listhigh.keys()) )
            if string[low] not in listlow.keys():
                listlow[string[low]] = low
            if string[high] not in listhigh:
                listhigh[string[high]] = high

            if string[low] in listhigh.keys():
                return listhigh[string[low]] - low + 1, string[low:listhigh[string[low]]+1]
            if string[high] in listlow.keys():
                return high - listlow[string[high]] + 1, string[listlow[string[high]]:high+1]

            low += 1
            high -= 1
            count += 1 
        return 1, ''
    else:
        return 0, ''
print( max_string('') )


