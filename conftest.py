import pytest
from fixture.application import Application
from comtypes.client import CreateObject
import os


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Apps\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('xlsx_'):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata)


def load_from_xlsx(file):
    xl = CreateObject("Excel.Application")
    wb = xl.Workbooks.Open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "%s.xlsx" % file))
    data = []
    sheet = wb.worksheets[1]
    for i in range(sheet.UsedRange.Rows.Count):
        data.append(sheet.Range["A%s" % (i+1)].Value[()])
    xl.Quit()
    return data
