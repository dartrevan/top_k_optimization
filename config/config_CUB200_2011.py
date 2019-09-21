DATA_ROOT="~/datasets"
DATASET = 'CUB200-2011' 
NET =  "bn_inception_v2" #"densenet201"
EMBEDDING_WIDTH =64
DATASET_NUM = 5864   #train
WITH_BOUNDING_BOX = False
DOWNLOAD = True
TEST_K = 10
TEST_BATCH_SIZE = 10
#general parameter
USE_CUDA = 1
EPOCH = 100000
LAMDA=1
METRIC_LOSS_PARAM = LAMDA
TRAINING_OLD = 0
TRAIN_CLASS = 100    #cifar100:80 CUB200:100 CARS196:98
TEST_CLASS = TRAIN_CLASS
MODEL_PATH = "model_param/"+NET+"_cub200_2011_"+str(WITH_BOUNDING_BOX)+"_"
K = 5            #3 5  10
N = 55             #
POS_SAMPLE_NUM = 10  #8 10  20
MULTI_THREAD = 1

GPU_NUM = '0'
METHOD = 0 #0:prec@k loss
METRIC_LOSS_LR = 1e-3
SCHEDULER_STEP = [8, 20, 70]

if METHOD == 0:      #0:prec@k loss 
	MARGIN = 0.05      #up to 0.4 
	SHOW_PER_ITER = 100
	BATCH_SIZE = 64   #0:20     1:200     2:500     3:500
	EMBD_LR = 1e-5
	SOFTMAX_LOSS_LR = 1e-4
	NET_LR = 1e-3
	WEIGHT_DECAY = 5e-4
	GAMMA=1e-1
