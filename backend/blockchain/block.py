import time
from backend.util.crypto_hash import crypto_hash
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': "genesis_last_hash",
    'hash': crypto_hash("genesis_hash"),
    'data': [], 
    'difficulty': 3,
    'nonce': "genesis_nonce"
}

class Block:
    """_summary_
    Block: a unit of storage
    A single unit that stores transactions in a blockchain that supports cryptocurrencies.
    """
    
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        
    def __repr__(self):
        return (
                "Block(\n"
                f"timestamp:\t{self.timestamp},\n"
                f"last_hash:\t{self.last_hash},\n"
                f"hash:\t\t{self.hash},\n"
                f"data:\t\t{self.data}.\n"
                f"difficulty:\t{self.difficulty}.\n"
                f"nonce:\t\t{self.nonce}.\n"
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
            'data': self.data,
            'difficulty': self.difficulty,
            'nonce': self.nonce
        }
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mines block based on last_block & data
        Args:
            last_block (Block): Previous Block
            data (str): Transactions data

        Returns:
            Block: returnes a mined block, until a block hash is found that 
            meets the leading 0's proof of work requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp) # last_block.difficulty
        nonce = 0
        hash = crypto_hash(last_block.to_dict(), data, timestamp, difficulty, nonce) #f"{timestamp}-{last_hash}"
        while hash[0:difficulty] != "0" * difficulty:
            nonce += 1
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            timestamp = time.time_ns()
            hash = crypto_hash(last_block.to_dict(), data, timestamp, difficulty, nonce)
        
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)


    @staticmethod
    def genesis():
        """
        Generate the genesis block
        Returns:
            Block: returns genesis block
        """
        # return Block(
        #     GENESIS_DATA['timestamp'],  # 1, 
        #     GENESIS_DATA['last_hash'],  # "genesis_last_hash", 
        #     GENESIS_DATA['hash'],       # crypto_hash("genesis_hash"), 
        #     GENESIS_DATA['data']        # []
        #     )
        return Block(**GENESIS_DATA)
    
    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Adjust difficulty based on time taken to mine last block
            - Increses the difficulty, if blocks are mined quickly
            - Decreases the difficulty, if blocks are mined slowly
        Args:
            last_block (Block): Previous Block
            new_timestamp (int): timestamp of new block
        Returns:
            int: returns adjusted difficulty
        """
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        
        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        
        return 1
    
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