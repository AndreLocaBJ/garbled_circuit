import os

def synth(working_dir):  
    with open('./synth_bool.abc', 'w') as file:
        file.write("source abc_alias.abc\n")
        for ele in os.listdir('{}/blif'.format(working_dir)):
            if ele.endswith('.blif'):
                file.write('read_blif {}/blif/{}\n'.format(working_dir,ele))
                file.write('cl\n')
                file.write('resyn2\n')
                file.write('cl\n')
                file.write('write_blif {}/blif/synth/{}.blif\n\n'.format(working_dir, ele.split('.')[0]))

    with open('./synth_mv.abc', 'w') as file:
        file.write("source abc_alias.abc\n")
        for ele in os.listdir('{}/blfmv'.format(working_dir)):
            if ele.endswith('.mv'):
                file.write('read_blif_mv {}/blfmv/{}\n'.format(working_dir, ele))
                file.write('strash\n')
                file.write('compress2\n')
                file.write('cl\n')
                file.write('resyn2\n')
                file.write('cl\n')
                file.write('write_blif_mv {}/blfmv/synth/abc/{}\n\n'.format(working_dir, ele))
    
    with open('./synth_mv.mvsis', 'w') as file:
        for ele in os.listdir('{}/blfmv'.format(working_dir)):
            if ele.endswith('.mv'):
                file.write('read_blif_mv {}/blfmv/{}\n'.format(working_dir, ele))
                file.write('sweep\n')
                file.write('eliminate -l 1\n')
                file.write('simplify -m nocomp\n')
                file.write('eliminate -l 1\n')
                file.write('sweep\n')
                file.write('eliminate -l 5\n')
                file.write('simplify\n')
                file.write('sweep\n')
                file.write('eliminate -l 1\n')
                file.write('sweep\n')
                file.write('fullsimp -m nocomp\n')
                file.write('write_blif_mv {}/blfmv/synth/mvsis/{}\n\n'.format(working_dir, ele))

def pla_to_blif(working_dir):
    with open('./pla_to_blif.mvsis', 'w') as file:
        file.write("source abc_alias.abc\n")
        for ele in os.listdir('{}/pla'.format(working_dir)):
            file.write('read_pla {}/pla/{}\n'.format(working_dir,ele))
            file.write('write_blif {}/blif/{}.blif\n\n'.format(working_dir, ele.split('.')[0]))