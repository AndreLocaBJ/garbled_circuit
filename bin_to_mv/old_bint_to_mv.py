if __name__ == '__main__':
    inp = None
    out = None
    inp_array = []
    out_array = []
    truth_array = []

    with open('bin_to_mv/base.pla', 'r') as input_file:
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
                truth_array.append(line)

    mv = input('Scegli il dominio multi-valore: ')
    # Ogni qunati bit devo dividere la tabella di verita'
    dv = len("{0:b}".format(int(mv)))
    print('Divido ogni {} bit\nInizio la conversione'.format(dv))

    conv_truth = []
    for line in truth_array:
        line['inp'] = [line['inp'][i * dv:(i + 1) * dv] for i in range((len(line['inp']) + dv - 1) // dv )]
        if '-' not in line['out']:
            line['out'] = [line['out'][i * dv:(i + 1) * dv] for i in range((len(line['out']) + dv - 1) // dv )]
            l_supp_inp = []
            l_supp_out = []
            for val in line['inp']:
                l_supp_inp.append(int(val,2))
            for val in line['out']:
                l_supp_out.append(int(val,2))
            conv_truth.append({
                'inp':  l_supp_inp,
                'out':  l_supp_out
            })
    
    print('Tabella binaria iniziale')
    for line in truth_array:
        print(line)
    print('Tabella converita')
    for line in conv_truth:
        print(line)
    print('Creo il file blif_mv')
    
    mv_inputs = list(map(str, input('Scegli il nome delle {} variabili di input: '.format(len(conv_truth[0]['inp']))).split()))
    mv_outputs = list(map(str, input('Scegli il nome delle {} variabili di input: '.format(len(conv_truth[0]['out']))).split()))
    with open('conv.blfmv', 'w') as blif:
        blif.write('.inputs {}\n'.format(' '.join(map(str, mv_inputs))))
        blif.write('.outputs {}\n'.format(' '.join(map(str, mv_outputs))))
        blif.write('.mv {} {}\n'.format(', '.join(map(str, mv_inputs)), mv))
        blif.write('.mv {} {}\n'.format(', '.join(map(str, mv_outputs)), mv))
        blif.write('.table {} -> {}\n'.format(', '.join(map(str, mv_inputs)), ', '.join(map(str, mv_outputs))))
        for line in conv_truth:
            blif.write('{} {}\n'.format(' '.join(map(str, line['inp'])), ' '.join(map(str, line['out']))))
        blif.write('.end\n')

