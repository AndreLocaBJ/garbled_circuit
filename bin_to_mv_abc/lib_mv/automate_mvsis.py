import os

def synth(working_dir):  
    with open('./synth.mvsis', 'w') as file:
        for ele in os.listdir('{}/blif'.format(working_dir)):
            if ele.endswith('.blif'):
                file.write('read_blif {}/blif/{}\n'.format(working_dir,ele))
                file.write('\n')
                file.write('write_blif {}/blif/synth/{}.blif\n\n'.format(working_dir, ele.split('.')[0]))

                file.write('read_blif_mv {}/blfmv/{}.mv\n'.format(working_dir, ele.split('.')[0]))
                file.write('write_blif_mv {}/blfmv/synth/{}.mv\n\n'.format(working_dir, ele.split('.')[0]))

def pla_to_blif(working_dir):
    for ele in os.listdir('{}/pla'.format(working_dir)):
        with open('./pla_to_blif.mvsis', 'a') as file:
            file.write('read_pla {}/pla/{}\n'.format(working_dir,ele))
            file.write('write_blif {}/blif/{}.blif\n\n'.format(working_dir, ele.split('.')[0]))