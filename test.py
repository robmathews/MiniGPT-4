from transformers import LlamaForCausalLM, LlamaTokenizer

tokenizer = LlamaTokenizer.from_pretrained("../Llama-7B")
model = LlamaForCausalLM.from_pretrained("../Llama-7B")
