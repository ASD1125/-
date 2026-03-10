dir = East
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
while True:
	x,y = get_pos_x(),get_pos_y()
	a,b = measure()
	if x == a and y == b:
		harvest()
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, substance)
		continue
	if dir == East:
		if can_move(South):
			dir = South
			move(South)
		elif can_move(East):
			move(East)
		elif can_move(North):
			dir = North
			move(North)
		elif can_move(West):
			dir = West
			move(West)
	elif dir == South:
		if can_move(West):
			dir = West
			move(West)
		elif can_move(South):
			move(South)
		elif can_move(East):
			dir = East
			move(East)
		elif can_move(North):
			dir = North
			move(North)
	elif dir == West:
		if can_move(North):
			dir = North
			move(North)
		elif can_move(West):
			move(West)
		elif can_move(South):
			dir = South
			move(South)
		elif can_move(East):
			dir = East
			move(East)
	elif dir == North:
		if can_move(East):
			dir = East
			move(East)
		elif can_move(North):
			move(North)
		elif can_move(West):
			dir = West
			move(West)
		elif can_move(South):
			dir = South
			move(South)
		
				