# vLLM env

You can try the docker image directly:

```bash
# it requires shm > 30% RAM, otherwise it will raise SIGBUS error
docker run --rm -it --entrypoint sh --gpus all --shm-size=80gb -p 8000:8000 kemingy/vllm:latest
```

Start a LLM service with tensor-parallel:

```bash
python -m vllm.entrypoints.openai.api_server \
    --model mosaicml/mpt-30b-chat \
    --tokenizer mosaicml/mpt-30b \
    --tensor-parallel-size 4 \
    --worker-use-ray \
    --host 0.0.0.0 \
    --port 8000
```

## Test

Run a single query with the OpenAI Python client:

```bash
python openai_client.py
```

## Build the docker image

```bash
docker build -t vllm .
```

To use a specific vllm version:

```bash
docker build --build-arg commit=66c54aa -t vllm .
```
