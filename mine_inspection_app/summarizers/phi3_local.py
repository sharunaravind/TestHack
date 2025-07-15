from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# You can change this to any compatible HuggingFace instruct model
MODEL_NAME = "microsoft/phi-3-mini-4k-instruct"

print("⏳ Loading local Phi-3 model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"  # Automatically use GPU if available
)
summarizer = pipeline("text-generation", model=model, tokenizer=tokenizer)

def summarize_with_phi3(text):
    """
    Summarizes text using Phi-3 locally.
    """
    prompt = f"<|system|>\nYou are an expert assistant that summarizes inspection logs.\n<|user|>\nSummarize this:\n{text}\n<|assistant|>"
    result = summarizer(prompt, max_new_tokens=300, do_sample=False, truncation=True)[0]["generated_text"]
    
    # Cut the generated text cleanly (after assistant marker)
    return result.split("<|assistant|>")[-1].strip()
