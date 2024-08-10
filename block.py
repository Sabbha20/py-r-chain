class Block:
    """_summary_
    Block: a unit of storage
    A single unit that stores transactions in a blockchain that supports cryptocurrencies.
    """
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return f"Block({self.data})"
    
def main():
    block = Block("Hello, World!")
    print(block)
    print(f"block.py __name__:{__name__}")
    
if __name__ == "__main__":
    main()