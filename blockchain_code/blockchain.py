# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:02:44 2017

@author: Mike
"""

class Blockchain(object):
    """ Blockchain 类负责管理链。
    它用来存储交易信息，也有一些帮助方法用来将新区块添加到链中。
    """
    def __init__(self):
        # 存储区块链
        self.chain = []
        # 存储交易信息
        self.current_transactions = []
        
    def new_block(self):
        # Creates a new Block and adds it to the chain
        
        pass
    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
         """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
    
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
    
"""
每个新区块都包含上一个区块的哈希。这一重要概念使得区块链的不可变性成为可能：如果攻击者篡改了链中的前序区块，所有的后续区块的哈希都是错的。
"""    
sample_block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}    