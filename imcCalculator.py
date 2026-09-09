def calculator_imc(weight: float, height: float):

    '''
    Calcula el IMC

    Params:
    -name: Nombre.
    -weight: Peso en Kilogramos.
    -height: Peso en metros.
    
    Return:
    -Devuelve el IMC
    '''

    imc = weight/(height*height)

    return imc



def area_circunferencia(r: float): 
    '''
        Calcula el area de una circunferencia
    
        Params:
        -r= Radio de la circunferencia
        
        Return:
        -Area de la circunferencia
    '''          
    PI = 3.14
    area = PI*(r*r)     


    