def hanoi_tower(discs, from_rod, to_rod, aux_rod, move_count):
    if discs == 1:
        print(f"Move disc 1 from {from_rod} to {to_rod}")
        return move_count + 1
    
    move_count = hanoi_tower(discs - 1, from_rod, aux_rod, to_rod, move_count)
    print(f"Move disc {discs} from {from_rod} to {to_rod}")
    move_count += 1
    move_count = hanoi_tower(discs - 1, aux_rod, to_rod, from_rod, move_count)
    
    return move_count

# 테스트
discs = 3
from_rod = 'A'
to_rod = 'C'
aux_rod = 'B'
move_count = 0
print(f"Solving Tower of Hanoi with {discs} discs...")
total_moves = hanoi_tower(discs, from_rod, to_rod, aux_rod, move_count)
print(f"Total moves: {total_moves}")
