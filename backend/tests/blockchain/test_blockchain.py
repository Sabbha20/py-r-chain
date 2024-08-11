from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    b1 = Blockchain()
    
    assert b1.chain[0].hash == GENESIS_DATA['hash']
    
def test_add_block():
    b1 = Blockchain()
    data = "test-data-1"
    b1.add_block(data)
    
    assert b1.chain[-1].data == data