import sys
from ...common.configuration import HAS_CAIMAN, HAS_TENSORFLOW#, HAS_ISX

__all__ = [
    'mesfile_io',
    'roi_manager',
    'tiff_io',
    'stimulus_mapping',
    'script_editor',
    'suite2p',
    'femtonics_mesc',
    'exporter',
]

if HAS_CAIMAN:
    __all__ += \
    [
        'cnmfe',
        'cnmf',
        'cnmf_3d',
        'caiman_motion_correction',
        'caiman_importer',
        'caiman_dfof'
    ]

if HAS_TENSORFLOW:
    __all__ += \
        [
            'nuset_segment',
        ]

if sys.version_info[1] >= 8:
    __all__ += ['inscopix_importer']

#if HAS_ISX:
#    __all__ += \
#    [
#        'inscopix_importer'
#    ]
