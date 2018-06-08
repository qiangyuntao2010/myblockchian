#!/usr/bin/env python
#coding=utf-8
import datetime
import hashlib
class DaDaBlockCoin:
    #index 索引，timestamp 时间戳，data 交易记录，self_hash交易hash,last_hash,上个hash
	def __init__(self,idex,timestamp,data,last_hash):
        	self.idex = idex
        	self.timestamp = timestamp
        	self.data = data
        	self.last_hash = last_hash
        	self.self_hash=self.hash_DaDaBlockCoin()


    	def hash_DaDaBlockCoin(self):
        	sha = hashlib.md5()
		#加密算法,这里可以选择sha256,sha512,为了打印方便，所以选了md5
        	#对数据整体加密
        	datastr = str(self.idex)+str(self.timestamp)+str(self.data)+str(self.last_hash)
        	sha.update(datastr.encode("utf-8"))
        	return sha.hexdigest()

def create_first_DaDaBlock():  # 创世区块
	return DaDaBlockCoin(0, datetime.datetime.now(), "qiangyuntao", "0")


# last_block,上一个区块
def create_money_DadaBlock(last_block):  # 其它块
	this_idex = last_block.idex + 1  # 索引加1	
	this_timestamp = datetime.datetime.now()
    	this_data = "love dada" + str(this_idex)  # 模拟交易数据
    	this_hash = last_block.self_hash  # 取得上一块的hash
	return DaDaBlockCoin(this_idex, this_timestamp, this_data, this_hash)


DaDaBlockCoins = [create_first_DaDaBlock()]  # 区块链列表，只有一个创世区块
nums = 1000
head_block = DaDaBlockCoins[0]
print(head_block.idex, head_block.timestamp, head_block.self_hash, head_block.last_hash)
for i in range(nums):
    	dadaBlock_add = create_money_DadaBlock(head_block)  # 创建一个区块链的节点
    	DaDaBlockCoins.append(dadaBlock_add)
    	head_block = dadaBlock_add
    	print(dadaBlock_add.idex, dadaBlock_add.timestamp, dadaBlock_add.self_hash, dadaBlock_add.last_hash)

