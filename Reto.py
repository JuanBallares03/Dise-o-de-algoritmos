import requests

def ConectarAPI():
    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    ConvertirJSON = response.json()
    return ConvertirJSON

ListaAPI = ConectarAPI()
# print(ListaAPI)
paises = []
for pais in ListaAPI:
    paises.append(pais["name"]["common"])
# print(paises)

OpcionUsuario = input("Porfavor digite el nombre del pais:")
def BuscarPaisLineal(lista):
   UrlMostrar = []
   for pais in lista:
       if pais["name"]["common"] == OpcionUsuario:
           UrlMostrar.append(pais["maps"]["googleMaps"])
           return UrlMostrar
   return "No se encontró"

print(BuscarPaisLineal(ListaAPI))


#Busqueda Binaria
paises.sort()
# print (paises)
def BuscarPaisBinaria(lista_api, lista_paises, pais_buscado):
    inicio = 0
    fin = len(lista_paises) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_paises[medio] == pais_buscado:
            # Cuando lo encuentra, recorro la API para sacar la URL
            for pais in lista_api:
                if pais["name"]["common"] == lista_paises[medio]:
                    return pais["maps"]["googleMaps"]
        elif lista_paises[medio] < pais_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return "No se encontró"

print(BuscarPaisBinaria(ListaAPI, paises, OpcionUsuario))