# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def count_calories(path):
    f = open(path, "r")
    actcalories = 0
    appendelement = True
    calories = []
    calories.append(0)
    for x in f:
        if x == '\n':
            for i in range(len(calories)):
                if actcalories > calories[i]:
                    calories.insert(i,actcalories)
                    appendelement = False
                    break
            if appendelement:
                calories.append(int(x))
            actcalories = 0
        else:
            actcalories += int(x)
    print(f'Kalorien aufsummiert : {calories[0] + calories[1] + calories[2]}')


def rock_paper_scissors(path):
    f = open(path, "r")
    points = 0
    for x in f:
        if x == 'A X\n':
            points += 3
        elif x == 'A Y\n':
            points += 4
        elif x == 'A Z\n':
            points += 8
        elif x == 'B X\n':
            points += 1
        elif x == 'B Y\n':
            points += 5
        elif x == 'B Z\n':
            points += 9
        elif x == 'C X\n':
            points += 2
        elif x == 'C Y\n':
            points += 6
        elif x == 'C Z\n':
            points += 7
    print(f'Gesamtpunktzahl : {points}')


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]


def rucksack_reorganisation_part1(path):
    f = open(path, 'r')
    list = []
    list2 = []
    sum = 0
    for x in f:
        chunk = chunks(x, int(len(x)/2))
        for i in chunk:
            if i != '\n':
                list.append(i)
    for i in range(int(len(list)/2)):
        for j in list[i*2]:
            if j in list[i*2+1]:
                list2.append(j)
                break
    for i in list2:
        if i.islower():
            sum += ord(i) - 96
        else:
            sum += ord(i) - 38
    print(sum)


def rucksack_reorganisation_part2(path):
    f = open(path, 'r')
    list = []
    list2 = []
    sum = 0
    for x in f:
        list.append(x)
    for i in range(int(len(list)/3)):
        for j in list[i*3]:
            if j in list[i*3+1]:
                if j in list[i*3+2]:
                    list2.append(j)
                    break
    for i in list2:
        if i.islower():
            sum += ord(i) - 96
        else:
            sum += ord(i) - 38
    print(sum)


def camp_cleanup_part1(path):
    f = open(path, 'r')
    list = []
    count = 0
    for x in f:
        i = x.split(',')
        list.append(i)
    for i in list:
        for j in i:
            j = j.split('-')


class TreeElement:

    def __init__(self, value, parent, name):
        self.value = value
        self.parent = parent
        self.name = name
        self.children = []

    def refreshvalue(self):
        for x in self.children:
            self.value = self.value + x.value

    def getchild(self, name):
        return self.children[name]

    def getparent(self):
        return self.parent

    def getvalue(self):
        return self.value
    
    def addchild(self, child):
        self.children.append(child)


def day7_tree(path):
    f = open(path, 'r')
    root = TreeElement(0, 'none')
    actualdirectory = root
    for x in f:
        parts = x.split(' ')
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '/':
                    actualdirectory = root
                elif parts[2] == '..':
                    actualdirectory = actualdirectory.getparent()
                else:
                    actualdirectory = actualdirectory.getchild(parts[2])
        elif parts[0] == 'dir':
            tmp = TreeElement(0, actualdirectory, parts[1])
            actualdirectory.addchild(tmp)
        else:
            tmp = TreeElement(parts[0], parts[1], 'file')
            actualdirectory.addchild(tmp)
    b = True
    count = 0
    actualdirectory = root
    while b:




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rucksack_reorganisation_part2("C:\\Users\\svekr\\Desktop\\rucksack.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
