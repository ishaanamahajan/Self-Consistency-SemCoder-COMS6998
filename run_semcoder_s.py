from transformers import AutoModelForCausalLM, AutoTokenizer

# Load SemCoder S
model_name = "semcoder/semcoder_s"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

