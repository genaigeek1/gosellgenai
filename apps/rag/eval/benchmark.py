from datasets import load_dataset
import evaluate

dolly = load_dataset("databricks/databricks-dolly-15k")
sample = dolly["train"].select(range(5))

predictions = [ex["response"] for ex in sample]
references = [ex["response"] for ex in sample]

rouge = evaluate.load("rouge")
results = rouge.compute(predictions=predictions, references=references)

print("📊 ROUGE Evaluation Results:")
for k, v in results.items():
    print(f"{k}: {v:.4f}")