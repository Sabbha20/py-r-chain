import hashlib
import json

def crypto_hash(*data):
    """
    Return a SHA-256 hash of the given arguments.
    Args:
        *data: Variable length argument list, each argument can be of any type.

    Returns:
        SHA-256 hash as a hex string.
    """
    # return hashlib.sha256(json.dumps(data).encode("utf-8")).hexdigest()
    stringified_args = sorted(map(lambda d: json.dumps(d, sort_keys=True), data))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('data'):\t{crypto_hash('data')}")
    print(f"crypto_hash(['data']):\t{crypto_hash(['data'])}")

if __name__ == "__main__":
    main()