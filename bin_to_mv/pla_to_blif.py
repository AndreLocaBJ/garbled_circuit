import os

if __name__ == "__main__":
    working_dir='./facili/starter'

    for ele in os.listdir(working_dir):
        with open('./pla_to_bin', 'a') as file:
            file.write('read_pla {}/{}\n'.format(working_dir,ele))
            file.write('write_blif_mv ./facili/blif/{}.blif\n\n'.format(ele.split('.')[0]))