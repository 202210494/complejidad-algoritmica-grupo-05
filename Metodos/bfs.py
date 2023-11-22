from queue import Queue
from database_manager import SocialMediaDatabaseManager

def bfs_find_paths(start_user, end_user, db_manager):
    global parents
    parents = {start_user: None}


    queue = Queue()
    queue.put(start_user)

    while not queue.empty():
        current_user = queue.get()

        if current_user == end_user:
    
            path = [end_user]
            while parents[end_user] is not None:
                end_user = parents[end_user]
                path.insert(0, end_user)
            return [path]


        success, neighbors = db_manager.get_following(current_user)
        if success:
            for neighbor in neighbors:
          
                if neighbor not in parents:
                    parents[neighbor] = current_user
                    queue.put(neighbor)

    return []

#solo para probar si funciona 
#if __name__ == "__main__":
#    db_manager = SocialMediaDatabaseManager()
#    start_user = "usuario_inicial"
#    end_user = "usuario_final"

#    paths = bfs_find_paths(start_user, end_user, db_manager)

#    if paths:
#        print(f"Se encontraron caminos de {start_user} a {end_user}:")
#        for path in paths:
#            print(" -> ".join(path))
#    else:
#        print(f"No se encontraron caminos de {start_user} a {end_user}.")