
class MinHeap(object):
    def __init__(self):
        self._list = []

    def heapify_down(self, index):
        while self._has_left_child(index):
            item = self._list[index]
            smaller_child_index = self._get_left_child_index(index)
            if self._has_right_child(index) and self._get_left_child(index) > self._get_right_child(index):
                smaller_child_index = self._get_right_child_index(index)
            if item > self._list[smaller_child_index]:
                self._swap(index, smaller_child_index)
                index = smaller_child_index
            else:
                break

            # if self._has_left_child(index) and self._get_left_child(index) < item:
            #     self._swap(index, self._get_left_child_index(index))
            #     index = self._get_left_child_index(index)
            #     done = False
            # elif self._has_right_child(index) and self._get_right_child(index) < item:
            #     self._swap(index, self._get_right_child_index(index))
            #     index = self._get_right_child_index(index)
            #     done = False
        # while self._child_is_less_than(index):

    def update(self, index, old_value, new_value):
        if old_value > new_value:
            self.heapify_up(index)
        if old_value < new_value:
            self.heapify_down(index)



    def heapify_up(self, index):
        while self._parent_is_greater_than(index):
            item = self._list[index]
            self._swap(index, self._get_parent_index(index))
            index = self._get_parent_index(index)

    def _parent_is_greater_than(self, index):
        if not self._has_parent(index):
            return False
        item = self._list[index]
        return item < self._list[self._get_parent_index(index)]


    def insert(self, item):
        self._list.append(item)
        self.heapify_up(len(self._list) - 1)

    def pop(self):
        self._swap(0, len(self._list) - 1)
        if len(self._list) > 0:
            output = self._list.pop()
        if len(self._list) > 0:
            self.heapify_down(0)
        return output

    def _swap(self, index1, index2):
        temp = self._list[index1]
        self._list[index1] = self._list[index2]
        self._list[index2] = temp

        #for this implementation only
        self._list[index1].index_label = index1
        self._list[index2].index_label = index2

    @property
    def size(self):
        return len(self._list)



    def _get_right_child_index(self, index): return index * 2 + 2
    def _get_left_child_index(self, index): return index * 2 + 1
    def _get_parent_index(self, index): return (index - 1) / 2

    def _get_right_child(self, index): return self._list[self._get_right_child_index(index)]
    def _get_left_child(self, index): return self._list[self._get_left_child_index(index)]
    def _get_parent(self, index): return self._list[self._get_parent_index(index)]

    def _has_right_child(self, index): return self._get_right_child_index(index) < len(self._list)
    def _has_left_child(self, index): return self._get_left_child_index(index) < len(self._list)
    def _has_parent(self, index): return self._get_parent_index(index) >= 0
