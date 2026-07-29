from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Assign items with no group to their own unique group
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        # Build graphs
        # Item graph: item -> [items that depend on it]
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        
        # Group graph: group -> [groups that depend on it]
        group_graph = defaultdict(set)
        group_indegree = defaultdict(int)
        
        # Initialize group indegrees
        for i in range(group_id):
            group_indegree[i] = 0
        
        # Build dependency graphs
        for i in range(n):
            for before_item in beforeItems[i]:
                item_graph[before_item].append(i)
                item_indegree[i] += 1
                
                # If items are in different groups, add group dependency
                if group[before_item] != group[i]:
                    if group[i] not in group_graph[group[before_item]]:
                        group_graph[group[before_item]].add(group[i])
                        group_indegree[group[i]] += 1
        
        # Topological sort for groups
        def topo_sort_groups():
            queue = deque([g for g in range(group_id) if group_indegree[g] == 0])
            result = []
            
            while queue:
                curr_group = queue.popleft()
                result.append(curr_group)
                
                for next_group in group_graph[curr_group]:
                    group_indegree[next_group] -= 1
                    if group_indegree[next_group] == 0:
                        queue.append(next_group)
            
            return result if len(result) == group_id else []
        
        # Topological sort for items within a group
        def topo_sort_items(items):
            local_indegree = {item: 0 for item in items}
            
            # Only count indegrees from items within the same group
            for item in items:
                for next_item in item_graph[item]:
                    if next_item in local_indegree:
                        local_indegree[next_item] += 1
            
            queue = deque([item for item in items if local_indegree[item] == 0])
            result = []
            
            while queue:
                curr_item = queue.popleft()
                result.append(curr_item)
                
                for next_item in item_graph[curr_item]:
                    if next_item in local_indegree:
                        local_indegree[next_item] -= 1
                        if local_indegree[next_item] == 0:
                            queue.append(next_item)
            
            return result if len(result) == len(items) else []
        
        # Get group order
        group_order = topo_sort_groups()
        if not group_order:
            return []
        
        # Group items by group
        group_to_items = defaultdict(list)
        for i in range(n):
            group_to_items[group[i]].append(i)
        
        # Sort items within each group and combine
        result = []
        for g in group_order:
            items = group_to_items[g]
            sorted_items = topo_sort_items(items)
            if len(sorted_items) != len(items):
                return []
            result.extend(sorted_items)
        
        return result