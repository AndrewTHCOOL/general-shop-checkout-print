txt = "MAXIMA LT UAB"
x = txt.center(41)
print(x)
txt = "S. Daukanto g. 1A. Telsiai , Kasa Nr. 5"
x = txt.center(41) 
print(x)
txt = "PVM moketojo kodas LT230335113"
y = txt.center(36)
print(y)
txt = "#D1273891" 
c = txt.rjust(39) #nukreipe teksta i gala
print(c)
print("Kvitas 109/2282")
morkos=	{
  "Produkto pavadinimas": "Sviezios Morkos", #produkto informacija
  "kiekis": 0.330, 
  "vieneto kaina": 1.99,
  }
obouoliai=	{
  "Produkto pavadinimas": "Obuoliai. nuo 65mm 'IDARED'",
  "kiekis": 1.374,
  "vieneto kaina": 2.29,
  }
agurkai= {
  "Produkto pavadinimas": "Trumpavaisiai agurkai",
  "kiekis": 0.394,
  "vieneto kaina": 14.99,
  }
cesnakai= {
  "Produkto pavadinimas": "Cesnakai",
  "kiekis": 0.152,
  "vieneto kaina": 10.99,
  }
saliamis= {
  "Produkto pavadinimas": "Vytintas saliamis MILAND a.",
  "kiekis": 0.254,
  "vieneto kaina": 20.00,
  }
silkes= {
  "Produkto pavadinimas": "Karstai rukytos Atlanto silkes",
  "kiekis": 1.000,
  "vieneto kaina": 5.29,
  }

bendras = morkos["kiekis"] * morkos["vieneto kaina"] # suskaiciavimas
bendras2 = obouoliai["kiekis"] * obouoliai["vieneto kaina"]
bendras3 = agurkai["kiekis"] * agurkai["vieneto kaina"]
bendras4 = cesnakai["kiekis"] * cesnakai["vieneto kaina"]
bendras5 = saliamis["kiekis"] * saliamis["vieneto kaina"]
bendras6 = silkes["kiekis"] * silkes["vieneto kaina"]
print("Šviežios Morkos")
print("1.99 X 0.330 KG", end = '                    ',), 
print(round(bendras, 2,)), # round komanda suapvalina
print("Obuoliai. nuo 65mm 'IDARED'")
print("2.29 X 1.374 KG", end = '                    ',), 
print(round(bendras2, 2)),
print("Trumpavaisiai agurkai")
print("14.99 X 0.394 KG", end = '                   ',), 
print(round(bendras3, 2)),
print("Česnakai")
print("10.99 X 0.152 KG", end = '                   ',), 
print(round(bendras4, 2)),
print("Vytintas saliamis MILAND a. \nr.")
print("20.00 X 0.254 KG", end = '                   ',), 
print(round(bendras5, 2)),
print("Karstai rukytos Atlanto \nsilkes", end = '                             ',)
print(bendras6),
print ("***************************************")
print("          Be PVM", end = '      PVM    ',),
print("    Su PVM"),
bendrasv = morkos["kiekis"] * morkos["vieneto kaina"]+ obouoliai["kiekis"] * obouoliai["vieneto kaina"] + \
  agurkai["kiekis"] * agurkai["vieneto kaina"] + cesnakai["kiekis"] * cesnakai["vieneto kaina"] + \
   saliamis["kiekis"] * saliamis["vieneto kaina"] + silkes["vieneto kaina"] * silkes["kiekis"]

pvm = bendrasv / 121 * 21
be_pvm = bendrasv - pvm #pvm apskaiciavimas
su_pvm = bendrasv
stuff_in_string = "A=21.00%  {0:2.2f} {1:9.2f} {2:13.2f} ".format(be_pvm, pvm, su_pvm)
print(stuff_in_string)
print ("***************************************")
print("Moketi", end = '                            ',)
print(round(su_pvm, 2))
print("Moketa", end = '                            ',)
k = 22.00
l = k - su_pvm
print (k)
print("Graza", end = '                              ',)
print (round(l, 2))
print("MAXIMA kortele 944000******7188", end = '       ')
print ("#")
print("Is viso MAXIMA PINIGU už kvitą 0.22", end = '   ',)
print ("#")
print("MAXIMA PINIGU likutis sąskaitoje 3.19", end = ' ',)
print ("#")
txt = "Nemokama MAXIMOS Infolinija:"
f = txt.center(36)
print(f)
txt = "{8 800} 20050 {8-22 val}"
o = txt.center(36)
print(o)
txt = "AČIŪ. KAD PIRKOTE\n"
m = txt.center(36)
print(m)
print ("Kasininkas(-ė) 60 5")
print ("LT LS 0000101AFF29  2013-04-14 13:42:52")