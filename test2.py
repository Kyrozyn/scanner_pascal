kata = ""
namatoken = ""
kamus = []
karakter = ""


def initkamus():
    f = open("kamus.txt", "r")
    for x in f:
        z = x.rstrip()
        kamus.append(z)


def result():
    print(kata + " : " + namatoken)


def check_keyword(s):
    if s in kamus:
        global namatoken
        namatoken = "Keyword"


def look():
    with open('sourceb.txt') as f:
        while True:
            global karakter
            global kata
            global namatoken
            karakter = f.read(1)

            if "{" in karakter:
                while True:
                    karakter = f.read(1)
                    if "}" in karakter:
                        break
                kata = ""

            if chr(39) in karakter:
                while True:
                    kata = kata + karakter
                    karakter = f.read(1)
                    if chr(39) in karakter:
                        break
                kata = kata + karakter
                namatoken = "Literals"
                result()
                kata = ""
            import string
            if karakter in string.ascii_lowercase[:26]:
                while True:
                    kata = kata + karakter
                    karakter = f.read(1)
                    if not karakter in string.ascii_lowercase[:26]:
                        break
                namatoken = "Identifier"
                check_keyword(kata)
                result()
                kata = ""
            if str.isnumeric(karakter):
                while True:
                    kata = kata + karakter
                    karakter = f.read(1)
                    if not str.isnumeric(karakter):
                        break
                namatoken = "Identifier"
                result()
                kata = ""
            if karakter in ["+", "-", "*", "/", "^"]:
                while True:
                    kata = kata + karakter;
                    karakter = f.read(1)
                    if not karakter in ["+", "-", "*", "/", "^"]:
                        break
                namatoken = "operator"
                result()
                kata = ""

            if karakter in ["(", ")", "[", "]", "^", ":", "=", ";", ",", "."]:
                kata = karakter
                namatoken = "Punctuation"
                result()
                kata = ""
initkamus()
look()
