from os import path, listdir
from os.path import basename


def create_0_1_array(le, pad):
    count_1 = pad
    count_0 = pad
    return [str(1) if i % (count_1 + count_0) < count_1 else str(0) for i in range(le)]


def resolve_dont_care(line, in_out):
    # Conto qunati - e creo 2^n nuove linee
    n_dc = pow(2, line[in_out].count('-'))

    input_entry = line[in_out]
    new_array = []

    for h in range(line[in_out].count('-')):
        val_array = create_0_1_array(n_dc, pow(2, h))
        # Prima iterazione --> creo l'array per le prossime iterazioni
        if h == 0:
            for i in range(n_dc):
                it = 0
                new_line = []
                # percorro l'array al rovescio per prendere prima la - meno significativa
                for j in range(len(input_entry)-1, -1, -1):
                    if input_entry[j] == '-' and it == 0:
                        new_line.append(val_array[(len(val_array)-1) - i])
                        it += 1
                    else:
                        new_line.append(line[in_out][j])
                new_array.append(new_line[::-1])
        # tutte le altre
        else:
            it = 0  # serve per fare in modo che sostituisca una - per ogni iterazione
            for c, l in enumerate(new_array):
                # percorro l'array al rovescio per prendere prima la - meno significativa
                for j in range(len(l)-1, -1, -1):
                    if l[j] == '-' and it == 0:
                        l[j] = val_array[(len(val_array)-1) - c]
                        it += 1
                it = 0

    if in_out == 'inp':
        return [{'inp':  l, 'out':  line['out']} for l in new_array]
    else:
        return [{'inp':  line['inp'], 'out':  l} for l in new_array]


def create_mv_truth_table(truth_array, dv):
    conv_truth = []
    for line in truth_array:
        line['inp'] = ''.join(line['inp'])
        line['inp'] = [line['inp'][i * dv:(i + 1) * dv]
                       for i in range((len(line['inp']) + dv - 1) // dv)]
        if '-' not in line['out']:
            line['out'] = ''.join(line['out'])
            line['out'] = [line['out'][i * dv:(i + 1) * dv]
                           for i in range((len(line['out']) + dv - 1) // dv)]
            l_supp_inp = []
            l_supp_out = []
            for val in line['inp']:
                if '-' not in val:
                    l_supp_inp.append(int(val, 2))
                else:
                    l_supp_inp.append('-')
            for val in line['out']:
                l_supp_out.append(int(val, 2))
            conv_truth.append({
                'inp':  l_supp_inp,
                'out':  l_supp_out
            })
    return conv_truth


def expand_dont_care(truth_table, dv):
    n_dont_care = ''

    for i in range(dv):
        n_dont_care += '-'

    # Espansione dei don't care
    # ESPANSIONE DEGLI INPUT
    len_truth_table = len(truth_table)
    i = 0
    while i < len_truth_table:
        if '-' in truth_table[i]['inp']:
            truth_table[i]['inp'] = ''.join(truth_table[i]['inp'])
            truth_table[i]['inp'] = [truth_table[i]['inp'][a:a+dv]
                                     for a in range(0, len(truth_table[i]['inp']), dv)]

            for a in range(len(truth_table[i]['inp'])):
                if truth_table[i]['inp'][a] == n_dont_care:
                    truth_table[i]['inp'][a] = 'k'*len(n_dont_care)
            truth_table[i]['inp'] = ''.join(truth_table[i]['inp'])
            new_lines = resolve_dont_care(truth_table[i], 'inp')
            truth_table = truth_table[:i] + new_lines + truth_table[i+1:]
            len_truth_table = len(truth_table)
        i += 1

    # ESPANSIONE DEGLI OUTPUT
    len_truth_table = len(truth_table)
    i = 0
    while i < len_truth_table:
        if '-' in truth_table[i]['out']:
            truth_table[i]['out'] = ''.join(truth_table[i]['out'])
            truth_table[i]['out'] = [truth_table[i]['out'][a:a+dv]
                                     for a in range(0, len(truth_table[i]['out']), dv)]

            for a in range(len(truth_table[i]['out'])):
                # metto un valore a caso dove il numero di - e' uguale a quello per avere un don't care cosi' non fa la sostituzione
                if truth_table[i]['out'][a] == n_dont_care:
                    truth_table[i]['out'][a] = 'k'*len(n_dont_care)
            truth_table[i]['out'] = ''.join(truth_table[i]['out'])
            new_lines = resolve_dont_care(truth_table[i], 'out')
            truth_table = truth_table[:i] + new_lines + truth_table[i+1:]
            len_truth_table = len(truth_table)
        i += 1

    for l in range(len(truth_table)):
        nl_i = ''.join(truth_table[l]['inp'])
        nl_o = ''.join(truth_table[l]['out'])
        truth_table[l]['inp'] = nl_i.replace('k'*len(n_dont_care), n_dont_care)
        truth_table[l]['out'] = nl_o.replace('k'*len(n_dont_care), n_dont_care)

    return truth_table


def crete_blif_mv(working_dir, mv_table, mv, nomefile):
    import string
    # string.ascii_lowercase -> tutte le lettere da a a z in minuscolo
    mv_input = [i for i in list(string.ascii_lowercase)[
        :len(mv_table[0]['inp'])]]
    mv_output = ['o{}'.format(i) for i in range(len(mv_table[0]['out']))]

    # Se devo dare nomi custom
    #mv_inputs = list(map(str, input('Scegli il nome delle {} variabili di input: '.format(len(mv_table[0]['inp']))).split()))
    #mv_outputs = list(map(str, input('Scegli il nome delle {} variabili di output: '.format(len(mv_table[0]['out']))).split()))

    with open('{}/blfmv/{}.mv'.format(working_dir, nomefile), 'w') as blif:
        blif.write('.model {}\n'.format(working_dir, nomefile))
        blif.write('.inputs {}\n'.format(' '.join(map(str, mv_input))))
        blif.write('.outputs {}\n'.format(' '.join(map(str, mv_output))))
        blif.write('.mv {} {}\n'.format(', '.join(map(str, mv_input)), mv))
        blif.write('.mv {} {}\n'.format(', '.join(map(str, mv_output)), mv))
        for count, out in enumerate(mv_output):
            blif.write('.table {} {}\n'.format(' '.join(map(str,
                                                            mv_input)), out))
            #blif.write('.default 0 0\n')
            for line in mv_table:
                blif.write('{} {}\n'.format(
                    ' '.join(map(str, line['inp'])), line['out'][count]))
        blif.write('.end\n')


def read_pla(path_file):
    inp = None
    out = None
    inp_array = []
    out_array = []
    truth_table = []
    with open(path_file, 'r') as input_file:
        for line in input_file.readlines():
            if '.i' in line and line[2] == ' ':
                inp = line.split(' ')[1]
            elif '.o' in line and line[2] == ' ':
                out = line.split(' ')[1]
            elif '.ilb' in line:
                inp_array = line.strip().split(' ')[1:]
            elif '.ob' in line:
                out_array = line.strip().split(' ')[1:]
            elif '.end' in line:
                continue
            else:
                line = {
                    'inp':  line.strip().split(' ')[0],
                    'out':  line.strip().split(' ')[1]
                }
                truth_table.append(line)
    return inp, out, inp_array, out_array, truth_table


def create_pla_expanded(working_dir, inp, out, inp_array, out_array, truth_table, name_file):
    with open('{}/ext_pla/{}_ext.pla'.format(working_dir, name_file), 'w') as pla:
        pla.write('.i {}'.format(inp))
        pla.write('.o {}'.format(out))
        pla.write('.ilb {}\n'.format(' '.join(map(str, inp_array))))
        pla.write('.ob {}\n'.format(' '.join(map(str, out_array))))
        for line in truth_table:
            pla.write('{} {}\n'.format(
                ''.join(map(str, line['inp'])), ''.join(map(str, line['out']))))
        pla.write('.end\n')


def bin_to_mv(working_dir, dv, mv):
    for pla in listdir('{}/pla'.format(working_dir)):
        if pla.endswith('.pla'):
            inp, out, inp_array, out_array, truth_table = read_pla(
                '{}/pla/{}'.format(working_dir, pla))
            truth_table = expand_dont_care(truth_table, dv)
            mv_table = create_mv_truth_table(truth_table, dv)
            #create_pla_expanded(inp, out,inp_array, out_array, truth_table, bn(pla).split('.')[0])
            crete_blif_mv(working_dir, mv_table, mv,
                          basename(pla).split('.')[0])


def euclide(a, b):
    while(b != 0):
        R = a % b
        a = b
        b = R
    return a


def expand_all_dont_care(truth_table, dv):
    # Espansione dei don't care
    # ESPANSIONE DEGLI INPUT
    len_truth_table = len(truth_table)
    i = 0
    while i < len_truth_table:
        if '-' in truth_table[i]['inp']:
            truth_table[i]['inp'] = ''.join(truth_table[i]['inp'])
            truth_table[i]['inp'] = [truth_table[i]['inp'][a:a+dv]
                                     for a in range(0, len(truth_table[i]['inp']), dv)]

            truth_table[i]['inp'] = ''.join(truth_table[i]['inp'])
            new_lines = resolve_dont_care(truth_table[i], 'inp')
            truth_table = truth_table[:i] + new_lines + truth_table[i+1:]
            len_truth_table = len(truth_table)
        i += 1

    # ESPANSIONE DEGLI OUTPUT
    len_truth_table = len(truth_table)
    i = 0
    while i < len_truth_table:
        if '-' in truth_table[i]['out']:
            truth_table[i]['out'] = ''.join(truth_table[i]['out'])
            truth_table[i]['out'] = [truth_table[i]['out'][a:a+dv]
                                     for a in range(0, len(truth_table[i]['out']), dv)]

            truth_table[i]['out'] = ''.join(truth_table[i]['out'])
            new_lines = resolve_dont_care(truth_table[i], 'out')
            truth_table = truth_table[:i] + new_lines + truth_table[i+1:]
            len_truth_table = len(truth_table)
        i += 1

    for l in range(len(truth_table)):
        nl_i = ''.join(truth_table[l]['inp'])
        nl_o = ''.join(truth_table[l]['out'])

    return truth_table


def bin_to_mv_mcd(working_dir):
    for pla in listdir('{}/pla'.format(working_dir)):
        if pla.endswith('.pla'):
            inp, out, inp_array, out_array, truth_table = read_pla(
                '{}/pla/{}'.format(working_dir, pla))
            # qui trovo l'mdc, ogni quanti bit devo dividere il circuito
            dv = euclide(int(inp), int(out))
            if int(inp.strip()) == int(out.strip()) or dv == int(inp):
                dv = dv/2
                # mv indica il massimo numeor che posso rappresentare con quei bit, ovvero il dominio del multivalore
            if dv >= 8:
                dv = 2 
            mv = pow(2, dv)
            print('{}\ninp: {}\nout:{}\nmulti-valore:{}\ndivide ogni:{}\n'.format(pla,
                  inp.strip(), out.strip(), int(mv), int(dv)))
            truth_table = expand_dont_care(truth_table, int(dv))
            mv_table = create_mv_truth_table(truth_table, int(dv))
            #create_pla_expanded(inp, out,inp_array, out_array, truth_table, bn(pla).split('.')[0])
            crete_blif_mv(working_dir, mv_table, int(mv),
                          basename(pla).split('.')[0])


def bin_to_mv_4(working_dir):
    for pla in listdir('{}/pla'.format(working_dir)):
        if pla.endswith('.pla'):
            inp, out, inp_array, out_array, truth_table = read_pla(
                '{}/pla/{}'.format(working_dir, pla))
            mv = 4
            dv = 2
            print('{}\ninp: {}\nout:{}\nmulti-valore:{}\ndivide ogni:{}\n'.format(pla,
                  inp.strip(), out.strip(), int(mv), int(dv)))
            truth_table = expand_dont_care(truth_table, int(dv))
            mv_table = create_mv_truth_table(truth_table, int(dv))
            #create_pla_expanded(inp, out,inp_array, out_array, truth_table, bn(pla).split('.')[0])
            crete_blif_mv(working_dir, mv_table, int(mv),
                          basename(pla).split('.')[0])