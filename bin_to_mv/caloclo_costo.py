from glob import glob
from os.path import basename as bn

def definizione_variabile(varList):
    var_array = []
    for index in range(1, len(varList) - 1):
        var = {
            'name': varList[index],
            'dom': int(varList[len(varList) - 1])
        }
        var_array.append(var)
    return var_array


def definizione_tabella(table_line):
    table = None
    if '->' in table_line:
        for i in range(1, len(table_line)):
            if table_line[i] == '->':
                table = {
                    'input':    table_line[1:i],
                    'output':   table_line[i + 1:len(table_line)]
                }
                break
    else:
        table = {
            'input':    table_line[1:len(table_line) - 1],
            'output':   [table_line[len(table_line) - 1]]
        }
    return table

def clacolo_costo_blfmv(blfmv):
    circuit_array = []
    name_circuit = None

    var_array = []
    table_array = None
    input_array = []
    output_array = []
    line_array = []

    with open(blfmv, 'r') as f:
        for line in f.readlines():
            if ".inputs" in line:
                input_array = line.strip().split(" ")[1:]
            elif ".outputs" in line:
                output_array = line.strip().split(" ")[1:]
            elif ".table" in line:
                if line_array != []:
                    circuito = {
                        'input':        table_array['input'],
                        'output':       table_array['output'],
                        'truth_table':  line_array
                    }
                    circuit_array.append(circuito)
                    line_array = []
                    table_array = None
                table_line = line.strip().split(" ")
                table_array = definizione_tabella(table_line)
            elif ".mv" in line:
                mvline = line.replace(",", "").strip().split(" ")
                var_array += definizione_variabile(mvline)
            elif '.model' in line:
                name_circuit = line.strip().replace(".model ", "")
            elif '.end' in line:
                circuito = {
                        'input':        table_array['input'],
                        'output':       table_array['output'],
                        'truth_table':  line_array
                    }
                circuit_array.append(circuito)
            elif '.default_input_arrival' in line:
                continue
            elif '.spec' in line:
                continue
            else:
                line_array.append(line.strip().split())

    if var_array == []:
        for inp in input_array:
            var = {
                'name': inp,
                'dom': 2
            }
            var_array.append(var)
        for out in output_array:
            var = {
                'name': out,
                'dom': 2
            }
            var_array.append(var)
    
    costo = 0
    n_inp = 0

    #print('Riassunto del circuito')
    #print('Il circuito ha {} input: {}'.format(len(input_array), ' '.join(map(str, input_array))))
    for circ in circuit_array:
        dom_var = 0
        for inp in circ['input']:
            for var in var_array:
                if inp == var['name']:
                    if dom_var < var['dom']:
                        n_inp +=1
                        dom_var = var['dom']
        costo += pow(dom_var, len(circ['input']))
    #print('Questi valori sono presenti in {} circuiti'.format(n_inp))
    #print('Il costo totale dei circuiti inviati è {}'.format(costo))
    return costo, len(circ['input']), dom_var

def calcolo_costo_pla(pla):
    with open(pla) as pla_circ:
        for line in pla_circ.readlines():
            if '.i' in line and line[2] == ' ':
                inp = line.split(' ')[1]    
    return pow(2, int(inp)), int(inp)

if __name__ == "__main__":
    for blfmv in glob('./facili/blfmv/*.blfmv'):
        c_blfmv, n_inp_blfmv, dom = clacolo_costo_blfmv(blfmv)
        c_pla, n_inp_pla= calcolo_costo_pla('./facili/starter/{}.pla'.format(bn(blfmv).split('.')[0]))
        with open('./calcolo_costi', 'a') as file:
            file.write('## {} ##\n'.format(bn(blfmv).split('.')[0]))
            file.write('- booleano:\n\t-Dimensione del circuito: {}\n\t-Costo variabili Alice: {}\n\t-Costo variabili Bob: {}\n\n'.format(c_pla, int(n_inp_pla)//2, int(n_inp_pla)//2))
            file.write('- multivalore:\n\t-Dimensione del circuito: {}\n\t-Costo variabili Alice: {}\n\t-Costo variabili Bob: {}\n'.format(c_blfmv, int(n_inp_blfmv)//2, int(n_inp_blfmv)//2))
            file.write('\n')