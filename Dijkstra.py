import heapq


def dijkstra(graph, start):
   """
   מממש את אלגוריתם דייקסטרה למציאת המסלול הקצר ביותר.
   """
   # אתחול מרחקים: 0 לנקודת המצא ואינסוף לכל השאר
   distances = {node: float('inf') for node in graph}
   distances[start] = 0

   # שמירת המסלול (מאיזה צומת הגענו לכל צומת)
   predecessors = {node: None for node in graph}

   # תור עדיפויות לשמירת הצמתים שצריך לבקר בהם
   priority_queue = [(0, start)]

   while priority_queue:
       current_distance, current_node = heapq.heappop(priority_queue)

       # אם מצאנו כבר מרחק קצר יותר לצומת הזה, נתעלם
       if current_distance > distances[current_node]:
           continue

       # מעבר על השכנים (תהליך ההרפיה - Relaxation)
       for neighbor, weight in graph[current_node].items():
           distance = current_distance + weight

           # אם מצאנו נתיב קצר יותר לשכן
           if distance < distances[neighbor]:
               distances[neighbor] = distance
               predecessors[neighbor] = current_node
               heapq.heappush(priority_queue, (distance, neighbor))

   return distances, predecessors


def get_path(predecessors, target):
   """משחזר את המסלול מהמקור ליעד"""
   path = []
   current = target
   while current is not None:
       path.append(current)
       current = predecessors[current]
   return " -> ".join(reversed(path))


def main():
   # ייצוג בית הקפה כגרף (מבוסס על מטריצת הסמיכות שלך)
   cafe_graph = {
       'A': {'B': 15, 'E': 10, 'J': 25},
       'B': {'C': 12, 'F': 5},
       'C': {'D': 7, 'G': 8},
       'D': {},
       'E': {'F': 14, 'I': 6},
       'F': {'G': 11},
       'G': {'J': 10},
       'H': {'D': 9},
       'I': {'H': 5},
       'J': {}
   }

   start_node = 'A'
   print(f"--- Running Dijkstra from Point {start_node} (Kitchen) ---\n")

   distances, predecessors = dijkstra(cafe_graph, start_node)

   # הדפסת התוצאות בצורה מסודרת
   print(f"{'Target':<8} | {'Distance':<10} | {'Shortest Path'}")
   print("-" * 40)

   for node in sorted(cafe_graph.keys()):
       if node == start_node: continue
       dist = distances[node]
       path = get_path(predecessors, node)
       print(f"{node:<8} | {dist:<10} | {path}")


if __name__ == "__main__":
   main()
