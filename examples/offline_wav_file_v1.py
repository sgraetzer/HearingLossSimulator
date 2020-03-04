# Added this to load hearinglossimulator module from local directory
MODULE_PATH = "/home/simone/hls/hearinglosssimulator/__init__.py"
MODULE_NAME = "hearinglosssimulator"
import importlib
import importlib.util
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module 
spec.loader.exec_module(module)

import hearinglosssimulator as hls
import sys

in_filename = 'in_sound.wav'
out_filename = 'out_sound_withloss.wav'

#this parameters is important
calibration =  93 #dbSPL for 0dBFs


# define loss parameters
loss_params = {  'left' : {'freqs' :  [125., 250., 500., 1000., 2000., 4000., 8000.],
                                            'compression_degree': [0.5,0.5,0.5,0.5,0.5,0.5,0.5],
                                            'passive_loss_db' : [0,10,20,30,40,50,70],
                                        },
                            'right' : {'freqs' :  [125., 250., 500., 1000., 2000., 4000., 8000.],
                                            'compression_degree': [0.5,0.5,0.5,0.5,0.5,0.5,0.5],
                                            'passive_loss_db' : [0,10,20,30,40,50,70],
                                        }
                        }

params = dict(nb_freq_band=32, low_freq = 100., high_freq = 8000.,
        tau_level = 0.005,  level_step =1., level_max = 100.,
        calibration =  calibration,
        loss_params = loss_params,
        chunksize=512, backward_chunksize=1024)

gpu_platform_index=0#Put None to manually select
gpu_device_index=0#Put None to manually select


hls.compute_wave_file(in_filename, out_filename, processing_class=hls.InvComp, duration_limit = 10., 
            gpu_platform_index =gpu_platform_index, gpu_device_index=gpu_device_index,
                **params)


