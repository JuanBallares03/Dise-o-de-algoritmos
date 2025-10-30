# maps_utils.py
import webbrowser

def Busqueda_Ruta(origen, destino, paradas):
    url = f"https://www.google.com/maps/dir/?api=1&origin={origen}&destination={destino}"
    if paradas:
        url += "&waypoints=" + "|".join(paradas)

    print("\nAbriendo Google Maps con la ruta...")
    webbrowser.open(url)
