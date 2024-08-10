import hashlib
import json

def crypto_hash(data):
    """
    This function returns a SHA-256 hash of the data.
    Args:
        data (any): 

    Returns:
        SHA-256 hash: 
    """
    return hashlib.sha256(json.dumps(data).encode("utf-8")).hexdigest()

def main():
    print(f"crypto_hash(data):\t{crypto_hash(["data"])}")
    

if __name__ == "__main__":
    main()