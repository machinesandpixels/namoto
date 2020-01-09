# Initialized the namoto block
namoto_block = []

# Add transaction to the block
def add_to_block(transaction_amount, last_transaction=[1]):
    
    namoto_block.append([last_transaction, transaction_amount])

# Get last transaction of our block
def get_last_block():
    """ Returns last blockchain value """
    return namoto_block[-1]
