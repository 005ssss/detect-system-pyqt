import torch

#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#model.load_state_dict(torch.load(save_path),map_location=device)

state_dict = torch.load('C:/Users/HP/Desktop/centernet-pytorch-main/logs/ep071-loss1.658-val_loss1.688.pth')
state_dict = torch.load('C:/Users/HP/Desktop/centernet-pytorch-main/logs/ep071-loss1.658-val_loss1.688.pth', map_location="cpu")
#state_dict = torch.load('pytorch_model.bin', map_location="cpu")

torch.save(state_dict, 'C:/Users/HP/Desktop/centernet-pytorch-main/logs/ep071-loss1.658-val_loss1.688_new.pth', _use_new_zipfile_serialization=False)
#torch.save(state_dict, 'pytorch_model.bin', _use_new_zipfile_serialization=False)