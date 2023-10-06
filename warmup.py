import sys

from huggingface_hub import snapshot_download

model = "meta-llama/Llama-2-7b-hf"

if len(sys.argv) == 2:
    model = sys.argv[1]

print(f"warmup with {model}")
snapshot_download(model)
