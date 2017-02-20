import sys
from minheap import MinHeap


def get_graph_from_file(filename):
    graph_heap = MinHeap()


    with open(filename, 'r') as f:
        for line in f:
            node = Node()
            split_line = line.split()
            node.g_num = int(split_line[0])
            #index label keeps track of where this node is in the heap's array
            node.index_label = graph_heap.size
            for edge in split_line[1:]:
                target, length = edge.split(',')
                node.edges.append({'target':int(target), 'length':int(length)})
            graph_heap.insert(node)
    return graph_heap

def dijkstra(graph_heap, start):
    #make a list of 0s that will ultimately hold the output--the indices of the list will represent the node number from the original graph for fast lookup
    shortest_path_list = [0] * (graph_heap.size + 1)
    for node in graph_heap._list:
        #put each node into index of shortest_path_list that corresponds to the node's number in the original graph (original graph starts with 1 rather than 0)
        shortest_path_list[node.index_label + 1] = node

    #set the starting point dijkstra score to 0
    shortest_path_list[start].d_num = 0

    while graph_heap.size > 0:
        new_node = graph_heap.pop()
        new_node.explored = True
        print("processing node number: " + str(new_node.g_num))
        #print("before processing edges, 92 is at " + str(shortest_path_list[92].index_label))
        for edge in new_node.edges:
            target = shortest_path_list[edge['target']]
            if not target.explored:
                heap_location = target.index_label
                old_d_num = target.d_num
                new_d_num = new_node.d_num + edge['length']
                if new_d_num < old_d_num:
                    target.d_num = new_d_num
                    #print("updated " + str(target.g_num) + " to have distance of " + str(target.d_num))
                    #print("target is " + str(target.g_num) + " index is " +str(heap_location) + " old value: " + str(old_d_num) + " new value: " + str(new_d_num))
                    graph_heap.update(heap_location, old_d_num, new_d_num)
                    #print("index changed to " + str(target.index_label))
        #print("after processing edges, 92 is at " + str(shortest_path_list[92].index_label))

    return shortest_path_list


class Node(object):
    g_num = 0
    d_num = 1000000
    index_label = 0
    explored = False
    def __init__(self):
        self.edges = []

    def __cmp__(self, other):
        if (self.d_num > other.d_num):
            return 1
        elif (self.d_num < other.d_num):
            return -1
        else:
            return 0



graph_heap = get_graph_from_file(sys.argv[1])
shortest_path_list = dijkstra(graph_heap, 1)
#for node in shortest_path_list[1:]:
    #print("shortest path for " + str(node.g_num) + " is " + str(node.d_num))

answer_string = ''
test_values = [7,37,59,82,99,115,133,165,188,197]
for num in test_values:
    answer_string = answer_string + str(shortest_path_list[num].d_num) + ','
print(answer_string)

# print(graph_heap.size)
# graph_heap.pop()
# for node in graph_heap._list:
#     print("node number: " + str(node.g_num))
#     print("index number: ") + str(node.index_label)
#     for edge in node.edges:
#         print(edge)



# testList = [1,2,3,4,5]
# heap = MinHeap()
#
# heap.insert(5)
# heap.insert(4)
# heap.insert(6)
# heap.insert(2)
# heap.insert(3)
# heap.insert(1)
#
# heap.pop()
# print(heap._list)
# heap.pop()
# print(heap._list)
# heap.pop()
# print(heap._list)
# heap.pop()
# print(heap._list)
# heap.pop()
# print(heap._list)
# heap.pop()
# print(heap._list)
# heap.pop()




# node1 = Node()
# node2 = Node()
# node1.d_num = 10
# print("d num of node 1 is: " + str(node1.d_num))
# print("d num of node 2 is: " + str(node2.d_num))
# print(node1 == node2)

#get_graph_from_file()


    # def _child_is_less_than(self, index):
    #     if not self._has_left_child(index) and not self._has_right_child(index):
    #         return False
    #     right_child = self._get_right_child(index)
    #     left_child = self._get_left_child(index)
    #     item = self._list[index]
    #     return (right_child < item) or (left_child < item)
