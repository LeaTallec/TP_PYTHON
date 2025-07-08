# créez une fonction qui prend en paramètres un **kwargs
# et qui renvoi la concaténation de toutes les clés valeur
# exemple function(je="suis", un="kwarg") doit renvoyer "jesuisunkwarg"
# exemple function(la="jolie", maison="dans", la="prairie") doit renvoyer "lajoliemaisondanslaprairie"

def concat_keys_values(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += str(key) + str(value)
    return result

print(concat_keys_values(je="suis", un="kwarg"))