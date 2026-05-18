import torch

# 디바이스 설정
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"사용 중인 디바이스: {device}")

# 1. 텐서와 모델이 실제로 MPS에 올라갔는지 확인
x = torch.randn(5, 5).to(device)
print(f"데이터가 위치한 곳: {x.device}")  # 출력에 'mps:0'이 포함되어야 함

# 2. 현재 할당된 GPU(MPS) 메모리 확인
if device.type == 'mps':
    allocated_memory = torch.mps.current_allocated_memory() / (1024 ** 2)
    print(f"현재 할당된 GPU 메모리: {allocated_memory:.2f} MB")