from os.path import join
from .constants import DATA_DIR

PARCELLATIONS_DIR = join(DATA_DIR, "HumanCorticalParcellations")

PARCELLATIONS = {
    'Glasser': {
        'dlabel': join(PARCELLATIONS_DIR, 
            "Glasser2016/Q1-Q6_RelatedValidation210.CorticalAreas_dil_" 
            "Final_Final_Areas_Group_Colors.32k_fs_LR.dlabel.nii"),
        'n_regions': 360
    },
    'SchaeferLG_100': {
        'dlabel': join(PARCELLATIONS_DIR, 
            "Schaefer2018_LocalGlobal/Schaefer2018_100Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 100
    },
    'SchaeferLG_200': {
        'dlabel': join(PARCELLATIONS_DIR, 
            "Schaefer2018_LocalGlobal/Schaefer2018_200Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 200
    },
    'SchaeferLG_300': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_300Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 300
    },
    'SchaeferLG_400': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_400Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 400
    },
    'SchaeferLG_500': {
        'dlabel': join(PARCELLATIONS_DIR, 
            "Schaefer2018_LocalGlobal/Schaefer2018_500Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 500
    },
    'SchaeferLG_600': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_600Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 600
    },
    'SchaeferLG_700': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_700Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 700
    },
    'SchaeferLG_800': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_800Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 800
    },
    'SchaeferLG_900': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_900Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 900
    },
    'SchaeferLG_1000': {
        'dlabel': join(PARCELLATIONS_DIR,
            "Schaefer2018_LocalGlobal/Schaefer2018_1000Parcels_"
            "17Networks_order.dlabel.nii"),
        'n_regions': 1000
    },
    'Yeo17': {
        'dlabel': join(PARCELLATIONS_DIR, 
            "Yeo2011/rsn_yeo-cortex_buckner-cerebellum_" 
            "choi-striatum_17networks_islands_MWfix.dlabel.nii"),
        'n_regions': 224
    }
}


SCENE_FILE = join(DATA_DIR, "Human.scene")
SCENE_ZIP_FILE = join(DATA_DIR, "scene.zip")
