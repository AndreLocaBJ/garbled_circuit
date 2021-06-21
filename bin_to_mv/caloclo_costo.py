from genericpath import exists
from os import listdir
from os import remove
from os.path import exists
from posixpath import basename

def get_circuit_info(file):
    input_var = []
    domain = None
    tables_array = []
    with open(file, 'r') as f:
        for line in f.readlines():
            if '.inputs' in line:
                input_var = line.strip().split(' ')[1:]
            elif '.mv' in line:
                domain = line.strip().split(' ')[-1]
            if '.table' in line:
                tables_array.append({
                    'input':    line.strip().split(' ')[1:-1],
                    'output':   line.strip().split(' ')[-1]
                })
    if domain == None: domain = 2
    return {
        'input_var':    input_var,
        'domain':       int(domain),
        'tables':       tables_array
    }

def circuit_cost(circ):
    cost = 0
    for table in circ['tables']:
        intersection = len(set(circ['input_var']).intersection(table['input']))
        cost += pow(circ['domain'], intersection)
    return cost


if __name__ == "__main__":

    wd = 'facili/blfmv/synth/'

    if exists('./calcolo_costi.csv'):
        remove('./calcolo_costi.csv')

    with open('calcolo_costi.csv', 'a') as final_file:
        final_file.write('NOME CIRC;COSTO BOOLEANO;INPUT ALICE;INPUT BOB;DOMINIO MULTIVALORE;COSTO MULTIVALORE;INPUT ALICE;INPUT BOB\n')
        for ele in listdir(wd):
            cir_mv = get_circuit_info(wd+'/'+ele)
            cost_mv = circuit_cost(cir_mv)
            alice_var_mv = None
            bob_var_mv = None
            if len(cir_mv['input_var']) % 2 != 0:
                alice_var_mv = int(len(cir_mv['input_var']) / 2)
                bob_var_mv = int(len(cir_mv['input_var']) / 2) + 1
            else:
                alice_var_mv = int(len(cir_mv['input_var']) / 2)
                bob_var_mv = int(len(cir_mv['input_var']) / 2)

            cir_bool = get_circuit_info('./facili/blif/synth/'+ele.split('.')[0]+'.blif')
            cost_bool = circuit_cost(cir_bool)
            alice_var_bool = None
            bob_var_bool = None
            if len(cir_bool['input_var']) % 2 != 0:
                alice_var_bool = int(len(cir_mv['input_var']) / 2)
                bob_var_bool = int(len(cir_mv['input_var']) / 2) + 1
            else:
                alice_var_bool = int(len(cir_mv['input_var']) / 2)
                bob_var_bool = int(len(cir_mv['input_var']) / 2)

            final_file.write('{};{};{};{};{};{};{};{}\n'.format(ele.split('.')[0], cost_bool, alice_var_bool, bob_var_bool, cir_mv['domain'], cost_mv, alice_var_mv, bob_var_mv))
                ### multi-valore
                #final_file.write('## {}\n'.format(ele.split('.')[0]))
                #final_file.write('- Multi-valore, dominio {}:\n'.format(cir_mv['domain']))
                #final_file.write('\tInput Alice: {}\n'.format(alice_var_mv))
                #final_file.write('\tInput Bob: {}\n'.format(bob_var_mv))
                #final_file.write('\tCosto circuito: {}\n'.format(cost_mv))
                ## booleano
                #final_file.write('- Boleano, dominio {}:\n'.format(cir_bool['domain']))
                #final_file.write('\tInput Alice: {}\n'.format(alice_var_bool))
                #final_file.write('\tInput Bob: {}\n'.format(bob_var_bool))
                #final_file.write('\tCosto circuito: {}\n\n'.format(cost_bool))

