#    opposite_of_n = 's'
#    opposite_of_s = 'n'
#    opposite_of_w = 'e'
#    opposite_of_e = 'w'
#
#    graph.add_vertex(player.current_room.id)
#    for direction in player.current_room.get_exits():
#        graph.add_edge(player.current_room.id, direction)
#    x = 0
#    counter = 0
#    while x == 0:
#        reference = player.current_room.id
#
#        if counter >= 10:
#            x = 1
#
#        if "n" in graph.vertices[reference] and graph.vertices[reference]['n'] is '?':
#            graph.vertices[reference]['n'] = 'OK'
#            traversal_path.append('n')
#            player.travel('n')
#
#            if not (player.current_room.id in graph.vertices):
#                graph.add_vertex(player.current_room.id)
#                for direction in player.current_room.get_exits():
#                    graph.add_edge(player.current_room.id, direction)
#
#        elif "s" in graph.vertices[reference] and graph.vertices[reference]['s'] is '?':
#            graph.vertices[reference]['s'] = 'OK'
#            traversal_path.append('s')
#            player.travel('s')
#
#            if not (player.current_room.id in graph.vertices):
#                graph.add_vertex(player.current_room.id)
#                for direction in player.current_room.get_exits():
#                    graph.add_edge(player.current_room.id, direction)
#
#        elif "w" in graph.vertices[reference] and graph.vertices[reference]['w'] is '?':
#            graph.vertices[reference]['w'] = 'OK'
#            traversal_path.append('w')
#            player.travel('w')
#
#            if not (player.current_room.id in graph.vertices):
#                graph.add_vertex(player.current_room.id)
#                for direction in player.current_room.get_exits():
#                    graph.add_edge(player.current_room.id, direction)
#
#        elif "e" in graph.vertices[reference] and graph.vertices[reference]['e'] is '?':
#            graph.vertices[reference]['e'] = 'OK'
#            traversal_path.append('e')
#            player.travel('e')
#
#            if not (player.current_room.id in graph.vertices):
#                graph.add_vertex(player.current_room.id)
#                for direction in player.current_room.get_exits():
#                    graph.add_edge(player.current_room.id, direction)
#        
#        else:
#            new_traversal_path = traversal_path
#            traveled_array = len(new_traversal_path) - 1            
#            while counter < 10:
#                while traveled_array >= 0:
#                    if new_traversal_path[traveled_array] == "n" and "s" in graph.vertices.get(reference):
#                        player.travel(opposite_of_n)
#                        traversal_path.append(opposite_of_n)
#                    elif new_traversal_path[traveled_array] == "s" and "n" in graph.vertices.get(reference):
#                        player.travel(opposite_of_s)
#                        traversal_path.append(opposite_of_s)
#                    elif new_traversal_path[traveled_array] == "w" and "e" in graph.vertices.get(reference):
#                        player.travel(opposite_of_w)
#                        traversal_path.append(opposite_of_w)
#                    elif new_traversal_path[traveled_array] == "e" and "w" in graph.vertices.get(reference):
#                        player.travel(opposite_of_e)
#                        traversal_path.append(opposite_of_e)
#
#                    reference = player.current_room.id
#
#                    if not (reference in graph.vertices):
#                        graph.add_vertex(player.current_room.id)
#                        for direction in player.current_room.get_exits():
#                            graph.add_edge(player.current_room.id, direction)
#
#                    if "n" in graph.vertices.get(reference) and graph.vertices.get(reference)['n'] == '?':
#                        graph.vertices[reference]['n'] = 'OK'
#                        traversal_path.append('n')
#                        player.travel('n')
#
#                        if not (player.current_room.id in graph.vertices):
#                            graph.add_vertex(player.current_room.id)
#                            for direction in player.current_room.get_exits():
#                                graph.add_edge(player.current_room.id, direction)
#
#                    elif "s" in graph.vertices.get(reference) and graph.vertices.get(reference)['s'] == '?':
#                        graph.vertices[reference]['s'] = 'OK'
#                        traversal_path.append('s')
#                        player.travel('s')
#
#                        if not (player.current_room.id in graph.vertices):
#                            graph.add_vertex(player.current_room.id)
#                            for direction in player.current_room.get_exits():
#                                graph.add_edge(player.current_room.id, direction)
#
#                    elif "w" in graph.vertices.get(reference) and graph.vertices.get(reference)['w'] == '?':
#                        graph.vertices[reference]['w'] = 'OK'
#                        traversal_path.append('w')
#                        player.travel('w')
#
#                        if not (player.current_room.id in graph.vertices):
#                            graph.add_vertex(player.current_room.id)
#                            for direction in player.current_room.get_exits():
#                                graph.add_edge(player.current_room.id, direction)
#
#                    elif "e" in graph.vertices.get(reference) and graph.vertices.get(reference)['e'] == '?':
#                        graph.vertices[reference]['e'] = 'OK'
#                        traversal_path.append('e')
#                        player.travel('e')
#
#                        if not (player.current_room.id in graph.vertices):
#                            graph.add_vertex(player.current_room.id)
#                            for direction in player.current_room.get_exits():
#                                graph.add_edge(player.current_room.id, direction)
#
#                    else:
#                        counter += 1
#                        traveled_array -= 1

#    q = Stack()
#    visited = set()
#
#    q.push(player.current_room.id)
#
#    while q.size() > 0:
#        v = q.pop()
#        if v not in visited:
#            visited.add(v)
#            newGraph.add_vertex(v)
#            for direction in player.current_room.get_exits():
#                newGraph.add_edge(v, direction)
#                player.travel(direction)
#                q.push(player.current_room.id)