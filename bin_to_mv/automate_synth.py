import os

if __name__ == "__main__":
    working_dir='./facili/blif'

    if not os.path.exists('./facili/blif/synth') and not os.path.exists('./facili/blfmv/synth'):
        os.makedirs('./facili/blif/synth')
        os.makedirs('./facili/blfmv/synth')
    
    if os.path.exists('./facili/synth/synth_out.mvsis'):
        os.remove('./facili/synth/synth_out.mvsis')

    with open('./synt_out.mvsis', 'w') as file:
        for ele in os.listdir(working_dir):
            if ele.endswith('.blif'):
                file.write('read_blif {}/{}\n'.format(working_dir,ele))
                file.write('collapse2\n')
                file.write('pair_decode\n')
                #file.write('collapse\n')
                file.write('write_blif_mv ./facili/blif/synth/{}.blif\n\n'.format(ele.split('.')[0]))

                file.write('read_blif_mv {}/{}.blfmv\n'.format('./facili/blfmv',ele.split('.')[0]))
                file.write('collapse2\n')
                file.write('pair_decode\n')
                #file.write('collapse\n')
                file.write('write_blif_mv ./facili/blfmv/synth/{}.blifmv\n\n'.format(ele.split('.')[0]))