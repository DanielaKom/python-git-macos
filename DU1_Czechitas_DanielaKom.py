import math

# V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. 
# Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

# Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut locality (lokalita, kde se pozemek nachází, 
# bude to objekt třídy Locality).

class Property:
    def __init__(self, locality: Locality):
        self.locality = locality

# Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. Třída bude mít atributy locality, 
# estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). Dále přidej metodu calculate_tax(), 
# která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math). 
# Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. 
# U atributu estate_type následující hodnoty a koeficienty:

class Estate(Property):
    estate_types = {
        "land": 0.85,
        "building site": 9,
        "forrest": 0.35,
        "garden": 2
    } 

    
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
    def calculate_tax(self):
        tax = self.area * self.estate_types[self.estate_type] * self.locality.locality_coefficient
        return f"Daň z uvedeného pozemku v lokalitě {self.locality.name} je: {math.ceil(tax)} Kč"

# Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.

blansko = Locality("Blansko", 2)
lesni_pozemek = Estate(blansko, "forrest", 500)
print(lesni_pozemek.calculate_tax())

# Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. Třída bude mít atributy locality, 
# area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání). 
# Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. 
# Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru commercial True, 
# tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        tax_residence = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            tax_residence = tax_residence * 2
            return f"Daň z uvedené nemovitosti v lokalitě {self.locality.name} je: {tax_residence} Kč"
        else:
            return f"Daň z uvedené nemovitosti v lokalitě {self.locality.name} je: {tax_residence} Kč"

# Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů čtverečních v lokalitě s koeficientem 3. 
# Potom je daň 60 * 3 * 15 = 2700. Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.

praha = Locality("Praha", 3)
byt_1 = Residence(praha, 60, False)
print(byt_1.calculate_tax())

byt_2 = Residence(praha, 60, True)
print(byt_2.calculate_tax())

# Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
  
manetin = Locality("Manětín", 0.8)
land_1 = Estate(manetin, "land", 900)
print(land_1.calculate_tax())

# Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.

dum_1 = Residence(manetin, 120, False)
print(dum_1.calculate_tax())

# Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. 
# Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.

brno = Locality("Brno", 3)
kancelar_1 = Residence(brno, 90, True)
print(kancelar_1.calculate_tax())
