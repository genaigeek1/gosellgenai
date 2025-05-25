import matplotlib.pyplot as plt

before = {"rouge1": 0.21, "rougeL": 0.18}
after = {"rouge1": 0.35, "rougeL": 0.30}

labels = list(before.keys())
before_scores = list(before.values())
after_scores = list(after.values())

x = range(len(labels))
width = 0.4

plt.bar(x, before_scores, width=width, label='Before')
plt.bar([i + width for i in x], after_scores, width=width, label='After')

plt.xticks([i + width/2 for i in x], labels)
plt.ylabel('Score')
plt.title('RAG Performance: Before vs After')
plt.legend()
plt.tight_layout()
plt.savefig("rag_eval_chart.png")
plt.show()