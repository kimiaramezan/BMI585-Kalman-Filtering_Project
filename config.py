# Define constants
ORIGINAL_SAMPLE_RATE = 200  # Original sample rate
NEW_SAMPLE_RATE = 100       # New sample rate
NOTCH_FREQ_US = 60.         # Notch frequency for US
NOTCH_FREQ_EUR = 50.        # Notch frequency for Europe
BANDPASS_FREQ_EEG = [0.5, 40]  # Bandpass frequencies for EEG
BANDPASS_FREQ_AIRFLOW = [0.1, 10]  # Bandpass frequencies for airflow
BANDPASS_FREQ_ECG = [0.5, 40]      # Bandpass frequencies for ECG
BANDPASS_FREQ_EOG = [0.1, 40]      # Bandpass frequencies for EOG
HIGHPASS_FREQ_EMG = 10        # Bandpass frequencies for EMG

NUM_PROCESSES = 4

# Define input channels (a complete list of channels)
"""
channel_groups = {
    "EEG": ["c3-m2", "c4-m1", "cz-oz", "f3-m2", "f4-m1", "o1-m2", "o2-m1"],
    "EOG": ["e1-m2", "e2-m1"],
    "CHIN": ["chin1-chin2"],
    "RESP": ["abd", "airflow", "cflow", "ptaf", "chest", "spo2", "xflow"],
    "ECG": ["ecg"],
    "EMG_R": ["rat"],
    "EMG_L": ["lat"]
}
"""

"""
channel_groups = {
    "EEG": ["c3-m2", "c4-m1", "cz-oz", "f3-m2", "f4-m1", "o1-m2", "o2-m1"],
    "EOG": ["e1-m2", "e2-m1"],
    "CHIN": ["chin1-chin2"]
}
"""

channel_groups = {
    "EEG": ["c3-m2", "c4-m1"],
    "EOG": ["e1-m2","e2-m1"]
}

# Define output channels (a complete list of channels)
label_groups = {
    "Stage": ["stage_expert_0"],
    "Arousal": ["arousal-shifted_converted_0", "arousal_expert_0"],
    "Resp": ["resp-h3_expert_0", "resp-h4_expert_0", "resp_expert_0"],
    "Limb": ["limb_expert_0"],
    "Sex": ["sex"],
    "Age": ["age"]
}

# Define the number of classes for each task

#num_classes = [5, 2, 6, 2, 2, 20]

num_classes = [5]

class_weights_tasks = [[1.2002, 0.4115, 2.1034, 2.8953, 1.0921], [0.5198, 13.1029]]


# Define the modalities that need at least one channel
#mandatory_groups = ["EEG", "EOG", "CHIN", "RESP", "ECG"]
mandatory_groups = ["EEG","EOG"]

num_to_type_apnea = {1:"OA", 2:"CA", 3:"MA", 4:"HY", 5:"RA"}

# Sex and Age encoding as sinusoidal waves
CARRIER_FREQ = 0.001
CARRIER_AMP = 0.2


datasets_to_folders_pre = {'shhs': 'shhs_corrected', 'mros':'mros_v3-h3', 'mgh':'mgh_v7','mesa':'mesa_v3-h3', 'emory': 'emory'}
datasets_to_folders = {'shhs_corrected': 'shhs', 'mros_v3-h3':'mros', 'mgh_v7':'mgh','mesa_v3-h3':'mesa', 'emory': 'emory'}

# Paths

# Nona
path_raw = '/labs/nasirilab/CAISR1.0/prepared_data/'
path_preprocessed = '/labs/nasirilab/UFNet/pre_processed/arshak_16_min/'

train_subjects_csv_file = '/labs/nasirilab/hfirooz/FoundationModel/csv_training_70_vld_15_test_15/train_50_Feb1st.csv'
val_subjects_csv_file = '/labs/nasirilab/hfirooz/FoundationModel/csv_training_70_vld_15_test_15/val_15_Feb1st.csv'

patients_demographic_csv_file = '/labs/nasirilab/hfirooz/FoundationModel/table1/caisr_table1_total_emory.csv'

# Samaneh
# path_raw = '/labs/nasirilab/CAISR1.0/prepared_data/'
# path_preprocessed = '/labs/nasirilab/UFNet/pre_processed/arshak_28_Feb/'


# #train_subjects_csv_file = '/home/snasiri/Desktop/FoundationModel/csv_training_70_vld_15_test_15/train_50_Feb1st.csv'
# train_subjects_csv_file = '/home/snasiri/Desktop/FoundationModel/csv_training_70_vld_15_test_15/train_700_Jan31.csv'

# #val_subjects_csv_file = '/home/snasiri/Desktop/FoundationModel/csv_training_70_vld_15_test_15/val_15_Feb1st.csv' #val_150_Jan31.csv'
# val_subjects_csv_file = '/home/snasiri/Desktop/FoundationModel/csv_training_70_vld_15_test_15/val_150_Jan31.csv'


# patients_demographic_csv_file = '/home/snasiri/Desktop/FoundationModel/table1/caisr_table1_total_emory.csv'


# Arshak
#path_raw = '/mnt/c/Users/marya/Downloads/CAISR_data'
#path_preprocessed = '/mnt/c/Users/marya/Downloads/CAISR_data_preprocessed'

#path_raw = '/media/arshak/New Volume/data'
#path_preprocessed = '/media/arshak/New Volume/preprocessed'

#train_subjects_csv_file = '/home/arshak/Desktop/Project/FoundationModel/csv_training_70_vld_15_test_15/test.csv'
#val_subjects_csv_file = '/home/arshak/Desktop/Project/FoundationModel/csv_training_70_vld_15_test_15/test.csv'
#patients_demographic_csv_file = '/home/arshak/Desktop/Project/FoundationModel/table1/caisr_table1_total_emory.csv'

required_columns = ['cohort', 'path_preprocessed', 'sex', 'age']

# Dataset parameters
segment_duration_minutes = 16  # Segment length for extraction
segment_duration_samples = int(segment_duration_minutes * 60 * NEW_SAMPLE_RATE) 

min_duration_minutes = 4
max_duration_minutes = 16

min_duration_samples = int(min_duration_minutes * 60 * NEW_SAMPLE_RATE) 
max_duration_samples = int(max_duration_minutes * 60 * NEW_SAMPLE_RATE) 


batch_size = 8
batch_size = 2
#learning_rate = 0.0001
#l2 = 1e-3
num_epochs = 4000

base_lr = 3e-4
weight_decay = 0.0001
warmup_pct = 0.1
final_div_factor = 10