import time
from backend.util.crypto_hash import crypto_hash

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
    
    def to_dict(self):
        """
        Convert the Block into a dictionary format.
        """
        return {
            'timestamp': self.timestamp,
            'last_hash': self.last_hash,
            'hash': self.hash,
            'data': self.data
        }
    
    @staticmethod
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
        hash = crypto_hash(last_block.to_dict(), data) #f"{timestamp}-{last_hash}"
        
        return Block(timestamp, last_hash, hash, data)


    @staticmethod
    def genesis():
        """
        Generate the genesis block
        Returns:
            Block: returns genesis block
        """
        return Block(1, "genesis_last_hash", crypto_hash("genesis_hash"), [])
    
def main():
    # block = Block("Hello, World!")
    # print(block)
    print(f"block.py __name__:\t{__name__}")
    
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "Block1-Data")
    print(block)

# main()
if __name__ == "__main__":
    main()