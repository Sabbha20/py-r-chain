from backend.blockchain.block import Block #, genesis, mine_block

class Blockchain:
    """
    Blockchain: A public ledger of transaction
    Implemented as lists of blocks, datasets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]
    
    def add_block(self, data):
        # self.chain.append(Block(data))
        self.chain.append(Block.mine_block(self.chain[-1], data))
        
    def __repr__(self):
        return f"Blockchain({self.chain})"
    
def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)
    print(f"blockchain.py __name__:{__name__}")
        

if __name__ == "__main__":
    main()  # call main() when run directly