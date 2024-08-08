#!/usr/bin/env python3

import time
import requests
import argparse

def get_hf_block(hf_timestamp):
    ts = hf_timestamp
    block = requests.get(f"https://kmd.explorer.dexstats.info/insight-api-komodo/status").json()["info"]["blocks"]
    print(f"Current block: {block}")
    now = int(time.time())
    sec_until_hf = int(ts) - now
    print(f"Seconds until HF: {sec_until_hf}\n")
    estimated_blocks = []
    last_checkpoint_block = 0
    last_checkpoint_blocktime = 0
    for i in range(1,3):
        print(f"==================== {i*30} days =========================")
        block_range = i * 30 * 60 * 24 # 30 days
        print(f"Blocks: {block_range}")
        checkpoint_block = block - block_range
        print(f"Checkpoint block: {checkpoint_block}")
        checkpoint_blockhash = requests.get(f"https://kmdexplorer.io/insight-api-komodo/block-index/{checkpoint_block}").json()["blockHash"]
        checkpoint_blocktime = requests.get(f"https://kmdexplorer.io/insight-api-komodo/block/{checkpoint_blockhash}").json()["time"]
        print(f"Checkpoint blocktime: {checkpoint_blocktime}")
        sec_range = now - checkpoint_blocktime
        print(f"Seconds: {sec_range} ({sec_range / 60 / 60 / 24} days)")
        sec_per_block_average = round(sec_range / block_range, 3)
        print(f"Seconds per block average over {i*30} days: {sec_per_block_average}")
        estimated_blocks_until_hf = int(sec_until_hf / sec_per_block_average)
        print(f"Estimated blocks until HF: {estimated_blocks_until_hf}")
        estimated_hf_block = block + estimated_blocks_until_hf
        print(f"Estimated HF block: {estimated_hf_block} (over {i*30} days)")
        estimated_blocks.append(estimated_hf_block)
        if last_checkpoint_block != 0:
            sec_range = last_checkpoint_blocktime - checkpoint_blocktime
            blocks = last_checkpoint_block - checkpoint_block
            print(f"Slice time: {sec_range} ({sec_range / 60 / 60 / 24} days)")
            sec_per_block_average = round(sec_range / blocks, 3)
            print(f"Slice sec per block average: {sec_per_block_average}\n")
        last_checkpoint_blocktime = checkpoint_blocktime
        last_checkpoint_block = checkpoint_block
    estimated_blocks.sort()
    print(f"HF estimated block range: {min(estimated_blocks)} - {max(estimated_blocks)}")
    print(f"HF Estimated block average: {round(sum(estimated_blocks) / len(estimated_blocks))}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimates hardfork block for a given future timestamp.')
    parser.add_argument('hf_timestamp', type=str, help='Hardfork timestamp')
    # Parse the argument
    args = parser.parse_args()
    get_hf_block(args.hf_timestamp)
