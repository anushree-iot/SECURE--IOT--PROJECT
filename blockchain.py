import hashlib
import time
import random

class Block:
    def __init__(self, index, sensor_data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.sensor_data = sensor_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.sensor_data) + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_first_block()]

    def create_first_block(self):
        return Block(0, "Genesis Block - System Start", "0")

    def add_block(self, sensor_data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), sensor_data, last_block.hash)
        self.chain.append(new_block)

    def check_security(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

print("--- Secure IoT Data Logger Started ---")
my_chain = Blockchain()

for i in range(5):
    temp = random.uniform(25.0, 35.0)
    humidity = random.uniform(40.0, 70.0)
    data = f"Temp: {temp:.2f}C, Humidity: {humidity:.2f}%"
    my_chain.add_block(data)
    print(f"Sensor Data Logged: {data}")
    time.sleep(1)

print("\n--- Blockchain Data ---")
for block in my_chain.chain:
    print(f"Block {block.index} | Hash: {block.hash[:15]}... | Data: {block.sensor_data}")

print("\nSecurity Check:", "SAFE - Koi Data Change Nahi Hua ✅" if my_chain.check_security() else "HACKED! Data Badla Gaya ❌")
