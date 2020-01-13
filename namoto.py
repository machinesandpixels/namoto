# Initialized the namoto block
namoto_block = []
block_length = len(namoto_block)

# Add transaction to block
def add_to_block(transaction_amount, last_transaction=[1]):

    if block_length < 1:
        last_transaction = 0
        
    namoto_block.append([last_transaction, transaction_amount])

# Get last transaction of block
def get_last_block():
    """ Returns last blockchain value """
    if block_length < 1:
        return None

    return namoto_block[-1]


def verify_chain():
    """ Checks if previous blocks have been unchanged """

    block_index = 0
    is_unchanged = True

    if block_length < 1:
        print('Blockchain is empty!')
        return None

    for block in namoto_block:

        if block[0] == namoto_block[block_index -1]:
            is_unchanged = True
            block_index += 1

        else:
            is_unchanged = False
            break

        return is_unchanged


