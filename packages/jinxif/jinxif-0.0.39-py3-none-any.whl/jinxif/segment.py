###
# title: segment.py
#
# language: Python3.7
# date: 2020-06-00
# license: GPL>=v3
# author: Jenny, bue
#
# description:
#   python3 script for cell segmentation
####

from cellpose import models
from jinxif import config
from jinxif import basic
import matplotlib.pyplot as plt
from numba import jit
import numpy as np
import os
import re
import subprocess
from skimage import exposure, io, morphology
from scipy import stats
import sys
import time
import torch

# PIL is backend from skimage io
# against DecompressionBombError: Image size (n pixels) exceeds limit of 178956970 pixels, could be decompression bomb DOS attack.
import PIL
PIL.Image.MAX_IMAGE_PIXELS = None

# development
#import importlib
#importlib.reload()

# global var
s_path_module = os.path.abspath(os.path.dirname(__file__))
s_path_module = re.sub(r'jinxif$','jinxif/', s_path_module)


# functions

###################
# numba functions #
###################

@jit(nopython=True, parallel=True)
def _relabel_numba(ai_cell_labels, ai_cellid_relabel, o_dtype=np.uint32):
    '''
    version: 2021-08-03

    input:
        ai_cell_labels: (n,) one dimensional numpy array with cell labels.
        ai_cellid_relabel: (n,2) dimensonal numpy array which maps original cell_id to nuc_id.
        o_dtype: data type inside the image array. stanadrd us np.uint32,
            because 32bit tiffs can be opened with most tiff compatibel softwares.

    output:
        ai_cell_relabeld: (n,) one dimensional numpy array with cell labels that match the nucleus.

    description:
        use numba to quickly iterate over each label and replace pixels with new pixel values.
    '''
    # handle input
    ai_cell_labels = ai_cell_labels.astype(o_dtype)
    ai_cellid_relabel = ai_cellid_relabel.astype(o_dtype)

    # do matching
    ai_cell_relabeld = ai_cell_labels.copy()
    for i_cellid_cell, i_cellid_nuc in ai_cellid_relabel:
        ai_cell_relabeld[ai_cell_labels == i_cellid_cell] = i_cellid_nuc

    # output
    return(ai_cell_relabeld)


# BUE 20210703: this numba function actually slows down speed!
#@jit(nopython=True, parallel=True)
#def _nuc_detector_numba(ai_nuc_labels, ai_cell_labels, i_cellid):
    '''
    version: 2021-07-03

    input:
        ai_nuc_labels: (n,) one dimensional numpy array with nucleus labels.
        ai_cell_labels: (n,) one dimensional numpy array with cell labels.
        i_cellid: integer to specify cellid for wech to detect the overlaping nucleus ids.

    output:
        ai_nuc: (n,) list like one dimensional numpy array with all possible nucleus ids.
        ai_nuc_unique: (n,) set like one dimensional numpy array with all possible nucleus ids.

    description:
        numba based function to quickly detect all nucleus ids related to the cellid specified with i_cellid.
    '''
    # find all non-zero nuclei label contained within that cell mask
#    ai_nuc = ai_nuc_labels[ai_cell_labels == i_cellid]
#    ai_nuc = ai_nuc[ai_nuc != 0]
#    ai_nuc_unique = np.unique(ai_nuc)

    # output
#    return(ai_nuc, ai_nuc_unique)


###########
# match #
##########

def _cell_to_nuc(ai_nuc_labels, ai_cell_labels):
    '''
    version: 2021-07-03

    input:
        ai_nuc_labels: (n,) one dimensional numpy array with nucleus labels.
        ai_cell_labels: (n,) one dimensional numpy array with cell labels.

    output:
        ai_cellid_relabel: (n,2) dimensonal numpy array which maps original cell_id to nuc_id.

    description:
        associate the largest nucleaus contained in each cell segmentation.
    '''
    # get cell dominant nuclei label reationship
    lli_cellid_relabel = []  # numba can't handle dictionary

    # iterate over each cell label
    for i_cellid in np.unique(ai_cell_labels):
        if i_cellid == 0:
            continue

        # find all non-zero nuclei label contained within that cell mask
        #ai_nuc, ai_nuc_unique = _nuc_detector_numba(
        #    ai_nuc_labels = ai_nuc_labels,
        #    ai_cell_labels = ai_cell_labels,
        #    i_cellid = i_cellid,
        #)
        ai_nuc = ai_nuc_labels[ai_cell_labels == i_cellid]
        ai_nuc = ai_nuc[ai_nuc != 0]
        ai_nuc_unique = np.unique(ai_nuc)
        # multiple nuclei, choose largest (most common pixels, i.e. mode)
        if len(ai_nuc_unique) > 1:
            ai_value, ai_count = np.unique(ai_nuc, return_counts=True) # does not work with numba
            i_nucid_mode = ai_value[np.argmax(ai_count)]
            if (i_cellid != i_nucid_mode):
                lli_cellid_relabel.append([i_cellid, i_nucid_mode])
        # one nuclei
        elif len(ai_nuc_unique) == 1:
            i_nucid_one = ai_nuc[0]
            if (i_cellid != i_nucid_one):
                lli_cellid_relabel.append([i_cellid, i_nucid_one])
        # zero nuclei
        else:
            lli_cellid_relabel.append([i_cellid, 0])

    # output
    ai_cellid_relabel = np.array(lli_cellid_relabel) #, dtype=np.int64)
    return(ai_cellid_relabel)


def _make_match_nuccell_labels(
        s_slide_pxscene,
        s_type_data = 'cmif',
        # file system
        s_segpath = 'nop/',
    ):
    '''
    version: 2021-10-12
    check out function match_nuccell_labels.

    description:
        this internal subfunction is only necessay becasue of the galaxy port.
    '''
    # handle input
    if not (s_type_data in {'cmif','codex'}):
        sys.exit('Error @ jinxif.extract.segment.match_nuccell_labels : unknowen s_type_data {s_type_data}.\nknowne are cmif and codex.')

    # for slide_pxscene
    # find nucleus and cell segmentation label files
    b_nuc = False
    b_cell = False
    for s_file in sorted(os.listdir(s_segpath)):
        if s_file.startswith(s_slide_pxscene):
            print(f'check: {s_file} ...')
            o_match_nuc = re.search(config.d_nconv['s_regex_tiff_celllabel_nuc'], s_file)
            o_match_cell = re.search(config.d_nconv['s_regex_tiff_celllabel_cell'], s_file)
            # load nuc file
            if not (o_match_nuc is None):
                print(f'found nuc celllabel file: {s_file}')
                i_nuc_diam = int(o_match_nuc[config.d_nconv['di_regex_tiff_celllabel_nuc']['i_nuc_diam']])
                ai_nuc_labels = io.imread(s_segpath + config.d_nconv['s_format_tiff_celllabel_nuc'].format(s_slide_pxscene, i_nuc_diam))
                b_nuc = True
            # load cell file
            elif not (o_match_cell is None):
                print(f'found cell celllabel file: {s_file}')
                s_seg_markers = o_match_cell[config.d_nconv['di_regex_tiff_celllabel_cell']['s_seg_markers']]
                i_cell_diam = int(o_match_cell[config.d_nconv['di_regex_tiff_celllabel_cell']['i_cell_diam']])
                ai_cell_labels = io.imread(s_segpath + config.d_nconv['s_format_tiff_celllabel_cell'].format(s_slide_pxscene, s_seg_markers, i_cell_diam))
                b_cell = True

    # check input
    if not(b_nuc & b_cell):
        sys.exit('Error @ jinxif.extract.segment.match_nuccell_labels : either no nucleus or no cell segmentation label file detected.')

    # start processing
    print(f'Processing matching {s_slide_pxscene}')
    start = time.time()

    # fill small holes
    ai_cell_labels = morphology.closing(ai_cell_labels)

    # remove small objects
    # bue 20210624: originally only cmif not codex, though think it want hurt.
    ai_cell_labels = morphology.remove_small_objects(ai_cell_labels, min_size=int(np.pi*(i_cell_diam/5)**2), connectivity=1, in_place=False)

    # ravel
    ti_nuc_shape = ai_nuc_labels.shape
    ai_nuc_labels = ai_nuc_labels.ravel()
    ti_cell_shape = ai_cell_labels.shape
    ai_cell_labels = ai_cell_labels.ravel()

    # match cellid with nucleiid
    print('get _cell_to_nuc_ listing ...')
    ai_cellid_relabel = _cell_to_nuc(ai_nuc_labels=ai_nuc_labels, ai_cell_labels=ai_cell_labels)

    # set minimalistic variable type
    print('running numba to relabel cell lables ...')
    if (ai_cellid_relabel.max() < 2**8):
        o_dtype = np.uint8
    elif (ai_cellid_relabel.max() < 2**16):
        o_dtype = np.uint16
    elif (ai_cellid_relabel.max() < 2**32):
        o_dtype = np.uint32
    else:
        # bue 20210810: curretly this will never happen. cellpose hardcoded the mask dtype to uint32.
        # this limits cell indexing to: 2**32 -1 = 4'294'967'295 [cell].
        o_dtype = np.uint64
    # numba re-label cellid
    ai_cell_relabeled = _relabel_numba(ai_cell_labels=ai_cell_labels, ai_cellid_relabel=ai_cellid_relabel, o_dtype=o_dtype)

    # unravel
    ai_nuc_labels.shape = ti_nuc_shape
    ai_cell_relabeled.shape = ti_cell_shape

    # data type specific case of
    if (s_type_data == 'cmif'):
        # cmif - no operation
        pass
    elif (s_type_data == 'codex'):
        # codex - set background to zero
        ai_mode = stats.mode(ai_cell_relabeled, axis=0)[0][0][0]
        ai_cell_relabeled[ai_cell_relabeled == ai_mode] = 0

    # finish processing
    end = time.time()
    print(f'time ellapse: {end - start}[sec]')
    print('Done Matching Cells and Nuclei!')

    # get output path
    os.makedirs(s_segpath, exist_ok=True)

    # save result
    s_ofile = config.d_nconv['s_format_tiff_celllabel_nuccellmatched'].format(s_slide_pxscene, s_seg_markers, i_nuc_diam, i_cell_diam)
    print(f'save: {s_ofile}')
    io.imsave(s_segpath + s_ofile, ai_cell_relabeled)


def match_nuccell_labels(
        s_slide_pxscene,
        s_type_data = 'cmif',
        # file system
        s_segdir = config.d_nconv['s_segdir'],  #'./Segmentation/',
        s_format_segdir_cellpose = config.d_nconv['s_format_segdir_cellpose'],  #'{}{}_CellposeSegmentation/', # s_segdir, s_slide
    ):
    '''
    version: 2021-08-03

    input:
        s_slide_pxscene: side_scene to be processed.
        s_type_data: this is for data type specific processsing. implemented is cmif and codex. default is cmif.
        s_segdir: segmentation directory
        s_format_segdir_cellpose: segmentation folder subdirectory where for each slide the cellpose segmentation results are stored.

    output:
        cell basins file, specified by s_format_tiff_celllabel_nuccellmatched.

    description:
        code to load original cell and nucleus label files,
        match cell labels to nuclesu labels, and save an updated cell label file.
    '''
    # handle input 
    s_slide = s_slide_pxscene.split('_')[0]
    s_segpath = s_format_segdir_cellpose.format(s_segdir, s_slide)

    # function call
    _make_match_nuccell_labels(
        s_slide_pxscene = s_slide_pxscene,
        s_type_data = s_type_data,
        # file system
        s_segpath = s_segpath,
    )



################
# segmentation #
################
def cellpose_torch(a_imgscaled, i_diameter, s_model_type, b_gpu=True):
    '''
    version: 2021-05-13

    input:
        a_imgscaled: scalled nucleus dapi or cell zstack image numpy array.
        i_diameter: nucleus or cell diameier in pixel.
        s_model_type: cellpose deep learing model type for cell segmentation. possible values are nuclei and cyto.
        b_gpu: boolean to set gpu processing.

    output:
        a_masks: nucleus or cell segemntation label numpy array.

    description:
        function to run cellpose segmentation.
    '''
    # got gpu?
    if b_gpu and not torch.cuda.is_available():
        sys.exit(f'Error @ segment.cellpose_torch : function called with b_gpu set {b_gpu},\nthough torch.cuda.is_available ({torch.cuda.is_available()}) could not detect any gpu.')

    # run model
    model = models.Cellpose(model_type=s_model_type, gpu=b_gpu, device=None, torch=True)

    if s_model_type == 'nuclei':
        li_channel = [0,0]
        r_flow_threshold = 0.0
        r_cellprob_threshold = 0.0
        i_min_size = int(np.pi * (i_diameter / 10)**2) # could be real

    elif s_model_type == 'cyto':
        li_channel = [2,3]
        r_flow_threshold = 0.6
        r_cellprob_threshold = 0.0
        i_min_size = int(np.pi * (i_diameter / 5)**2) # clould be real

    else:
        sys.exit(f'Error @ segment.cellpose_torch : unknowen s_model_type {s_model_type}.\nknowen are nuclei and cyto.')

    print(f'segment modelling with minimum cell size: {i_min_size}')
    a_masks, flows, styles, diams = model.eval(
        x = a_imgscaled,
        channels = li_channel,
        diameter = i_diameter,  # bue: could be real
        flow_threshold = r_flow_threshold,
        cellprob_threshold = r_cellprob_threshold,
        min_size = i_min_size,
    )

    # output
    return(a_masks)


# single
def _make_segment_nuc_dapi(
        s_slide_pxscene,
        s_tiff_dapi,
        i_nuc_diam,
        # file system
        s_regpath = 'nop/',
        s_segpath = 'nop/',
        # gpu
        b_gpu = True,
    ):
    '''
    version: 2021-10-08
    check out function make_segment_nuc_dapi.

    description:
        this internal subfunction is only necessay becasue of the galaxy port.
    '''
    # for slide_pxscene
    # load and rescale 16[bit] dapi image
    a_dapi = io.imread(s_regpath + s_tiff_dapi)
    a_dapi = exposure.rescale_intensity(a_dapi, in_range=(np.quantile(a_dapi, 0.03), 1.5 * np.quantile(a_dapi, 0.9999)))

    # nucleus cellpose segmentation 16[bit] dapi image
    a_mask = cellpose_torch(a_imgscaled=a_dapi, i_diameter=i_nuc_diam, s_model_type='nuclei', b_gpu=b_gpu)
    if (a_mask.max() < 2**8):
        a_mask = a_mask.astype(np.uint8)
    elif (a_mask.max() < 2**16):
        a_mask = a_mask.astype(np.uint16)
    elif (a_mask.max() < 2**32):
        a_mask = a_mask.astype(np.uint32)
    else:
        a_mask = a_mask.astype(np.uint64)

    # get output path
    os.makedirs(s_segpath, exist_ok=True)

    # save segmentation basin file
    print(f"saving {s_slide_pxscene} nuc basins")
    io.imsave(s_segpath + config.d_nconv['s_format_tiff_celllabel_nuc'].format(s_slide_pxscene, i_nuc_diam), a_mask)

    # save 16[bit] dapi image
    print(f"saving {s_slide_pxscene} nuc projection")
    io.imsave(s_segpath + config.d_nconv['s_format_png_nucprojection'].format(s_slide_pxscene, i_nuc_diam), a_dapi.astype('uint16'))
    #io.imsave(s_segpath + config.d_nconv['s_format_png_nucprojection'].format(s_slide_pxscene, i_nuc_diam), (a_dapi/255).astype('uint8'))


def segment_nuc_dapi(
        s_slide_pxscene,
        s_tiff_dapi,
        i_nuc_diam,
        # file system
        s_regdir = config.d_nconv['s_regdir'],  #'./RegisteredImages/',
        s_format_regdir = config.d_nconv['s_format_regdir'],  #'{}{}/',
        s_segdir = config.d_nconv['s_segdir'],  #'./Segmentation/',  # this is actually updated
        s_format_segdir_cellpose = config.d_nconv['s_format_segdir_cellpose'],  #'{}{}_CellposeSegmentation/', # s_segdir, s_slide
        # gpu
        b_gpu = True,
    ):
    '''
    version: 2021-06-25

    input:
        s_slide_pxscene: side_scene to be processed.
        s_tiff_dapi: dapi image file name.
        i_nuc_diam: nucleus diameter in pixel.
        s_regdir: registrated image directory.
        s_format_regdir: regisered imge subfolder format string.
        s_segdir: segmentation directory.
        s_format_segdir_cellpose: segmentation directory cellpose segmentation format string.
        b_gpu: boolean to set gpu processing.

    output:
        nucleus segmentation label basin file specified by s_format_tiff_celllabel_nuc.
        nucleus z projection file specified s_format_png_nucprojection.

    description:
        load a single dapi image file, scale it, run cellpose segmentation on it,
        and save the resulting nucleus z projection and nucleus label file.
    '''
    # handle input 
    s_regpath = s_format_regdir.format(s_regdir, s_slide_pxscene)
    s_slide = s_slide_pxscene.split('_')[0]
    s_segpath = s_format_segdir_cellpose.format(s_segdir, s_slide)

    # function call
    _make_segment_nuc_dapi(
        s_slide_pxscene = s_slide_pxscene,
        s_tiff_dapi = s_tiff_dapi,
        i_nuc_diam = i_nuc_diam,
        # file system
        s_regpath = s_regpath,
        s_segpath = s_segpath,
        # gpu
        b_gpu = b_gpu,
    )


# stack
def _make_segment_cell_zstack(
        s_slide_pxscene,
        s_tiff_dapi,
        i_cell_diam,
        es_seg_marker,
        es_rare_marker,
        # file system
        s_regpath = 'nop/',
        s_segpath = 'nop/',
        # gpu
        b_gpu = True,
    ):
    '''
    version: 2021-10-08
    check out function make_segment_cell_zstack.

    description:
        this internal subfunction is only necessay becasue of the galaxy port.
    '''
    # for slide_pxscene
    # check es_seg_marker
    if (es_seg_marker is None):
        print('Waring @ jinxif.segment.segment_cell_zstack : es_seg_marker is None. cell segementation skipped.')

    else:
        # load and rescale 16[bit] dapi image
        a_dapi = io.imread(s_regpath + s_tiff_dapi)
        a_dapi = exposure.rescale_intensity(a_dapi, in_range=(np.quantile(a_dapi, 0.03), 1.5 * np.quantile(a_dapi, 0.9999)))

        # load and rescale 16[bit] non dapi images
        df_img = basic.parse_tiff_reg(s_wd=s_regpath)
        df_img = df_img.loc[df_img.marker.isin(es_seg_marker), :]  # filter by segmarker
        df_img.sort_values(['marker','round_order'], inplace=True)  # this definds the z stack layer order!
        ls_z_marker = []
        la_img_scaled = []
        for s_ifile in df_img.index:
            s_z_marker = df_img.loc[s_ifile, 'marker']
            print(f'using {type(s_z_marker)} {s_z_marker} for cell segmentation.')
            a_img = io.imread(df_img.index.name + s_ifile)
            if (s_z_marker in es_rare_marker):
                a_img_scaled = exposure.rescale_intensity(a_img, in_range=(np.quantile(a_img,0.03), 1.5 * np.quantile(a_img, 0.99999)))
            else:
                a_img_scaled = exposure.rescale_intensity(a_img, in_range=(np.quantile(a_img, 0.03), 1.5 * np.quantile(a_img, 0.9999)))
            la_img_scaled.append(a_img_scaled)
            ls_z_marker.append(s_z_marker)
        s_z_label = ".".join(ls_z_marker)

        # generate 16[bit] zstack
        print(f"number of images in cyto z projection are {len(la_img_scaled)}")
        a_mip = np.stack(la_img_scaled).max(axis=0)
        a_zdh = np.dstack((np.zeros(a_mip.shape), a_mip, a_dapi)).astype('uint16')

        # cell cellpose segmentation 16[bit] zstack
        a_mask = cellpose_torch(a_imgscaled=a_zdh, i_diameter=i_cell_diam, s_model_type='cyto', b_gpu=b_gpu)

        # get output path
        os.makedirs(s_segpath, exist_ok=True)

        # save segmentation basin file
        print(f"saving {s_slide_pxscene} {s_z_label} cell basins")
        io.imsave(s_segpath + config.d_nconv['s_format_tiff_celllabel_cell'].format(s_slide_pxscene, s_z_label, i_cell_diam), a_mask)

        # save 8[bit] z stack image
        print(f"saving {s_slide_pxscene} {s_z_label} cyto projection")
        io.imsave(s_segpath + config.d_nconv['s_format_png_cellprojection'].format(s_slide_pxscene, s_z_label, i_cell_diam), (a_zdh/255).astype('uint8'))



def segment_cell_zstack(
        s_slide_pxscene,
        s_tiff_dapi,
        i_cell_diam,
        es_seg_marker,
        es_rare_marker,
        # file system
        s_regdir = config.d_nconv['s_regdir'],  #'./RegisteredImages/',
        s_format_regdir = config.d_nconv['s_format_regdir'],   #'{}{}/', # s_regdir, s_slide_pxscene
        s_segdir = config.d_nconv['s_segdir'],  #'./SubtractedRegisteredImages/',
        s_format_segdir_cellpose = config.d_nconv['s_format_segdir_cellpose'],  #'{}{}_CellposeSegmentation/', # s_segdir, s_slide
        # gpu
        b_gpu = True,
    ):
    '''
    version: 2021-06-25

    input:
        s_slide_pxscene: side_scene to be processed.
        s_tiff_dapi: dapi image file name.
        i_cell_diam: cell diameter in pixel.
        es_seg_marker: set of cytoplasm segmentation markers. no need to specify cellpartition.
        es_rare_marker: set of rare markers. there expression will be slightly enhanced by the scaleing step.
        s_regdir: registrated image directory.
        s_format_regdir: regisered imge subfolder format string.
        s_segdir: segmentation directory.
        s_format_segdir_cellpose: segmentation directory cellpose segmentation format string.
        b_gpu: boolean to set gpu processing.

    output:
        cell segmentation label basin file specified by s_format_tiff_celllabel_cell.
        cell  projection file specified s_format_png_cellprojection.

    description:
        load dapi image cell segemnation files, scale them, generate z stack,
        run cellpose segmentation on z stack,
        and save the resulting cell z projection and cell label file.
    '''
    # handle input 
    s_regpath = s_format_regdir.format(s_regdir, s_slide_pxscene)
    s_slide = s_slide_pxscene.split('_')[0]
    s_segpath = s_format_segdir_cellpose.format(s_segdir, s_slide)

    # function call
    _make_segment_cell_zstack(
        s_slide_pxscene = s_slide_pxscene,
        s_tiff_dapi = s_tiff_dapi,
        i_cell_diam = i_cell_diam,
        es_seg_marker = es_seg_marker,
        es_rare_marker = es_rare_marker,
        # file system
        s_regpath = s_regpath,
        s_segpath = s_segpath,
        # gpu
        b_gpu = b_gpu,
    )



# spawner
def segment_spawn(
        # input
        es_slide,
        s_task,  # known segmentation tasks are nuc, cell, or nuccell, and match
        # segmentation
        i_nuc_diam = 30,
        i_cell_diam = 30,
        s_dapi_round = 'R1',  # usualy the round we regsiter to, but by miltenyi the dapi round is R0 
        es_seg_marker = None, # {'Ecad'} this is only for the cell not the nucleus segmentation
        es_rare_marker = set(),  # this are markers that have to be enhanced
        s_type_data = 'cmif', # cmif codex
        # gpu
        s_gpu = 'gpu:1',  # None if no gpu is used anything else if gpu is used. e.g. slurm string possible 'gpu:p100:1' (fast) 'gpu:v100:1' (slow), 'gpu:1' (any)
        # processing
        s_type_processing = 'slurm',
        s_slurm_partition = 'exacloud',
        s_slurm_mem ='32G',
	    s_slurm_time ='36:00:00',
	    s_slurm_account ='gray_lab',
        # file system
        s_regdir = config.d_nconv['s_regdir'],  #'./RegisteredImages/',
        s_format_regdir = config.d_nconv['s_format_regdir'],   #'{}{}/', # s_regdir, s_slide_pxscene
        s_segdir = config.d_nconv['s_segdir'],  #'./SubtractedRegisteredImages/',
        s_format_segdir_cellpose = config.d_nconv['s_format_segdir_cellpose'],  #'{}{}_CellposeSegmentation/', # s_segdir, s_slide
    ):
    '''
    version: 2021-08-03

    input:
        # input
        es_slide: set of slidenames that shoul get segmented.
        s_task: which task should be run? do nuclei, cell, or nuccell segmentaion or matching nucleus and cell labels.
            knowen tasks are 'nuc', 'cell', 'nuccell', and 'match'.
        # segmentation parameter
        i_nuc_diam: minimum nucleus diameter in pixel.
        i_cell_diam: minimum cell diameter in pixel.
        s_dapi_round: dapi round used for nucleus segmenation. usualy the round we regsiter to, which is R1,
            but for e.g. miltenyi the dapi round we have to use is R0.
        es_seg_marker: set of cell segmentaion markers. usually Ecad for cancer cells, though can be more then one marker.
            None will only do nucleus segmentation, no cell segmentation. It is the same as the s_task = 'nuc' setting.
        es_rare: set of weak markers that have to be slightly enhanced in intensity though the scaleing step.
        s_type_data: this information is used for data type specific segmentaion processing. knownen are data type cmif and codex. default is cmif.
        s_gpu: slurm cluster gpu allocation. none None, any 'gpu:1',  faster 'gpu:v100:1', slower 'gpu:p100:1', not rapids compatible 'gpu:rtx2080:1'
        # processing parameter
        s_type_processing: to specify if registration should be run on the slurm cluster or on a simple slurp machine.
        s_partition: slurm cluster partition to use. options are 'exacloud', 'light'.
        s_mem: slurm cluster memory allocation. format '64G'.
        s_time: slurm cluster time allocation in hour or day format. max '36:00:00' [hour] or '30-0' [day].
        s_account: slurm cluster account to credit time from. 'gray_lab', 'chin_lab', 'heiserlab'.
        # file system
        s_regdir: registrated image directory.
        s_format_regdir: regisered imge subfolder format string.
        s_segdir: segmentation directory
        s_format_segdir_cellpose: segmentation folder subdirectory where for each slide the cellpose segmentation results are stored.

    output:
        spawned nucleus or cell segmentaion or cell to nuc lable matching jobs.

    description:
        spawns cellpose segmentation jobs by modifying a python and bash script,
        saving them and calling with subprocess.
        run either on slurm cluster or normal machine.
    '''
    # for each folder in regdir
    for s_folder in sorted(os.listdir(s_regdir)):
        # detect input folder which can be in a registered slide or in a slide_pxscene folder
        b_found = any([s_folder.startswith(s_slide) for s_slide in es_slide])
        if b_found:
            s_imgdir = f'{s_regdir}{s_folder}/'
            # for each pxscene
            df_img = basic.parse_tiff_reg(s_wd=f'{s_regdir}{s_folder}/')
            for s_slide_pxscene in sorted(set(df_img.slide_scene)):
                print(f'Processing {s_task} {s_slide_pxscene} ...')

                # match
                if s_task == 'match':
                    # manipulate input
                    s_gpu = None

                    # load template script
                    s_pathfile_template = f'{s_path_module}src/template_segmentation_match.py'
                    with open(s_pathfile_template) as f:
                        s_stream = f.read()

                    # edit template code (order matters!)
                    # parameters
                    s_stream = s_stream.replace('peek_s_slide_pxscene', s_slide_pxscene)
                    s_stream = s_stream.replace('peek_s_type_data', s_type_data)
                    # file system
                    s_stream = s_stream.replace('peek_s_segdir', s_segdir)
                    s_stream = s_stream.replace('peek_s_format_segdir_cellpose', s_format_segdir_cellpose)

                    # write executable code to file
                    time.sleep(4)
                    s_pathfile_executable = f'segmentation_{s_task}_{s_slide_pxscene}.py'.replace('-','')
                    with open(s_pathfile_executable, 'w') as f:
                        f.write(s_stream)

                # nuc, cell, nuccell segmentation
                else:
                    # handle input
                    b_gpu = False
                    if (s_gpu != None):
                       b_gpu = True

                    # get dapi image file name
                    s_tiff_dapi = df_img.loc[(df_img.loc[:,'round'] == s_dapi_round) & (df_img.color == config.d_nconv['s_color_dapi_jinxif']) & (df_img.slide_scene == s_slide_pxscene),:].index[0]

                    # load template script
                    s_pathfile_template = f'{s_path_module}src/template_segmentation_nuccell.py'
                    with open(s_pathfile_template) as f:
                        s_stream = f.read()

                    # edit template code (order  matters!)
                    # parameter
                    s_stream = s_stream.replace('peek_s_slide_pxscene', s_slide_pxscene)
                    s_stream = s_stream.replace('peek_s_task', s_task)
                    s_stream = s_stream.replace('peek_s_tiff_dapi', s_tiff_dapi)
                    s_stream = s_stream.replace('peek_i_nuc_diam', str(i_nuc_diam))
                    s_stream = s_stream.replace('peek_i_cell_diam', str(i_cell_diam))
                    s_stream = s_stream.replace('peek_es_seg_marker', str(es_seg_marker))
                    s_stream = s_stream.replace('peek_es_rare_marker', str(es_rare_marker))
                    # files system
                    s_stream = s_stream.replace('peek_s_regdir', s_regdir)
                    s_stream = s_stream.replace('peek_s_format_regdir', s_format_regdir)
                    s_stream = s_stream.replace('peek_s_segdir', s_segdir)
                    s_stream = s_stream.replace('peek_s_format_segdir_cellpose', s_format_segdir_cellpose)
                    # gpu
                    s_stream = s_stream.replace('peek_b_gpu', str(b_gpu))  # output basin files

                    # write executable code to file
                    time.sleep(4)
                    s_pathfile_executable = f'segmentation_{s_task}_{s_slide_pxscene}.py'
                    with open(s_pathfile_executable, 'w') as f:
                        f.write(s_stream)


                # execute segmentation script
                time.sleep(4)
                if (s_type_processing == 'slurm'):
                    # generate sbatch file
                    s_pathfile_sbatch = f'segmentation_{s_task}_{s_slide_pxscene}.sbatch'
                    config.slurmbatch(
                        s_pathfile_sbatch=s_pathfile_sbatch,
                        s_srun_cmd=f'python3 {s_pathfile_executable}',
                        s_jobname=f's{s_task[0]}{s_slide_pxscene}',
                        s_partition=s_slurm_partition,
                        s_gpu=s_gpu,
                        s_mem=s_slurm_mem,
                        s_time=s_slurm_time,
                        s_account=s_slurm_account,
                    )
                    # Jenny this is cool! Popen rocks.
                    subprocess.run(
                        ['sbatch', s_pathfile_sbatch],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                    )
                else:  # non-slurm
                    # Jenny this is cool! Popen rocks.
                    s_file_stdouterr = f'slurp-segmentation_{s_task}_{s_slide_pxscene}.out'
                    subprocess.run(
                        ['python3', s_pathfile_executable],
                        stdout=open(s_file_stdouterr, 'w'),
                        stderr=subprocess.STDOUT,
                    )


# plot z projection and basin label file
def _make_nuccell_zprojlabel_imgs(
        # tissue edge distance detection
        s_tissue_dapi = 'DAPI1',
        i_tissue_dapi_thresh = 512,
        i_tissue_area_thresh = 65536,
        # file system
        s_segpath = 'nop/',
        s_qcpath = 'nop/',
    ):
    '''
    version: 2021-10-12
    check out function nuccell_zprojlabel_imgs.

    description:
        this internal subfunction is only necessay because of the galaxy port.
    '''
    es_slidepxscene_nuc = set()
    es_slidepxscene_nuccellmatched = set()
    es_slidepxscene_nuccellmatchedexp = set()
    for s_file in sorted(os.listdir(s_segpath)):

        # detect segmentation label file and extract infromation
        s_slidepxscene = None
        i_exp = 0
        b_nuc = False
        b_nuccellmatched = False
        b_nuccellmatchedfeat = False
        o_match = re.search(config.d_nconv['s_regex_tiff_celllabel_nuccellmatchedfeat'], s_file)
        if not (o_match is None):
            s_slide = o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatchedfeat']['s_slide']]  # bue: given as function input!
            s_pxscene = o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatchedfeat']['s_pxscene']]
            s_seg_markers = o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatchedfeat']['s_seg_markers']]
            i_nuc_diam = int(o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatchedfeat']['i_nuc_diam']])
            i_cell_diam = int(o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatchedfeat']['i_cell_diam']])
            i_exp = int(o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatchedfeat']['i_exp']])
            s_slidepxscene = f'{s_slide}_{s_pxscene}'
            b_nuc = True
            b_nuccellmatched = True
            b_nuccellmatchedexp = True
        else:
            o_match = re.search(config.d_nconv['s_regex_tiff_celllabel_nuccellmatched'], s_file)
            if not (o_match is None):
                s_slide = o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatched']['s_slide']]  # bue: given as function input!
                s_pxscene = o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatched']['s_pxscene']]
                s_seg_markers = o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatched']['s_seg_markers']]
                i_nuc_diam = int(o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatched']['i_nuc_diam']])
                i_cell_diam = int(o_match[config.d_nconv['di_regex_tiff_celllabel_nuccellmatched']['i_cell_diam']])
                s_slidepxscene = f'{s_slide}_{s_pxscene}'
                b_nuc = True
                b_nuccellmatched = True
                b_nuccellmatchedexp = False
            else:
                o_match = re.search(config.d_nconv['s_regex_tiff_celllabel_nuc'], s_file)
                if not (o_match is None):
                    s_slide = o_match[config.d_nconv['di_regex_tiff_celllabel_nuc']['s_slide']]  # bue: given as function input!
                    s_pxscene = o_match[config.d_nconv['di_regex_tiff_celllabel_nuc']['s_pxscene']]
                    s_seg_markers = None
                    i_nuc_diam = int(o_match[config.d_nconv['di_regex_tiff_celllabel_nuc']['i_nuc_diam']])
                    i_cell_diam = None
                    s_slidepxscene = f'{s_slide}_{s_pxscene}'
                    b_nuc = True
                    b_nuccellmatched = False
                    b_nuccellmatchedexp = False
                else:
                    pass

        # plot
        if not (o_match is None) and ( \
                (b_nuc and not s_slidepxscene in es_slidepxscene_nuc) or \
                (b_nuccellmatched and not s_slidepxscene in es_slidepxscene_nuccellmatched) or \
                (b_nuccellmatchedexp and not s_slidepxscene in es_slidepxscene_nuccellmatchedexp) 
            ):
            print(f'run jinxif.segment.nuccell_zprojlabel_imgs for slide_scene: {s_slidepxscene}')
 
            # generate plot
            fig, ax = plt.subplots(nrows=2, ncols=4, figsize=(16,8))

            # load img files into plot
            # nucleus
            ax[0,0].set_title('nuc z projection')
            ax[0,0].imshow(io.imread(s_segpath + config.d_nconv['s_format_png_nucprojection'].format(s_slidepxscene, i_nuc_diam)))
            ax[0,1].set_title('nuc label')
            ax[0,1].imshow(io.imread(s_segpath + config.d_nconv['s_format_tiff_celllabel_nuc'].format(s_slidepxscene, i_nuc_diam)))
            ax[0,2].set_title('tissue edge distance')
            ax[0,3].set_title('tissue mask')
            try:
                ai_distances = io.imread(s_segpath + config.d_nconv['s_format_tiff_tissueedgedistance'].format(s_slidepxscene, s_tissue_dapi, i_tissue_dapi_thresh, i_tissue_area_thresh))
                ab_tissue = ai_distances > 0
                ax[0,2].imshow(ai_distances)
                ax[0,3].imshow(ab_tissue)
            except FileNotFoundError:
                #ax[0,2].axis('off')
                #ax[0,3].axis('off')
                pass
            # cell
            ax[1,0].set_title('cell z projection')
            try:
                ax[1,0].imshow(io.imread(s_segpath + config.d_nconv['s_format_png_cellprojection'].format(s_slidepxscene, s_seg_markers, i_cell_diam)))  # bue: s_seg_markers == s_z_label
            except FileNotFoundError:
                #ax[1,0].axis('off')
                pass
            ax[1,1].set_title('cell label - original')
            try:
                ax[1,1].imshow(io.imread(s_segpath + config.d_nconv['s_format_tiff_celllabel_cell'].format(s_slidepxscene, s_seg_markers, i_cell_diam)))
            except FileNotFoundError:
                #ax[1,1].axis('off')
                pass
            ax[1,2].set_title('cell label - nuc ok')
            try:
                ax[1,2].imshow(io.imread(s_segpath + config.d_nconv['s_format_tiff_celllabel_nuccellmatched'].format(s_slidepxscene, s_seg_markers, i_nuc_diam, i_cell_diam)))
            except FileNotFoundError:
                #ax[1,2].axis('off')
                pass
            # feature corrected img
            ax[1,3].set_title('cell label - nuc feat ok')
            try:
                ax[1,3].imshow(io.imread(s_segpath + config.d_nconv['s_format_tiff_celllabel_nuccellmatchedfeat'].format(s_slidepxscene, s_seg_markers, i_nuc_diam, i_cell_diam, i_exp)))
            except FileNotFoundError:
                #ax[1,3].axis('off')
                pass

            # finish plot
            fig.suptitle(f'{s_slidepxscene} segmentation')
            os.makedirs(s_qcpath, exist_ok=True)
            fig.savefig(s_qcpath + f'{s_slidepxscene}_nuccell_zprojection_labelbasin_img.png', facecolor='white')
            plt.close()

            # update es_slidepxscene_nuccellmatch
            if (b_nuc):
                es_slidepxscene_nuc.add(s_slidepxscene)
            if (b_nuccellmatched):
                es_slidepxscene_nuccellmatched.add(s_slidepxscene)
            if (b_nuccellmatchedexp):
                es_slidepxscene_nuccellmatchedexp.add(s_slidepxscene)


def nuccell_zprojlabel_imgs(
        s_slide,
        # tissue edge distance
        s_tissue_dapi = 'DAPI1',
        i_tissue_dapi_thresh = 512,
        i_tissue_area_thresh = 65536,
        # file system
        s_segdir = config.d_nconv['s_segdir'],  #'./Segmentation/',
        s_format_segdir_cellpose = config.d_nconv['s_format_segdir_cellpose'],  #'{}{}_CellposeSegmentation/',  # s_segdir, s_slide
        s_qcdir = config.d_nconv['s_qcdir'],  #'./QC/',
    ):
    '''
    version: 2021-07-13

    input:
        s_slide: slide scene id to process.
        s_tissue_dapi: by dapi and round marker label specify the image which should be used for tissue detection.
        i_tissue_dapi_thresh: dapi threshold value for tissue, which will be much lower then the dapi positive nucleus value, 
            in our experience, something between 300 and 600.
        i_tissue_area_thresh: specify pixel area treshold to use to fill tissue gaps between dapi nuclei.
        s_segdir: segmentation directory.
        s_format_segdir_cellpose: segmentation directory cellpose segmentation format string.
        s_qcdir: quality control directory.

    output:
       png plot at s_qcdir + s_segdir.split('/')[-2]

    description:
        function to generate for each slide_pxscene for a slice a summary nuc and cell z projection and basin label plot for quality control.
    '''
    # for slide in segmentation dir
    s_segpath = s_format_segdir_cellpose.format(s_segdir, s_slide)
    s_qcpath = s_qcdir + s_segdir.split('/')[-2] + '/'

    # subfunction call
    _make_nuccell_zprojlabel_imgs(
        # tissue edge distance detection
        s_tissue_dapi = s_tissue_dapi,
        i_tissue_dapi_thresh = i_tissue_dapi_thresh,
        i_tissue_area_thresh = i_tissue_area_thresh,
        # file system
        s_segpath = s_segpath,
        s_qcpath = s_qcpath,
    )


# spawner function
def nuccell_zprojlabel_imgs_spawn(
        es_slide,
        # tissue edge distance
        s_tissue_dapi = 'DAPI1',
        i_tissue_dapi_thresh = 400,
        i_tissue_area_thresh = 50000,
        # processing
        s_type_processing = 'slurm',
        s_slurm_partition = 'exacloud',
        s_slurm_mem = '32G',
        s_slurm_time = '36:00:0',
        s_slurm_account = 'gray_lab',
        # file system
        s_segdir = config.d_nconv['s_segdir'],  #'./Segmentation/',
        s_format_segdir_cellpose = config.d_nconv['s_format_segdir_cellpose'],  #'{}{}_CellposeSegmentation/',  # s_segdir, s_slide
        s_qcdir = config.d_nconv['s_qcdir'],  #'./QC/'
    ):
    '''
    version: 2021-07-13

    input:
        es_slide: set of slide id from which per pxscene qc images should be generated.
        s_tissue_dapi: by dapi and round marker label specify the image which should be used for tissue detection.
        i_tissue_dapi_thresh: dapi threshold value for tissue, which will be much lower then the dapi positive nucleus value, 
            in our experience, something between 300 and 600.
        i_tissue_area_thresh: specify pixel area treshold to use to fill tissue gaps between dapi nuclei.
        s_type_processing: string to specify if pipeline is run on a slum cluster on not.
            knowen vocabulary is slurm and any other string.
        s_slurm_partition: slurm cluster partition to use.
            OHSU ACC options are 'exacloud', 'light', (and 'gpu').
            the default is tweaked to OHSU ACC settings.
        s_slurm_mem: slurm cluster memory allocation. format '64G'.
        s_slurm_time: slurm cluster time allocation in hour or day format.
            OHSU ACC max is '36:00:00' [hour] or '30-0' [day].
            the related qos code is tewaked to OHSU ACC settings.
        s_slurm_account: slurm cluster account to credit time from.
            my OHSU ACC options are 'gray_lab', 'chin_lab', 'heiserlab'.

        s_segdir: segmentation directory.
        s_format_segdir_cellpose: segmentation directory cellpose segmentation format string.
        s_qcdir: quality control directory.

    output:
        png plot under s_qcdir + s_segdir.split("/")[-2]

    description:
        generte array raw images to check tissue identity, focus, etc.
    '''
    # for each slide
    for s_slide in sorted(es_slide):
        # this have to be a python template!
        print(f'nuccell_zprojlabel_imgs_spawn: {s_slide}')

        # set run commands
        s_pathfile_template = 'template_nuccellzprojlabel_slide.py'
        s_pathfile = f'nuccellzprojlabel_slide_{s_slide}.py'
        s_srun_cmd = f'python3 {s_pathfile}'
        ls_run_cmd = ['python3', s_pathfile]

        ## any ##
        # load template script code
        with open(f'{s_path_module}src/{s_pathfile_template}') as f:
            s_stream = f.read()

        # edit code generic
        s_stream = s_stream.replace('peek_s_slide', s_slide)
        s_stream = s_stream.replace('peek_s_tissue_dapi', s_tissue_dapi)
        s_stream = s_stream.replace('peek_i_tissue_dapi_thresh', str(i_tissue_dapi_thresh))
        s_stream = s_stream.replace('peek_i_tissue_area_thresh', str(i_tissue_area_thresh))
        s_stream = s_stream.replace('peek_s_segdir', s_segdir)
        s_stream = s_stream.replace('peek_s_format_segdir_cellpose', s_format_segdir_cellpose)
        s_stream = s_stream.replace('peek_s_qcdir', s_qcdir)

        # write executable afsubtraction script code to file
        time.sleep(4)
        with open(s_pathfile, 'w') as f:
            f.write(s_stream)

        # execute script code
        time.sleep(4)
        if (s_type_processing == 'slurm'):
            # generate sbatch file
            s_pathfile_sbatch = f'nuccellzprojlabel_slide_{s_slide}.sbatch'
            config.slurmbatch(
                s_pathfile_sbatch = s_pathfile_sbatch,
                s_srun_cmd = s_srun_cmd,
                s_jobname = f'q{s_slide}',
                s_partition = s_slurm_partition,
                s_gpu = None,
                s_mem = s_slurm_mem,
                s_time = s_slurm_time,
                s_account = s_slurm_account,
            )
            # Jenny this is cool! Popen rocks.
            subprocess.run(
                ['sbatch', s_pathfile_sbatch],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        else:  # non-slurm
            # Jenny this is cool! Popen rocks.
            s_file_stdouterr = f'slurp-nuccellzprojlabel_slide_{s_slide}.out'
            o_process = subprocess.run(
                ls_run_cmd,
                stdout=open(s_file_stdouterr, 'w'),
                stderr=subprocess.STDOUT,
            )


# development code
'''
import napari
labels = io.imread('Scene 059 nuclei20 - Nuclei Segmentation Basins.tif')
cell_labels = io.imread('Scene 059 cell25 - Cell Segmentation Basins.tif')
cyto_img = io.imread('Scene 059 - CytoProj.png')
dapi_img = io.imread('Scene 059 - ZProjectionDAPI.png')
viewer = napari.Viewer()
viewer.add_labels(labels,blending='additive')
viewer.add_labels(cell_labels,blending='additive')
viewer.add_image(cyto_img,blending='additive')
viewer.add_image(dapi_img,blending='additive',colormap='blue')
#cell_boundaries = skimage.segmentation.find_boundaries(cell_labels,mode='outer')
#viewer.add_labels(cell_boundaries,blending='additive')
#nuclear_boundaries = skimage.segmentation.find_boundaries(labels,mode='outer')
#viewer.add_labels(nuclear_boundaries,blending='additive',num_colors=2)
closing = skimage.morphology.closing(cell_labels)
viewer.add_labels(closing,blending='additive')
container = nuc_to_cell(labels,closing)#cell_labels)
#matched cell labels
cells_relabel = relabel_numba(container[0],closing)
#remove background
mode = scipy.stats.mode(cells_relabel,axis=0)[0][0][0]
black = cells_relabel.copy()
black[black==mode] = 0
viewer.add_labels(black,blending='additive')
cell_boundaries = skimage.segmentation.find_boundaries(cells_relabel,mode='outer')
viewer.add_labels(cell_boundaries,blending='additive')
#ring
overlap = black==labels
viewer.add_labels(overlap, blending='additive')
#cytoplasm
ring_rep = black.copy()
ring_rep[overlap] = 0
viewer.add_labels(ring_rep, blending='additive')
#membrane
rim_labels = contract_membrane(black)
viewer.add_labels(rim_labels, blending='additive')
#expanded nucleus
__,__,peri_nuc = expand_nuc(labels,distance=3)
viewer.add_labels(peri_nuc, blending='additive')
'''
