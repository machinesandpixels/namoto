# Namoto Blockchain
namoto_blockchain = []
namoto_length = len(namoto_blockchain)

# The individual blocks in the blockchain
namoto_block = {}

pending_transactions = []

# Add transaction to block
def add_to_block(transaction_amount, last_transaction=[1]):

    if namoto_length < 1:
        last_transaction = 0
        
    namoto_blockchain.append([last_transaction, transaction_amount])

# Get last transaction of block
def get_last_block():
    """ Returns last blockchain value """
    if namoto_length < 1:
        return None

    return namoto_blockchain[-1]


def verify_chain():
    """ Checks if previous blocks have been unchanged """

    block_index = 0
    is_unchanged = True

    if namoto_length < 1:
        print('Blockchain is empty!')
        return None

    for block in namoto_blockchain:

        if block[0] == namoto_blockchain[block_index -1]:
            is_unchanged = True
            block_index += 1

        else:
            is_unchanged = False
            break

        return is_unchanged

def mine_block():
    pass

def add_transaction(sender, receiver, amount=1.0):
    pass
