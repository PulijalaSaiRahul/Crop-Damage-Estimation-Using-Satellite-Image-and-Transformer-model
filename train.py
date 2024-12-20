#importing necessary libraries

# coding=utf-8
import os
import torch.optim as optim                 #Torch's optimization algorithms
import torch.utils.data
from torch.utils.data import DataLoader     #Tools for handling dataset and loadings
from tqdm import tqdm                       #for creating progress bars
from data_utils import LoadDatasetFromFolder, DA_DatasetFromFolder, calMetric_iou   #custom utility function
import numpy as np                          #numerical operations
import random                               #generate random numbers
from model.network import CDNet
from train_options import parser            
import itertools                            #for creating iterators for eficient looping
from loss.losses import cross_entropy

args = parser.parse_args()                  # to parse the command-line arguments provided by the user based on the defined structure.
os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu_id            #setting environment
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# set seeds
# This ensures that if the script uses any random number generation from Python's random module, 
# the generated sequence will be the same each time the script runs with the same seed value.
def seed_torch(seed=2022):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
seed_torch(2022)

if __name__ == '__main__':
    mloss = 0

    # load data
    train_set = DA_DatasetFromFolder(args.hr1_train, args.hr2_train, args.lab_train, crop=False)
    val_set = LoadDatasetFromFolder(args, args.hr1_val, args.hr2_val, args.lab_val)
    train_loader = DataLoader(dataset=train_set, num_workers=args.num_workers, batch_size=args.batchsize, shuffle=True)
    val_loader = DataLoader(dataset=val_set, num_workers=args.num_workers, batch_size=args.val_batchsize, shuffle=True)

    # define model
    CDNet = CDNet(img_size = args.img_size).to(device, dtype=torch.float)

    if torch.cuda.device_count() > 1:
        print("Let's use", torch.cuda.device_count(), "GPUs!")
        CDNet = torch.nn.DataParallel(CDNet, device_ids=range(torch.cuda.device_count()))   #PyTorch module that enables parallel processing across multiple GPUs.

    # set optimization
    optimizer = optim.Adam(itertools.chain(CDNet.parameters()), lr= args.lr, betas=(0.9, 0.999))
    CDcriterionCD = cross_entropy().to(device, dtype=torch.float)           # initializes the optimizer and the loss function for the neural network model (CDNet)

    # training
    for epoch in range(1, args.num_epochs + 1):
        train_bar = tqdm(train_loader)
        running_results = {'batch_sizes': 0, 'SR_loss':0, 'CD_loss':0, 'loss': 0 }

        CDNet.train()           # enables training mode 

        for hr_img1, hr_img2, label in train_bar:
            running_results['batch_sizes'] += args.batchsize

            hr_img1 = hr_img1.to(device, dtype=torch.float)
            hr_img2 = hr_img2.to(device, dtype=torch.float)
            label = label.to(device, dtype=torch.float)
            label = torch.argmax(label, 1).unsqueeze(1).float()

            result1, result2, result3= CDNet(hr_img1, hr_img2)

            CD_loss = CDcriterionCD(result1, label) +CDcriterionCD(result2, label)+CDcriterionCD(result3, label)

            CDNet.zero_grad()       # Clears the gradients calculated in the previous iteration.

            CD_loss.backward()      #Computes the gradients of the loss with respect to the model parameters
            optimizer.step()        #Updates the model parameters using the optimizer based on the computed gradients

            running_results['CD_loss'] += CD_loss.item() * args.batchsize

            train_bar.set_description(
                desc='[%d/%d] loss: %.4f' % (
                    epoch, args.num_epochs,
                    running_results['CD_loss'] / running_results['batch_sizes'],))

        # eval
        CDNet.eval()            # starts model evaluation

        with torch.no_grad():
            val_bar = tqdm(val_loader)
            inter, unin = 0,0
            valing_results = {'batch_sizes': 0, 'IoU': 0}

            for hr_img1, hr_img2, label in val_bar:
                valing_results['batch_sizes'] += args.val_batchsize

                hr_img1 = hr_img1.to(device, dtype=torch.float)
                hr_img2 = hr_img2.to(device, dtype=torch.float)
                label = label.to(device, dtype=torch.float)
                label = torch.argmax(label, 1).unsqueeze(1).float()

                cd_map,_,_ = CDNet(hr_img1, hr_img2)

                CD_loss = CDcriterionCD(cd_map, label)

                cd_map = torch.argmax(cd_map, 1).unsqueeze(1).float()

                gt_value = (label > 0).float()
                prob = (cd_map > 0).float()
                prob = prob.cpu().detach().numpy()

                gt_value = gt_value.cpu().detach().numpy()
                gt_value = np.squeeze(gt_value)
                result = np.squeeze(prob)
                
                intr, unn = calMetric_iou(gt_value, result)
                inter = inter + intr
                unin = unin + unn

                valing_results['IoU'] = (inter * 1.0 / unin)

                val_bar.set_description(
                    desc='IoU: %.4f' % (  valing_results['IoU'],))

        # save model parameters
        # val_loss = valing_results['IoU']

        # if val_loss > mloss or epoch==1:
        #     mloss = val_loss
            torch.save(CDNet.state_dict(),  args.model_dir+'netCD_epoch_%d.pth' % (epoch))