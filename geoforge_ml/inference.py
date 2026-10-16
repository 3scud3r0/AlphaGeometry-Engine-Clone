"""Bounded greedy neural generation. Outputs are uncertified candidates."""
from geoforge_upgrade_suite.neural_baseline import require_torch

def greedy_tokens(model,start_ids,max_new_tokens=32):
    require_torch()
    import torch
    if max_new_tokens<0:raise ValueError("negative token budget")
    state=torch.tensor([start_ids],dtype=torch.long)
    model.eval()
    with torch.no_grad():
        for _ in range(max_new_tokens):
            limit=model.config.context
            logits,_=model(state[:,-limit:])
            token=logits[:,-1,:].argmax(dim=-1,keepdim=True)
            state=torch.cat((state,token),dim=1)
    return state[0].tolist()
