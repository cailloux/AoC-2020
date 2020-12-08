import re

f = open("./input/day4.in","r")

class Credentials():

    def __init__(self) -> None:
        super().__init__()
        self.byr = 0
        self.iyr = 0
        self.eyr = 0
        self.hgt = ""
        self.hcl = ""
        self.ecl = ""
        self.pid = 0
        self.cid = 0

    def isValid(self):
        if self.hgt:
            height = re.findall(r'[A-Za-z]+|\d+', self.hgt)
            if len(height) > 1:
                if height[1] == "in":
                    if 59 <= int(height[0]) <= 76:
                        pass
                    else:
                        self.hgt = ""
                elif height[1] == "cm":
                    if 150 <= int(height[0]) <= 193:
                        pass
                    else:
                        self.hgt = ""
                else:
                    self.hgt = ""
            else:
                self.hgt = ""

        if self.hcl:
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.hcl)
            if match:
                pass
            else:
                self.hcl = ""

        if self.pid:
            match = re.search(r'^[0-9]{9}$', self.pid)
            if match:
                pass
            else:
                self.pid = 0
        
        if self.ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            pass
        else:
            self.ecl = ""

        valid = False
        if (
            1920 <= int(self.byr) <= 2002
            and 2010 <= int(self.iyr) <= 2020
            and 2020 <= int(self.eyr) <= 2030
            and self.hgt
            and self.hcl
            and self.ecl
            and self.pid
        ):
            valid = True
        return valid

def processData(inputString):
    attributes = inputString.split(" ")
    attributes.pop()
    data = dict(s.split(':') for s in attributes)

    x = Credentials()

    x.byr = data.get("byr", 0)
    x.iyr = data.get("iyr", 0)
    x.eyr = data.get("eyr", 0)
    x.hgt = data.get("hgt", "")
    x.hcl = data.get("hcl", "")
    x.ecl = data.get("ecl", "")
    x.pid = data.get("pid", 0)
    x.cid = data.get("cid", 0)

    eval = x.isValid()
    
    if eval:
        return 1
    else:
        return 0

count = 0
dataString = ""

for line in f:
    if line == "\n":
        count += processData(dataString)
        dataString = ""
        continue
    dataString = dataString + line.rstrip() + " "


# When we get to the end of the file, we need to process the final data string
count += processData(dataString)

print(count)


f.close()
