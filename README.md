# challenge-dirmod
Unicamente acepta como moneda el parametro EUR ya que es la unica disponible en la capa gratuita de https://exchangeratesapi.io/  

# CloudFront
URL: https://d1izi6gd19d7cg.cloudfront.net/index.html  

# API Gateway
URL: https://pqlqcqe8q3.execute-api.us-east-2.amazonaws.com/prod  
Metodo: GET  
Parametros: base(Simbolo de Moneda), date(YYYY-MM-DD)  

# Logs funcion Lambda
Almacena los parametros recibidos como logs de CloudWatch con el siguiente formato: {'base': 'EUR', 'date': '2021-12-27'}  
