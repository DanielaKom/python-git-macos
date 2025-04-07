# Část 1

# V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). 
# Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektui. 
# Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace. 
# S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO, 
# kde ICO nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). 
# S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd. Text, který API vrátí, 
# převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). Získané informace vypiš na obrazovku.

import json
import requests

ico_company = input("Zadejte prosím IČO požadovaného subjektu: ")

url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO".replace("ICO", ico_company)
company = requests.get(url)
data = company.json()
company_name = data.get("obchodniJmeno")
address = data.get("sidlo").get("textovaAdresa")
print(f"{company_name}")
print(f"{address}")


# Část 2

# Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. Napiš program, který se zeptá uživatele(ky) na název subjektu, 
# který chce vyhledat. Následně vypiš všechny nalezené subjekty, které ti API vrátí.
# V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat. 
# Request typu POST pošleme tak, že namísto funkce requests.get() použijeme funkci requests.post(). K requestu musíme přidat hlavičku (parametr headers), 
# který určí formát výstupních dat. Použij slovník níže.

# headers = {
#     "accept": "application/json",
#     "Content-Type": "application/json",
# }
# Dále přidáme parametr data, do kterého vložíme řetězec, který definuje, co chceme vyhledávat. Data vkládáme jako řetězec, který má JSON formát. 
# Pokud chceme například vyhledat všechny subjekty, které mají v názvu řetězec "moneta", použijeme následující řetězec.

# data = '{"obchodniJmeno": "moneta"}'
# Níže je příklad odeslání requestu:

# headers = {
#     "accept": "application/json",
#     "Content-Type": "application/json",
# }
# data = '{"obchodniJmeno": "moneta"}'
# res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

# Tentokrát API vrátí počet nalezených subjektů (pocetCelkem) a seznam nalezených subjektů ekonomickeSubjekty. Tvůj program by měl vypsat obchodní jména všech nalezených subjektů 
# a jejich identifikační čísla, výstupy odděluj čárkou.



import json
import requests

company_name = input("Zadejte prosím název hledaného subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = json.dumps({"obchodniJmeno": company_name})
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
data = response.json()
number_company = data.get("pocetCelkem")
companies = data.get("ekonomickeSubjekty")

print(f"Celkem bylo nalezeno: {number_company} subjektů.")

for company in companies:
    print(f"{company.get("obchodniJmeno")}, {company.get("ico")}")