from os import remove, listdir, makedirs, path
from lib_mv.bin_to_mv import bin_to_mv, bin_to_mv_4, bin_to_mv_mcd
from lib_mv.automate_mvsis import synth,pla_to_blif
from lib_mv.caloclo_costo import calcolo_costi_no_synth, calcolo_costi_synth
from os.path import exists
from subprocess import call
from shutil import rmtree

if __name__ == '__main__':

    working_dir = './prova'
    
    if path.exists('{}/blif'.format(working_dir)) and path.exists('{}/blfmv'.format(working_dir)):
        rmtree('{}/blif'.format(working_dir))
        rmtree('{}/blfmv'.format(working_dir))
      
    makedirs('{}/blif/synth'.format(working_dir))
    makedirs('{}/blfmv/synth'.format(working_dir))
    makedirs('{}/blfmv/synth/abc'.format(working_dir))
    makedirs('{}/blfmv/synth/mvsis'.format(working_dir))
    
    if path.exists('{}/synth_out.mvsis'.format(working_dir)):
        remove('{}/synth_out.mvsis'.format(working_dir))
    
    if not path.exists('{}/pla'.format(working_dir)):
        print('CARTELLA PLA NON PRESENTE')
        exit
    
    #mv = input('Scegli il dominio multi-valore: ')
    ## Ogni qunati bit devo dividere la tabella di verita'
    #dv = len("{0:b}".format(int(mv)-1))
    #print('Divido ogni {} bit\nInizio la conversione'.format(dv))
    #bin_to_mv(working_dir,dv,mv)

    #bin_to_mv_mcd(working_dir)
    bin_to_mv_4(working_dir)

    if exists('./pla_to_blif.mvsis'):
        remove('./pla_to_blif.mvsis')
    pla_to_blif(working_dir)

    call(['abc', '-F', './pla_to_blif.mvsis'])

    synth(working_dir)

    call(['abc', '-F', './synth_bool.abc'])
    call(['abc', '-F', './synth_mv.abc'])
    call(['mvsis', '-F', './synth_mv.mvsis'])

    if exists('./calcolo_costi_abc.csv'):
        remove('./calcolo_costi_abc.csv')
    if exists('./calcolo_costi_mvsis.csv'):
        remove('./calcolo_costi_mvsis.csv')
    if exists('./calcolo_costi_no_synth_abc.csv'):
        remove('./calcolo_costi_no_synth_abc.csv')
    if exists('./calcolo_costi_no_synth_mvsis.csv'):
        remove('./calcolo_costi_no_synth_mvsis.csv')

    calcolo_costi_synth(working_dir, 'abc')
    calcolo_costi_no_synth(working_dir, 'abc')
    calcolo_costi_synth(working_dir, 'mvsis')
    calcolo_costi_no_synth(working_dir, 'mvsis')