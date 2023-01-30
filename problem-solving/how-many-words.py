import re


def howMany(sentence):
    # initialize total with 0
    total = 0
# convert string into list
    slist = list(sentence.split())
# iterate list one by one
    for i in slist:
        # find all valid character in element
        j = re.findall("[a-zA-Z*,*?*\-!*.]", i)
        # compare length of element with new element
        if len(i) == len(j):
           # increment total by one
            total += 1

    return total


def main():
    ans = howMany("How many eggs are in a half-dozen, 13?")
    print(ans)


if __name__ == "__main__":
    main()
