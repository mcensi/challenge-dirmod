import json
import requests


def lambda_handler(event, context):
    #LOG
    print(event)

    
    #COMPROBACION DE PARAMETROS
    if not 'date' in event or not 'base' in event:
        return 'Los parametros son incorrectos'
    
    #DATOS REQUEST API
    baseURL = 'http://api.exchangeratesapi.io/v1/'
    date = event['date'].split('-')
    date = date[0] + f'-{int(date[1]):02d}' + f'-{int(date[2]):02d}'
    apiKey = ''
    base = event['base']
    URL = f'{baseURL}{date}?access_key={apiKey}&base={base}'
    
    
    #REQUEST
    response = requests.get(URL)
    responseCode = response.status_code
    data = response.json()
    
    
    #MANEJO DE ERRORES
    errors = ({
            104: 'Se supero la cuota de consultas mensuales a la API.',
            106: 'La solicitud no obtuvo resultados.',
            201: 'Se ingreso una moneda invalida.',
            301: 'No se ingreso ninguna fecha.',
            302: 'Se ingreso una fecha invalida.',
            400: 'Ocurrio un error inesperado.' })
    
    if responseCode in errors:
        error = f'Error {responseCode}: {errors[responseCode]}'
        return {
            'success': False,
            'Error': str(error)
        }
    elif 'success' in data and data['success'] == True:
        return {
            'success': True,
            'rates': data['rates']
        }
