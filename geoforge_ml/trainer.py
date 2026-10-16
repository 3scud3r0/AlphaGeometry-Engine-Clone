"""Training baseline; no pretrained AG2/Gemini weights are bundled."""
from geoforge_upgrade_suite.neural_baseline import (
    NeuralTrainer,TrainingConfig,ProofTextDataset,TransformerConfig,require_torch
)
__all__=["NeuralTrainer","TrainingConfig","ProofTextDataset","TransformerConfig","require_torch"]
