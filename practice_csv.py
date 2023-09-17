import csv
from collections import Counter

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader =csv.reader(csv_file, delimiter=',')
        head=next(reader)
        data=[]
        for row in reader:
            itera= zip(head, row)
            dicc = {key: value for key, value in itera}
            data.append(dicc)
        return data

def data_to_charts(country, path):
    data=read_csv(path)
    for row in data:
        if country in row.values():
            diccad={
                clave: int(valor) for clave, valor in row.items() if '20' in clave or '19' in clave }
            print(diccad)
            labels=list(diccad.keys())
            values=list(diccad.values())
            # labels.pop(-1)
            # values.pop(-1)
            labels.reverse()
            values.reverse()
    return labels, values

def world_populations(path):
    data=read_csv(path)
    val=[]
    for row in data:
        world=[float(valor) for clave, valor  in row.items() if 'World' in clave]
        val.append(world[0])
    freclist=Counter(val)
    returnlist={clave: (frec / (len(val)) * 100 ) for clave, frec in freclist.items() }   
    print(returnlist)  
    return returnlist

if __name__ == '__main__':
    # datos=read_csv('./world.csv')
    # print(datos[2])

    #lab, val=data_to_charts('Algeria','./world.csv')
    #print(str(val), str(lab))
    world_populations('./world.csv')


