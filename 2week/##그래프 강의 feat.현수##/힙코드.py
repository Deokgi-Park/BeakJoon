def heapify(arr, n, i):
    largest = i  # 최대값을 현재 노드로 설정
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # 왼쪽 자식 노드가 힙의 크기 내에 있고 현재 노드보다 크면 교환
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # 오른쪽 자식 노드가 힙의 크기 내에 있고 현재 노드보다 크면 교환
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # 현재 노드가 최대값이 아니면 교환하고 재귀적으로 힙 구성
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # 배열의 중간부터 역순으로 heapify를 실행하여 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# 예시
arr = [12, 11, 13, 5, 6, 7]
build_max_heap(arr)
print("Max Heap:", arr)