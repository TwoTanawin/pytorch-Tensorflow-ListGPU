import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"PyTorch is using {torch.cuda.get_device_name()} GPU")
else:
    device = torch.device("cpu")
    print("PyTorch is using CPU")
