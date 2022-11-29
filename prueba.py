from helpers.model import new_model as model
from helpers.inter import interprete

Texto_variado = [
    'Nepomuceno Almonte recibió un plazo de 24 horas para salir a Ixmiquilpan, Hidalgo, en \n espera de instrucciones del gobierno; mientras que a Pedro Ampudia se le ordenó que \nmarchara a Cuernavaca',
    'La situación es, ¿qué pasa cuando a los personajes no se les asigna un nombre?, \n¿cómo pueden ser referentes?',
    'int i,suma=0;\nfor(i=1;i<=100;i++)\nsuma=suma+i;\n int i,j;',
    '#include <iostream>\nusing namespace std;\nint main() {\ncout << "Hola mundo, bienvenidos!" << endl;\nreturn 0;\n}',
    'El resultado de este primer análisis, permite identificar 3 grupos que permiten la clasificación de los\n programas de formación incluidos en la Base de información del SIRAF:',
    'import importlib.util\nspec = importlib.util.spec_from_file_location("foo.bar", "/path/to/file.py")\nfoo = importlib.util.module_from_spec(spec)'
]

analizando = model.predict(Texto_variado)

print(interprete(analizando))