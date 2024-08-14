from backend.blockchain.blockchain import Blockchain
import time
from backend.config import SECONDS


time_list = []

def average_block_rate(block_chain: Blockchain, no_of_executions: int):
    for i in range(no_of_executions):
        start_time = time.time_ns()
        block_chain.add_block(i)
        end_time = time.time_ns()
        
        time_to_mine = (end_time - start_time) / SECONDS
        time_list.append(time_to_mine)
        
        avg_time = sum(time_list)/len(time_list)
        
        print("="*50+"\n")
        print(f"Block Difficulty Level:\t\t{block_chain.chain[-1].difficulty}")
        print(f"Block Nonce Value:\t\t{block_chain.chain[-1].nonce}")
        print(f"Time to mine new block:\t\t{time_to_mine:.6f} sec")
        print(f"Average time to add block:\t{avg_time:.6f} sec\n")
        print("="*50+"\n")
        
bl_chain = Blockchain()
NUMBER_OF_EXECUTION = 10

average_block_rate(bl_chain, NUMBER_OF_EXECUTION) 