# run vllm with openai compatible api
python -m vllm.entrypoints.openai.api_server --model mosaicml/mpt-30b-chat --tokenizer mosaicml/mpt-30b --tensor-parallel-size 4 --worker-use-ray --host 0.0.0.0 --port 8000

# it requires shm > 30% RAM, otherwise it will raise SIGBUS error
docker run --rm -it --gpus all --shm-size=80gb -p 8000:8000 -v /home/keming/.cache:/root/.cache kemingy/vllm:latest
