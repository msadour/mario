class Character:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Get the name to put it in the field.
        :return:
        """
        return self.name

class Mario(Character):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

    def update_position(self, new_position):
        """
        Update the current position of Mario after a mouvement.
        :param new_position:
        :return:
        """
        self.position = new_position

class Princess(Character):
    def __init__(self, name):
        super().__init__(name)

class Game:
    def __init__(self, grid_size, mario, princess):
        self.mario = mario
        self.princess = princess
        self.index_max = grid_size - 1 #I use this variable to avoid to an index out of range
        self.win = False
        if grid_size == 3:
            self.field = ['--' + mario.get_name(),'-x-','-' + princess.get_name() +'-']
        # elif grid_size == 5:
        #     pass #later
        # else:
        #     pass

    def __repr__(self):
        return '\n'.join(self.field)

    def get_possibilities(self):
        """
        Return the possibility of directions for the current position of Mario.
        :return: possibilities
        """
        possibilities = []

        if self.mario.position[1] < self.index_max and self.check_obstacle_in_direction('RIGHT'):
            possibilities.append('RIGHT')

        if self.mario.position[1] > 0 and self.check_obstacle_in_direction('LEFT'):
            possibilities.append('LEFT')

        if self.mario.position[0] > 0 and self.check_obstacle_in_direction('UP'):
            possibilities.append('UP')

        if self.mario.position[0] < self.index_max and self.check_obstacle_in_direction('DOWN'):
            possibilities.append('DOWN')

        return possibilities

    def get_next_element(self, new_position):
        """
        Check which element is in the next position (in the selected direction).
        :param new_position:
        :return:
        """
        return self.field[new_position[0]][new_position[1]]

    def check_obstacle_in_direction(self, direction):
        """
        Check if the next element is an obstacle for avoid to move wrongly.
        :param direction:
        :return:
        """
        if direction == 'RIGHT':
            index_to_the_right = self.mario.position[1] + 1
            if self.get_next_element((self.mario.position[0], index_to_the_right)) != 'x':
                return True
        elif direction == 'LEFT':
            index_to_the_left = self.mario.position[1] - 1
            if self.get_next_element((self.mario.position[0], index_to_the_left)) != 'x':
                return True
        elif direction == 'UP':
            index_to_up = self.mario.position[0] - 1
            if self.get_next_element((index_to_up, self.mario.position[1])) != 'x':
                return True
        elif direction == 'DOWN':
            index_to_the_down = self.mario.position[0] + 1
            if self.get_next_element((index_to_the_down, self.mario.position[1])) != 'x':
                return True

    def update_field(self, old_position , new_position):

        def update_string_in_field(level, new_string, index):

            list_field = list(level)
            list_field[index] = new_string
            return ''.join(list_field)

        self.field[old_position[0]] = update_string_in_field(self.field[old_position[0]], '-', old_position[1])
        self.field[new_position[0]] = update_string_in_field(self.field[new_position[0]], self.mario.get_name(), new_position[1])

    def move_mario(self, mario, direction, test=False):
        """
        Move Mario to a direction.
        :param mario:
        :param direction:
        :param test:
        :return:
        """
        old_position = mario.position

        if direction == 'RIGHT':
            index_to_the_right = old_position[1] + 1
            new_position = (old_position[0], index_to_the_right)
        elif direction == 'LEFT':
            index_to_the_left = old_position[1] - 1
            new_position = (old_position[0], index_to_the_left)
        elif direction == 'UP':
            index_to_up = old_position[0] - 1
            new_position = (index_to_up, old_position[1])
        elif direction == 'DOWN':
            index_to_the_down = old_position[0] + 1
            new_position = (index_to_the_down, old_position[1])

        if self.get_next_element(new_position) == 'p':
            self.win = True
        else:
            if self.get_next_element(new_position) != 'x':
                self.update_field(old_position, new_position)
                self.mario.update_position(new_position)
