import wandb

def init_wandb(project="local-rag"):
    wandb.init(project=project)

def log_metrics(metrics: dict):
    wandb.log(metrics)