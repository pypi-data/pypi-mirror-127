#!/bin/bash

#   colors can be specified as:
#   '(r,g,b)'     colors in the range 0-255
#   '(r,g,b,a)'   colors in the range 0-255  alpha in the range 0-1
#   'l_orange_0.7' for legs colors         0.0 for pale color, 1.0 for dark colors
#                  color can be one of 'brown','blue','green','orange', 'red','pink','purple','yellow', 'b_w'
#                  see: https://domutils.readthedocs.io/en/stable/legsTutorial.html#specifying-colors
#   
#   any other strings will be passed "as is" to matplotlib

#   linestyle: 'solid' 'dotted' 'dashed' 'dashdot'
#   passed "as is" to matplotlib "linestyle" argument of the ax.plot() method


#parameters for the aggregation
date_0='2016070200'       
date_f='2016082600'
delta_date=720
leadtime_0=-180
leadtime_f=730
delta_leadtime=10
leadtime_ignore=10
leadtime_greyed_out=(-180 180)
score_dir='/space/hall3/sitestore/eccc/mrd/rpndat/dja001/dasVerif/ominusp/'
outname_file_struc='%verified_name/%Y%m%d%H_sqlite/%verified_name_vs_%reference_name__%Y%m%d%H.sqlite3'
figure_dir='/space/hall3/sitestore/eccc/mrd/rpndat/dja001/test_new_griddedobs_tmp/'
verif_domains=('radars')
make_same=('True')
thresholds=(.1 .5 1. 5. 10.)
#time_series=('fbias' 'pod' 'far' 'csi' 'lmin' 'corr_coeff')
time_series=('fbias' 'csi' 'lmin')
twod_panels=('histograms')
n_cpus=1

#
#
#Use those to force the Y range for time_series figures
# comment them for automatic range
#ylim_fbias=(0.85 1.4)
#ylim_pod=(0.2   .38)
#ylim_far=(0.65 0.84)
#ylim_csi=(0.11 0.22)
#ylim_lmin=(5. 180.)
#ylim_corr_coeff=(0.07 0.13)

#
#name of reference dataset
reference_name='bmosaicsv8'

#
##experiments being verified
#exp_list=(       'N2CC800E16V1' 'N2CC802E16V1' 'DJA832E16'     )
#exp_desc=(       'ctrl'         'LHN_cycled'   'LHN_prog_only' )
#exp_color=(      'l_b_w_0.7'    'l_blue_0.7'   'l_orange_0.7'  )
#exp_linestyle=(  'dashed'       'solid'       'dashed'        )
#exp_linewidth=(  '2.5'          '2.5'          '2.5'           )

#exp_list=(       'N2CC800E16V1' 'DJA832E16'     'DJA837E16'     'DJA838E16'     'DJA839E16')
#exp_desc=(       'ctrl'         'LHN_prog_only' 'No_I_profiles' 'No_moist'      'No_smoothing')
#exp_color=(      'l_b_w_0.7'    'l_orange_0.7'  'l_pink_0.7'    'l_green_0.7'   'l_brown_0.7')
#exp_linestyle=(  'dashed'       'dashed'        'solid'         'dashed'        'solid')
#exp_linewidth=(  '2.5'          '2.5'           '2'             '2.5'           '2')

#'DJA838E16'    'DJA837E16'      'DJA839E16'      'DJA840E16'    'DJA841E16'  'DJA842E16'    'DJA843E16'        \
#'No_moist'     'No_I_profiles'  'No_smoothing'   'Canada_only'  'US_only'    'W_0.1'        'W_0.4'          \
#'l_orange_0.7' 'l_pink_0.7'     'l_purple_0.7'   'l_red_0.7'    'l_blue_0.7' 'l_yellow_0.7' 'l_brown_0.7'       \
#'dashed'       'solid'          'solid'          'solid'        'solid'      'solid'        'solid'            \
#'2.5'          '2'              '2'              '2'            '2'          '2'            '2'                \




#
#
#Users should not have to change anything below this line
##########################################################

#These systrem variables are important for preventing crashes
export XDG_RUNTIME_DIR=/space/hall3/sitestore/eccc/mrd/rpndat/dja001/tmpdir
export MPLBACKEND="agg" 
ulimit -s 128000
#make sure numpy does not use multithreading 
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
export NUMEXPR_NUM_THREADS=1   

#workaround the fact that argparse does not like arguments with no value
if [[ -z "${ylim_fbias}" ]]      ; then ylim_fbias=None; fi
if [[ -z "${ylim_pod}" ]]        ; then ylim_pod=None; fi
if [[ -z "${ylim_far}" ]]        ; then ylim_far=None; fi
if [[ -z "${ylim_csi}" ]]        ; then ylim_csi=None; fi
if [[ -z "${ylim_lmin}" ]]       ; then ylim_lmin=None; fi
if [[ -z "${ylim_corr_coeff}" ]] ; then ylim_corr_coeff=None; fi


#you can use :
#   python gridded_obs.py -h 
#for a complete description of arguments
python -c 'import gridded_obs; gridded_obs.aggregate()'               \
                    --date_0 ${date_0}                                \
                    --date_f ${date_f}                                \
                    --delta_date ${delta_date}                        \
                    --leadtime_0 ${leadtime_0}                        \
                    --leadtime_f ${leadtime_f}                        \
                    --delta_leadtime   ${delta_leadtime}              \
                    --leadtime_ignore  ${leadtime_ignore}             \
                    --leadtime_greyed_out  ${leadtime_greyed_out[*]}  \
                    --score_dir             ${score_dir}              \
                    --outname_file_struc ${outname_file_struc}        \
                    --figure_dir ${figure_dir}                        \
                    --verif_domains ${verif_domains[*]}               \
                    --make_same ${make_same}                          \
                    --thresholds  ${thresholds[*]}                    \
                                                                      \
                     --time_series  ${time_series[*]}                 \
                    --twod_panels   ${twod_panels[*]}                 \
                                                                      \
                    --n_cpus ${n_cpus}                                \
                                                                      \
                    --reference_name ${reference_name}                \
                                                                      \
                    --exp_list        ${exp_list[*]}                  \
                    --exp_desc        ${exp_desc[*]}                  \
                    --exp_color       ${exp_color[*]}                 \
                    --exp_linestyle   ${exp_linestyle[*]}             \
                    --exp_linewidth   ${exp_linewidth[*]}             \
                    --ylim_fbias      ${ylim_fbias[*]}                \
                    --ylim_pod        ${ylim_pod[*]}                  \
                    --ylim_far        ${ylim_far[*]}                  \
                    --ylim_csi        ${ylim_csi[*]}                  \
                    --ylim_lmin       ${ylim_lmin[*]}                 \
                    --ylim_corr_coeff ${ylim_corr_coeff[*]}           \

