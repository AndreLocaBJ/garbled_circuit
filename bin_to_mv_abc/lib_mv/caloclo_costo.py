from os import listdir


def info_circuito(working_dir, circuito):
    with open('{}/{}'.format(working_dir, circuito)) as circ:
        input = None
        output = None
        mv = int(0)
        table_array = []
        for line in circ.readlines():
            if '.inputs' in line.strip():
                input = line.strip().split(' ')[1:]
            if '.outputs' in line.strip():
                output = line.strip().split(' ')[1:]
            if '.mv' in line.strip():
                if mv < int(line.strip().split(' ')[-1]):
                    mv = int(line.strip().split(' ')[-1])
            if '.table' in line.strip():
                l = line.strip().split(' ')
                table_array.append(
                    {
                        'input':    l[1:len(l)-1],
                        'output':   l[-1]
                    }
                )

        # i blif non hanno .mv, quidi gli do il valore di dominio
        if mv == 0:
            mv = 2

        return {
            'dominio':   mv,
            'input':    input,
            'output':   output,
            'tabelle':  table_array
        }


def calcolo_costo_circuito(circuito):
    costo = 0
    for t in circuito['tabelle']:
        intersection = len(set(circuito['input']).intersection(t['input']))
        costo = costo + pow(circuito['dominio'], intersection)
    return costo


def calcolo_costi(working_dir):
    with open('calcolo_costi.csv', 'a') as file:
        file.write(
            'NOME CIRC;COSTO BOOLEANO;INPUT ALICE;INPUT BOB;DOMINIO MULTIVALORE;COSTO MULTIVALORE;INPUT ALICE;INPUT BOB\n')
        for blfmv in listdir('{}/blfmv/synth'.format(working_dir)):
            if blfmv.endswith('.blifmv'):
                print(blfmv)
                circ_mv = info_circuito(
                    '{}/blfmv/synth'.format(working_dir), blfmv)
                costo_mv = calcolo_costo_circuito(circ_mv)
                if len(circ_mv['input']) % 2 != 0:
                    alice_var_mv = int(len(circ_mv['input']) / 2)
                    bob_var_mv = int(len(circ_mv['input']) / 2) + 1
                else:
                    alice_var_mv = int(len(circ_mv['input']) / 2)
                    bob_var_mv = int(len(circ_mv['input']) / 2)

                circ_bool = info_circuito(
                    '{}/blif/synth'.format(working_dir), '{}.blif'.format(blfmv.split('.')[0]))
                costo_bool = calcolo_costo_circuito(circ_bool)
                if len(circ_bool['input']) % 2 != 0:
                    alice_var_bool = int(len(circ_bool['input']) / 2)
                    bob_var_bool = int(len(circ_bool['input']) / 2) + 1
                else:
                    alice_var_bool = int(len(circ_bool['input']) / 2)
                    bob_var_bool = int(len(circ_bool['input']) / 2)
                file.write('{};{};{};{};{};{};{};{}\n'.format(blfmv.split('.')[
                    0], costo_bool, alice_var_bool, bob_var_bool, circ_mv['dominio'], costo_mv, alice_var_mv, bob_var_mv))
