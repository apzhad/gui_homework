from comtypes.client import CreateObject
import os
import random
import string
import sys
import getopt


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["count of groups", "file for group data"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 7
f = "groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(max_length):
    symbols = string.ascii_letters + string.digits + ' '*10
    return "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


xl = CreateObject("Excel.Application")
wb = xl.Workbooks.Add()
for i in range(n):
    xl.Range["A%s" % (i+1)].Value[()] = random_string(10)
xl.DisplayAlerts = 0
wb.SaveAs(os.path.join(project_dir, f))
xl.Quit()
