import json 


# Dump dictionary into a json file
def write_to_json(filename, dictionary):
    with open(filename, "w") as outfile: 
        json.dump(dictionary, outfile)


def preprocess_data(old_map):
    NAME = 'category'
    PRODUCTS = 'products'
    VALUE = 'value'
    new_map = {
        NAME: 'Cisco Products',
        PRODUCTS: []
    }

    for k, v in old_map.items():
        child = {NAME: k, PRODUCTS: []}

        if type(v) == list:
            for i, p in enumerate(v):
                obj = {NAME: p, VALUE: i+1}
                child[PRODUCTS].append(obj)
        else:
            for (p, val) in v.items():
                obj = {NAME: p, PRODUCTS: []}
                for sub in val:
                    obj[PRODUCTS].append({NAME: sub, VALUE: 1})
                child[PRODUCTS].append(obj)

        new_map[PRODUCTS].append(child)

    return new_map
