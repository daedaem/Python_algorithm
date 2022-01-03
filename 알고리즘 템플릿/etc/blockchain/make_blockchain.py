# 1
import hashlib
import time
import json


# print(hashlib.sha256('나는바보'.encode()).hexdigest()) # 64글자
# print(hashlib.sha256('나는바보,'.encode()).hexdigest())
# print(hashlib.sha256('나는바보.'.encode()).hexdigest())


class Block():
    def __init__(self, index, timestamp, data):
        # 블록 인덱스 값
        self.index = index
        # 블록 생성 시간
        self.timestamp = timestamp
        # 블록 저장된 데이터, 트랜젝션 등
        self.data = data
        # 이전 블록 해쉬값
        self.prevhash = 0
        self.nonce = 0
        # 현재 블록 해쉬 값
        self.hash = self.calHash()

    def calHash(self):
        # sha256에 들어갈 수 있는 데이터 타입은 byte이므로
        # string으로 변환 후 encode로 변환
        # 해쉬값을 16진수로 표현하기 위해 hexdigest
        return hashlib.sha256(str(self.index).encode() + str(self.data).encode() +
                              str(self.nonce).encode() + str(self.timestamp).encode() + str(
            self.prevhash).encode()).hexdigest()

    def mine(self, difficulty):
        ans = ["0"] * difficulty
        answer = "".join(ans)
        while str(self.hash)[:difficulty] != answer:
            self.nonce += 1
            self.hash = self.calHash()
        return self.hash


class BlockChain:
    def __init__(self, ):
        self.chain = []
        # 난이도 설정 : 0을 5개로 시작
        self.difficulty = 5
        self.createGenesis()

    def createGenesis(self):
        # time.titme()으로 timestamp값
        # time 모듈의 time() 함수는 현재 Unix timestamp을 소수로 리턴. 정수부는 초단위, 소수부는 마이크로(micro) 초단위.
        self.chain.append(Block(0, time.time(), 'Genesis Block'))

    # 생성된 블록 체인 추가 시,
    def addBlock(self, nBlock):
        # 이전 해시값과
        nBlock.prevhash = self.chain[len(self.chain) - 1].hash
        # 현재 해시값을
        nBlock.hash = nBlock.mine(self.difficulty)
        # 체인에 추가
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    # 체인 유효성 검사는
    def isValid(self):
        i = 1
        while i < len(self.chain):
            # 현재 블록의 해쉬 값과 계산된 해쉬값의 비교
            if self.chain[i].hash != self.chain[i].calHash():
                return False
            #  현재 블록이 가지고 있는 이전 블록해쉬값과 이전 블록에 저장되어 있는 해쉬값 비교
            if self.chain[i].prevhash != self.chain[i - 1].hash:
                return False
            i += 1
        return True


onion = BlockChain()
onion.addBlock(Block(len(onion.chain), time.time(), "2nd stranscation"))
onion.addBlock(Block(len(onion.chain), time.time(), {"3rd": "send 100BTC to Cho's wallet."}))
for block in onion.chain:
    # vars는 객체의 어트리뷰트(함수나 변수)를 돌려줌
    # python 객체를 JSON 문자열로 변환하기 위해서 dumps()함수 사용
    # indent 들여쓰기 정도
    print(json.dumps(vars(block), indent=2))

onion.chain[2].data = {"3rd": "send 1BTC to Cho's wallet."}
print('Chain is OK?', onion.isValid())

# 2
# import hashlib


# class WenivCoin:

#     def __init__(self, prevhash, transactions):
#         self.prevhash = prevhash
#         self.transactions = transactions
#         self.data = ' - 거래 : ' + '\n - 거래 : '.join(transactions) + '\n - 앞 블록 해쉬 ' + prevhash
#         self.blockhash = hashlib.sha256(self.data.encode()).hexdigest()

# t1 = '호준 -> 길동, 1 위니브코인'
# t2 = '길동 -> 춘향, 2 위니브코인'
# t3 = '춘향 -> 준호, 3 위니브코인'
# t4 = '길동 -> 호준, 1 위니브코인'
# t5 = '길동 -> 준호, 2 위니브코인'
# t6 = '길동 -> 준호, 3 위니브코인'

# 블록1 = WenivCoin('Initial_Text', [t1, t2])
# print(블록1.data)
# 블록1.blockhash
# 블록2 = WenivCoin(블록1.blockhash, [t3, t4])
# print(블록2.data)
# 블록3 = WenivCoin(블록2.blockhash, [t5, t6])
# print(블록3.data)


# 3
# # from hashlib import sha256

# # blockchain = []

# # def make_genesis_block():
# #     """첫 블록을 만듭니다."""
# #     data = 'Genesis'
# #     prev_hash = b''
# #     current_hash = make_hash(data, prev_hash)
# #     blockchain.append((data, prev_hash, current_hash))

# # def make_hash(data: str, prev_hash: bytes) -> bytes:

# #     """해시 생성"""
# #     return sha256(data.encode() + prev_hash).digest()

# # def add_block(data: str):
# #     """블록을 블록체인에 추가"""
# #     _, _, prev_hash = blockchain[-1]
# #     current_hash = make_hash(data, prev_hash)
# #     blockchain.append((data, prev_hash, current_hash))

# # def show_blockchain():
# #     """블록 체인을 보여줌"""
# #     for i, (data, prev_hash, current_hash) in enumerate(blockchain):
# #         print(f'블록 {i}|n{data}|n{prev_hash.hex()}|n{current_hash.hex()}')

# # def verify_blockchain():
# #     """블록체인을 검증"""
# #     for i in range(1, len(blockchain)):
# #         data, prev_hash, current_hash = blockchain[i]
# #         last_data, last_prev_hash, last_current_hash = blockchain[i -1 ]
# #         if prev_hash != last_current_hash:
# #             print(f"블록 {i} 이전 해시 != 블록 {i-1} 현해시. |n"f"{prev_hash.hex()} != |n{last_current_hash.hex()}")
# #             return False
# #         if last_current_hash != (temp := make_hash(last_data, last_prev_hash)):
# #             print(f"블록 {i-1} 검증실패. |n" f"{last_current_hash.hex()} != |n{temp.hex()}")
# #             return False
# #         if current_hash != (temp := make_hash(last_data, prev_hash)):
# #             print(f"블록 {i} 검증실패. |n" f"{current_hash.hex()} != |n{temp.hex()}")
# #             return False
# #     return True

# # make_genesis_block()
# # add_block('나는미남이다')
# # add_block('진짜미남이다')
# # add_block('아님말고')
# # show_blockchain()
# # print()
# # print(verify_blockchain())


