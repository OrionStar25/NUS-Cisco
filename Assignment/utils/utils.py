import json
import csv
import pickle


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


def convert_to_csv(data, name, headers):
    with open(name,'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(headers)
        
        for row in data:
            csv_out.writerow(row)


def create_edge_list(data):
    edges = []

    for cat, prods in data.items():
        if type(prods) == list:
            for prod in prods:
                e = (cat, prod)
                edges.append(e)
        else:
            for sub_cat, sub_prods in prods.items():
                for sub_prod in sub_prods:
                    e = (sub_cat, sub_prod)
                    edges.append(e)
                
                e = (cat, sub_cat)
                edges.append(e)

    return edges


def get_products(data):
    products = []

    for prods in data.values():
        if type(prods) == list:
            for prod in prods:
                products.append(prod)
        else:
            for sub_prods in prods.values():
                for sub_prod in sub_prods:
                    products.append(sub_prod)

    return products


def write_list_to_file(filename, data):
    with open(filename, 'w') as f:
        for row in data:
            f.write(f'{row}\n')


def write_text_to_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()

def load_pickle(filename):
    with open(filename, 'rb') as file: 
        # Call load method to deserialze 
        pkl = pickle.load(file) 
    
    return pkl
