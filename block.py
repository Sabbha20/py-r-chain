import time

def mine_block(last_block, data):
    """
    Mines block based on last_block & data
    Args:
        last_block (Block): Previous Block
        data (str): Transactions data

    Returns:
        Block: returnes a mined block
    """
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f"{timestamp}-{last_hash}"
    
    return Block(timestamp, last_hash, hash, data)

def genesis():
    """
    Generate the genesis block
    Returns:
        Block: returns genesis block
    """
    return Block(1, "genesis_last_hash", "genesis_hash", [])

class Block:
    """_summary_
    Block: a unit of storage
    A single unit that stores transactions in a blockchain that supports cryptocurrencies.
    """
    
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        
    def __repr__(self):
        return (
                "Block(\n"
                f"timestamp:\t{self.timestamp},\n"
                f"last_hash:\t{self.last_hash},\n"
                f"hash:\t\t{self.hash},\n"
                f"data:\t\t{self.data}.\n"
                ")"
                )
    
def main():
    # block = Block("Hello, World!")
    # print(block)
    # print(f"block.py __name__:{__name__}")
    
    genesis_block = genesis()
    block = mine_block(genesis_block, "Data1")
    print(block)
    
if __name__ == "__main__":
    main()