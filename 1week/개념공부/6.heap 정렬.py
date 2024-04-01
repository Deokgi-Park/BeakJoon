def heapify(arr, n, i):
    largest = i  # 루트를 가장 큰 값으로 설정
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 자식이 루트보다 크다면 largest를 왼쪽 자식으로 변경
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 루트보다 크다면 largest를 오른쪽 자식으로 변경
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 변경되었다면 해당 위치의 노드와 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 변경된 위치를 기준으로 다시 heapify
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 최대 힙을 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙 정렬 수행
    for i in range(n - 1, 0, -1):
        # 현재 최대값(루트)을 마지막 요소와 교환
        arr[i], arr[0] = arr[0], arr[i]
        # 힙 크기를 줄여서 마지막 요소를 제외하고 다시 heapify
        heapify(arr, i, 0)

# 예시
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("정렬된 배열은", arr)