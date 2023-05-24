from Map import *

def main():
    my_map = Map()
    my_map.createFirstLayer()

    #nx.draw_networkx(my_map.firstLayer)
    print(my_map.findPath((3, 7), (42, 53)))


main()


