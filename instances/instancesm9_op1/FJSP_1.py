nr_machines = 10
nr_jobs = 12
orders = {0: {'product': 'enzyme0', 'due': 25}, 1: {'product': 'enzyme0', 'due': 18}, 2: {'product': 'enzyme1', 'due': 26}, 3: {'product': 'enzyme1', 'due': 15}, 4: {'product': 'enzyme2', 'due': 23}, 5: {'product': 'enzyme2', 'due': 19}, 6: {'product': 'enzyme3', 'due': 23}, 7: {'product': 'enzyme3', 'due': 20}, 8: {'product': 'enzyme4', 'due': 15}, 9: {'product': 'enzyme4', 'due': 18}, 10: {'product': 'enzyme5', 'due': 13}, 11: {'product': 'enzyme5', 'due': 24}}
machines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
operations = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1], 3: [0, 1], 4: [0, 1], 5: [0, 1], 6: [0, 1, 2], 7: [0, 1, 2], 8: [0, 1, 2], 9: [0, 1, 2], 10: [0, 1], 11: [0, 1]}
machineAlternatives = {(0, 0): [0, 1, 2, 9], (0, 1): [3, 4, 5, 6], (0, 2): [7, 8], (1, 0): [0, 1, 2, 9], (1, 1): [3, 4, 5, 6], (2, 0): [0, 1, 2, 9], (2, 1): [3, 4, 5, 6], (3, 0): [0, 1, 2, 9], (3, 1): [3, 4, 5, 6], (3, 2): [7, 8], (4, 0): [3, 4, 5, 6], (4, 1): [7, 8], (4, 2): [7, 8], (5, 0): [3, 4, 5, 6], (5, 1): [7, 8], (1, 2): [7, 8], (6, 0): [0, 1, 2, 9], (6, 1): [3, 4, 5, 6], (6, 2): [7, 8], (7, 0): [0, 1, 2, 9], (7, 1): [3, 4, 5, 6], (7, 2): [7, 8], (8, 0): [0, 1, 2, 9], (8, 1): [3, 4, 5, 6], (8, 2): [7, 8], (9, 0): [0, 1, 2, 9], (9, 1): [3, 4, 5, 6], (9, 2): [7, 8], (10, 0): [3, 4, 5, 6], (10, 1): [7, 8], (11, 0): [3, 4, 5, 6], (11, 1): [7, 8]}
processingTimes = {(0, 0, 0): 8, (0, 0, 1): 8, (0, 0, 2): 8, (0, 0, 9): 8, (0, 1, 3): 4, (0, 1, 4): 4, (0, 1, 5): 4, (0, 1, 6): 4, (0, 2, 7): 4, (0, 2, 8): 4, (1, 0, 0): 8, (1, 0, 1): 8, (1, 0, 2): 8, (1, 0, 9): 8, (1, 1, 3): 4, (1, 1, 4): 4, (1, 1, 5): 4, (1, 1, 6): 4, (2, 0, 3): 3, (2, 0, 4): 3, (2, 0, 5): 3, (2, 0, 6): 3, (2, 1, 7): 3, (2, 1, 8): 3, (3, 0, 0): 3, (3, 0, 1): 3, (3, 0, 2): 3, (3, 0, 9): 3, (3, 1, 3): 2, (3, 1, 4): 2, (3, 1, 5): 2, (3, 1, 6): 2, (3, 2, 7): 6, (3, 2, 8): 6, (4, 0, 0): 5, (4, 0, 1): 5, (4, 0, 2): 5, (4, 0, 9): 5, (4, 1, 3): 4, (4, 1, 4): 4, (4, 1, 5): 4, (4, 1, 6): 4, (4, 2, 7): 7, (4, 2, 8): 7, (5, 0, 3): 3, (5, 0, 4): 3, (5, 0, 5): 3, (5, 0, 6): 3, (5, 1, 7): 3, (5, 1, 8): 3, (1, 2, 7): 4, (1, 2, 8): 4, (2, 0, 0): 3, (2, 0, 1): 3, (2, 0, 2): 3, (2, 0, 9): 3, (2, 1, 3): 2, (2, 1, 4): 2, (2, 1, 5): 2, (2, 1, 6): 2, (4, 0, 3): 3, (4, 0, 4): 3, (4, 0, 5): 3, (4, 0, 6): 3, (4, 1, 7): 3, (4, 1, 8): 3, (6, 0, 0): 4, (6, 0, 1): 4, (6, 0, 2): 4, (6, 0, 9): 4, (6, 1, 3): 6, (6, 1, 4): 6, (6, 1, 5): 6, (6, 1, 6): 6, (6, 2, 7): 6, (6, 2, 8): 6, (7, 0, 0): 4, (7, 0, 1): 4, (7, 0, 2): 4, (7, 0, 9): 4, (7, 1, 3): 6, (7, 1, 4): 6, (7, 1, 5): 6, (7, 1, 6): 6, (7, 2, 7): 6, (7, 2, 8): 6, (8, 0, 0): 5, (8, 0, 1): 5, (8, 0, 2): 5, (8, 0, 9): 5, (8, 1, 3): 4, (8, 1, 4): 4, (8, 1, 5): 4, (8, 1, 6): 4, (8, 2, 7): 7, (8, 2, 8): 7, (9, 0, 0): 5, (9, 0, 1): 5, (9, 0, 2): 5, (9, 0, 9): 5, (9, 1, 3): 4, (9, 1, 4): 4, (9, 1, 5): 4, (9, 1, 6): 4, (9, 2, 7): 7, (9, 2, 8): 7, (10, 0, 3): 8, (10, 0, 4): 8, (10, 0, 5): 8, (10, 0, 6): 8, (10, 1, 7): 3, (10, 1, 8): 3, (11, 0, 3): 8, (11, 0, 4): 8, (11, 0, 5): 8, (11, 0, 6): 8, (11, 1, 7): 3, (11, 1, 8): 3}
changeOvers = {(0, 'enzyme0', 'enzyme0'): 0, (0, 'enzyme0', 'enzyme1'): 3, (0, 'enzyme0', 'enzyme2'): 1, (0, 'enzyme0', 'enzyme3'): 2, (0, 'enzyme0', 'enzyme4'): 2, (0, 'enzyme0', 'enzyme5'): 3, (0, 'enzyme1', 'enzyme0'): 1, (0, 'enzyme1', 'enzyme1'): 0, (0, 'enzyme1', 'enzyme2'): 1, (0, 'enzyme1', 'enzyme3'): 4, (0, 'enzyme1', 'enzyme4'): 3, (0, 'enzyme1', 'enzyme5'): 1, (0, 'enzyme2', 'enzyme0'): 1, (0, 'enzyme2', 'enzyme1'): 1, (0, 'enzyme2', 'enzyme2'): 0, (0, 'enzyme2', 'enzyme3'): 1, (0, 'enzyme2', 'enzyme4'): 3, (0, 'enzyme2', 'enzyme5'): 2, (0, 'enzyme3', 'enzyme0'): 2, (0, 'enzyme3', 'enzyme1'): 2, (0, 'enzyme3', 'enzyme2'): 3, (0, 'enzyme3', 'enzyme3'): 0, (0, 'enzyme3', 'enzyme4'): 4, (0, 'enzyme3', 'enzyme5'): 2, (0, 'enzyme4', 'enzyme0'): 2, (0, 'enzyme4', 'enzyme1'): 4, (0, 'enzyme4', 'enzyme2'): 3, (0, 'enzyme4', 'enzyme3'): 2, (0, 'enzyme4', 'enzyme4'): 0, (0, 'enzyme4', 'enzyme5'): 4, (0, 'enzyme5', 'enzyme0'): 1, (0, 'enzyme5', 'enzyme1'): 3, (0, 'enzyme5', 'enzyme2'): 1, (0, 'enzyme5', 'enzyme3'): 4, (0, 'enzyme5', 'enzyme4'): 3, (0, 'enzyme5', 'enzyme5'): 0, (1, 'enzyme0', 'enzyme0'): 0, (1, 'enzyme0', 'enzyme1'): 4, (1, 'enzyme0', 'enzyme2'): 1, (1, 'enzyme0', 'enzyme3'): 3, (1, 'enzyme0', 'enzyme4'): 3, (1, 'enzyme0', 'enzyme5'): 1, (1, 'enzyme1', 'enzyme0'): 1, (1, 'enzyme1', 'enzyme1'): 0, (1, 'enzyme1', 'enzyme2'): 2, (1, 'enzyme1', 'enzyme3'): 4, (1, 'enzyme1', 'enzyme4'): 3, (1, 'enzyme1', 'enzyme5'): 4, (1, 'enzyme2', 'enzyme0'): 1, (1, 'enzyme2', 'enzyme1'): 2, (1, 'enzyme2', 'enzyme2'): 0, (1, 'enzyme2', 'enzyme3'): 4, (1, 'enzyme2', 'enzyme4'): 3, (1, 'enzyme2', 'enzyme5'): 3, (1, 'enzyme3', 'enzyme0'): 4, (1, 'enzyme3', 'enzyme1'): 1, (1, 'enzyme3', 'enzyme2'): 1, (1, 'enzyme3', 'enzyme3'): 0, (1, 'enzyme3', 'enzyme4'): 1, (1, 'enzyme3', 'enzyme5'): 2, (1, 'enzyme4', 'enzyme0'): 3, (1, 'enzyme4', 'enzyme1'): 4, (1, 'enzyme4', 'enzyme2'): 4, (1, 'enzyme4', 'enzyme3'): 1, (1, 'enzyme4', 'enzyme4'): 0, (1, 'enzyme4', 'enzyme5'): 4, (1, 'enzyme5', 'enzyme0'): 1, (1, 'enzyme5', 'enzyme1'): 1, (1, 'enzyme5', 'enzyme2'): 1, (1, 'enzyme5', 'enzyme3'): 2, (1, 'enzyme5', 'enzyme4'): 1, (1, 'enzyme5', 'enzyme5'): 0, (2, 'enzyme0', 'enzyme0'): 0, (2, 'enzyme0', 'enzyme1'): 1, (2, 'enzyme0', 'enzyme2'): 3, (2, 'enzyme0', 'enzyme3'): 2, (2, 'enzyme0', 'enzyme4'): 3, (2, 'enzyme0', 'enzyme5'): 2, (2, 'enzyme1', 'enzyme0'): 4, (2, 'enzyme1', 'enzyme1'): 0, (2, 'enzyme1', 'enzyme2'): 1, (2, 'enzyme1', 'enzyme3'): 2, (2, 'enzyme1', 'enzyme4'): 3, (2, 'enzyme1', 'enzyme5'): 3, (2, 'enzyme2', 'enzyme0'): 3, (2, 'enzyme2', 'enzyme1'): 1, (2, 'enzyme2', 'enzyme2'): 0, (2, 'enzyme2', 'enzyme3'): 3, (2, 'enzyme2', 'enzyme4'): 4, (2, 'enzyme2', 'enzyme5'): 4, (2, 'enzyme3', 'enzyme0'): 3, (2, 'enzyme3', 'enzyme1'): 1, (2, 'enzyme3', 'enzyme2'): 2, (2, 'enzyme3', 'enzyme3'): 0, (2, 'enzyme3', 'enzyme4'): 3, (2, 'enzyme3', 'enzyme5'): 3, (2, 'enzyme4', 'enzyme0'): 1, (2, 'enzyme4', 'enzyme1'): 4, (2, 'enzyme4', 'enzyme2'): 1, (2, 'enzyme4', 'enzyme3'): 2, (2, 'enzyme4', 'enzyme4'): 0, (2, 'enzyme4', 'enzyme5'): 4, (2, 'enzyme5', 'enzyme0'): 4, (2, 'enzyme5', 'enzyme1'): 2, (2, 'enzyme5', 'enzyme2'): 1, (2, 'enzyme5', 'enzyme3'): 3, (2, 'enzyme5', 'enzyme4'): 3, (2, 'enzyme5', 'enzyme5'): 0, (3, 'enzyme0', 'enzyme0'): 0, (3, 'enzyme0', 'enzyme1'): 3, (3, 'enzyme0', 'enzyme2'): 3, (3, 'enzyme0', 'enzyme3'): 2, (3, 'enzyme0', 'enzyme4'): 1, (3, 'enzyme0', 'enzyme5'): 3, (3, 'enzyme1', 'enzyme0'): 4, (3, 'enzyme1', 'enzyme1'): 0, (3, 'enzyme1', 'enzyme2'): 3, (3, 'enzyme1', 'enzyme3'): 3, (3, 'enzyme1', 'enzyme4'): 1, (3, 'enzyme1', 'enzyme5'): 3, (3, 'enzyme2', 'enzyme0'): 2, (3, 'enzyme2', 'enzyme1'): 2, (3, 'enzyme2', 'enzyme2'): 0, (3, 'enzyme2', 'enzyme3'): 2, (3, 'enzyme2', 'enzyme4'): 1, (3, 'enzyme2', 'enzyme5'): 1, (3, 'enzyme3', 'enzyme0'): 3, (3, 'enzyme3', 'enzyme1'): 1, (3, 'enzyme3', 'enzyme2'): 1, (3, 'enzyme3', 'enzyme3'): 0, (3, 'enzyme3', 'enzyme4'): 4, (3, 'enzyme3', 'enzyme5'): 4, (3, 'enzyme4', 'enzyme0'): 3, (3, 'enzyme4', 'enzyme1'): 2, (3, 'enzyme4', 'enzyme2'): 3, (3, 'enzyme4', 'enzyme3'): 3, (3, 'enzyme4', 'enzyme4'): 0, (3, 'enzyme4', 'enzyme5'): 3, (3, 'enzyme5', 'enzyme0'): 1, (3, 'enzyme5', 'enzyme1'): 1, (3, 'enzyme5', 'enzyme2'): 3, (3, 'enzyme5', 'enzyme3'): 1, (3, 'enzyme5', 'enzyme4'): 4, (3, 'enzyme5', 'enzyme5'): 0, (4, 'enzyme0', 'enzyme0'): 0, (4, 'enzyme0', 'enzyme1'): 2, (4, 'enzyme0', 'enzyme2'): 4, (4, 'enzyme0', 'enzyme3'): 2, (4, 'enzyme0', 'enzyme4'): 1, (4, 'enzyme0', 'enzyme5'): 1, (4, 'enzyme1', 'enzyme0'): 2, (4, 'enzyme1', 'enzyme1'): 0, (4, 'enzyme1', 'enzyme2'): 3, (4, 'enzyme1', 'enzyme3'): 3, (4, 'enzyme1', 'enzyme4'): 2, (4, 'enzyme1', 'enzyme5'): 4, (4, 'enzyme2', 'enzyme0'): 1, (4, 'enzyme2', 'enzyme1'): 4, (4, 'enzyme2', 'enzyme2'): 0, (4, 'enzyme2', 'enzyme3'): 3, (4, 'enzyme2', 'enzyme4'): 4, (4, 'enzyme2', 'enzyme5'): 3, (4, 'enzyme3', 'enzyme0'): 2, (4, 'enzyme3', 'enzyme1'): 1, (4, 'enzyme3', 'enzyme2'): 2, (4, 'enzyme3', 'enzyme3'): 0, (4, 'enzyme3', 'enzyme4'): 2, (4, 'enzyme3', 'enzyme5'): 1, (4, 'enzyme4', 'enzyme0'): 4, (4, 'enzyme4', 'enzyme1'): 4, (4, 'enzyme4', 'enzyme2'): 2, (4, 'enzyme4', 'enzyme3'): 3, (4, 'enzyme4', 'enzyme4'): 0, (4, 'enzyme4', 'enzyme5'): 1, (4, 'enzyme5', 'enzyme0'): 1, (4, 'enzyme5', 'enzyme1'): 3, (4, 'enzyme5', 'enzyme2'): 1, (4, 'enzyme5', 'enzyme3'): 2, (4, 'enzyme5', 'enzyme4'): 1, (4, 'enzyme5', 'enzyme5'): 0, (5, 'enzyme0', 'enzyme0'): 0, (5, 'enzyme0', 'enzyme1'): 2, (5, 'enzyme0', 'enzyme2'): 2, (5, 'enzyme0', 'enzyme3'): 2, (5, 'enzyme0', 'enzyme4'): 1, (5, 'enzyme0', 'enzyme5'): 3, (5, 'enzyme1', 'enzyme0'): 4, (5, 'enzyme1', 'enzyme1'): 0, (5, 'enzyme1', 'enzyme2'): 2, (5, 'enzyme1', 'enzyme3'): 3, (5, 'enzyme1', 'enzyme4'): 4, (5, 'enzyme1', 'enzyme5'): 2, (5, 'enzyme2', 'enzyme0'): 3, (5, 'enzyme2', 'enzyme1'): 1, (5, 'enzyme2', 'enzyme2'): 0, (5, 'enzyme2', 'enzyme3'): 3, (5, 'enzyme2', 'enzyme4'): 4, (5, 'enzyme2', 'enzyme5'): 3, (5, 'enzyme3', 'enzyme0'): 2, (5, 'enzyme3', 'enzyme1'): 3, (5, 'enzyme3', 'enzyme2'): 3, (5, 'enzyme3', 'enzyme3'): 0, (5, 'enzyme3', 'enzyme4'): 1, (5, 'enzyme3', 'enzyme5'): 2, (5, 'enzyme4', 'enzyme0'): 1, (5, 'enzyme4', 'enzyme1'): 4, (5, 'enzyme4', 'enzyme2'): 1, (5, 'enzyme4', 'enzyme3'): 1, (5, 'enzyme4', 'enzyme4'): 0, (5, 'enzyme4', 'enzyme5'): 3, (5, 'enzyme5', 'enzyme0'): 4, (5, 'enzyme5', 'enzyme1'): 4, (5, 'enzyme5', 'enzyme2'): 3, (5, 'enzyme5', 'enzyme3'): 4, (5, 'enzyme5', 'enzyme4'): 4, (5, 'enzyme5', 'enzyme5'): 0, (6, 'enzyme0', 'enzyme0'): 0, (6, 'enzyme0', 'enzyme1'): 1, (6, 'enzyme0', 'enzyme2'): 1, (6, 'enzyme0', 'enzyme3'): 2, (6, 'enzyme0', 'enzyme4'): 3, (6, 'enzyme0', 'enzyme5'): 3, (6, 'enzyme1', 'enzyme0'): 4, (6, 'enzyme1', 'enzyme1'): 0, (6, 'enzyme1', 'enzyme2'): 2, (6, 'enzyme1', 'enzyme3'): 1, (6, 'enzyme1', 'enzyme4'): 3, (6, 'enzyme1', 'enzyme5'): 2, (6, 'enzyme2', 'enzyme0'): 4, (6, 'enzyme2', 'enzyme1'): 3, (6, 'enzyme2', 'enzyme2'): 0, (6, 'enzyme2', 'enzyme3'): 4, (6, 'enzyme2', 'enzyme4'): 3, (6, 'enzyme2', 'enzyme5'): 1, (6, 'enzyme3', 'enzyme0'): 3, (6, 'enzyme3', 'enzyme1'): 1, (6, 'enzyme3', 'enzyme2'): 3, (6, 'enzyme3', 'enzyme3'): 0, (6, 'enzyme3', 'enzyme4'): 2, (6, 'enzyme3', 'enzyme5'): 2, (6, 'enzyme4', 'enzyme0'): 2, (6, 'enzyme4', 'enzyme1'): 2, (6, 'enzyme4', 'enzyme2'): 2, (6, 'enzyme4', 'enzyme3'): 4, (6, 'enzyme4', 'enzyme4'): 0, (6, 'enzyme4', 'enzyme5'): 1, (6, 'enzyme5', 'enzyme0'): 2, (6, 'enzyme5', 'enzyme1'): 2, (6, 'enzyme5', 'enzyme2'): 3, (6, 'enzyme5', 'enzyme3'): 1, (6, 'enzyme5', 'enzyme4'): 3, (6, 'enzyme5', 'enzyme5'): 0, (7, 'enzyme0', 'enzyme0'): 0, (7, 'enzyme0', 'enzyme1'): 4, (7, 'enzyme0', 'enzyme2'): 2, (7, 'enzyme0', 'enzyme3'): 2, (7, 'enzyme0', 'enzyme4'): 2, (7, 'enzyme0', 'enzyme5'): 2, (7, 'enzyme1', 'enzyme0'): 2, (7, 'enzyme1', 'enzyme1'): 0, (7, 'enzyme1', 'enzyme2'): 3, (7, 'enzyme1', 'enzyme3'): 2, (7, 'enzyme1', 'enzyme4'): 1, (7, 'enzyme1', 'enzyme5'): 4, (7, 'enzyme2', 'enzyme0'): 1, (7, 'enzyme2', 'enzyme1'): 1, (7, 'enzyme2', 'enzyme2'): 0, (7, 'enzyme2', 'enzyme3'): 2, (7, 'enzyme2', 'enzyme4'): 4, (7, 'enzyme2', 'enzyme5'): 2, (7, 'enzyme3', 'enzyme0'): 3, (7, 'enzyme3', 'enzyme1'): 1, (7, 'enzyme3', 'enzyme2'): 3, (7, 'enzyme3', 'enzyme3'): 0, (7, 'enzyme3', 'enzyme4'): 2, (7, 'enzyme3', 'enzyme5'): 3, (7, 'enzyme4', 'enzyme0'): 2, (7, 'enzyme4', 'enzyme1'): 3, (7, 'enzyme4', 'enzyme2'): 4, (7, 'enzyme4', 'enzyme3'): 4, (7, 'enzyme4', 'enzyme4'): 0, (7, 'enzyme4', 'enzyme5'): 3, (7, 'enzyme5', 'enzyme0'): 4, (7, 'enzyme5', 'enzyme1'): 1, (7, 'enzyme5', 'enzyme2'): 1, (7, 'enzyme5', 'enzyme3'): 1, (7, 'enzyme5', 'enzyme4'): 3, (7, 'enzyme5', 'enzyme5'): 0, (8, 'enzyme0', 'enzyme0'): 0, (8, 'enzyme0', 'enzyme1'): 1, (8, 'enzyme0', 'enzyme2'): 2, (8, 'enzyme0', 'enzyme3'): 3, (8, 'enzyme0', 'enzyme4'): 2, (8, 'enzyme0', 'enzyme5'): 4, (8, 'enzyme1', 'enzyme0'): 1, (8, 'enzyme1', 'enzyme1'): 0, (8, 'enzyme1', 'enzyme2'): 1, (8, 'enzyme1', 'enzyme3'): 4, (8, 'enzyme1', 'enzyme4'): 3, (8, 'enzyme1', 'enzyme5'): 1, (8, 'enzyme2', 'enzyme0'): 4, (8, 'enzyme2', 'enzyme1'): 1, (8, 'enzyme2', 'enzyme2'): 0, (8, 'enzyme2', 'enzyme3'): 3, (8, 'enzyme2', 'enzyme4'): 2, (8, 'enzyme2', 'enzyme5'): 4, (8, 'enzyme3', 'enzyme0'): 3, (8, 'enzyme3', 'enzyme1'): 2, (8, 'enzyme3', 'enzyme2'): 4, (8, 'enzyme3', 'enzyme3'): 0, (8, 'enzyme3', 'enzyme4'): 2, (8, 'enzyme3', 'enzyme5'): 3, (8, 'enzyme4', 'enzyme0'): 3, (8, 'enzyme4', 'enzyme1'): 4, (8, 'enzyme4', 'enzyme2'): 1, (8, 'enzyme4', 'enzyme3'): 4, (8, 'enzyme4', 'enzyme4'): 0, (8, 'enzyme4', 'enzyme5'): 1, (8, 'enzyme5', 'enzyme0'): 4, (8, 'enzyme5', 'enzyme1'): 4, (8, 'enzyme5', 'enzyme2'): 1, (8, 'enzyme5', 'enzyme3'): 1, (8, 'enzyme5', 'enzyme4'): 2, (8, 'enzyme5', 'enzyme5'): 0, (9, 'enzyme0', 'enzyme0'): 0, (9, 'enzyme0', 'enzyme1'): 4, (9, 'enzyme0', 'enzyme2'): 2, (9, 'enzyme0', 'enzyme3'): 3, (9, 'enzyme0', 'enzyme4'): 2, (9, 'enzyme0', 'enzyme5'): 4, (9, 'enzyme1', 'enzyme0'): 2, (9, 'enzyme1', 'enzyme1'): 0, (9, 'enzyme1', 'enzyme2'): 3, (9, 'enzyme1', 'enzyme3'): 4, (9, 'enzyme1', 'enzyme4'): 3, (9, 'enzyme1', 'enzyme5'): 4, (9, 'enzyme2', 'enzyme0'): 4, (9, 'enzyme2', 'enzyme1'): 1, (9, 'enzyme2', 'enzyme2'): 0, (9, 'enzyme2', 'enzyme3'): 3, (9, 'enzyme2', 'enzyme4'): 4, (9, 'enzyme2', 'enzyme5'): 4, (9, 'enzyme3', 'enzyme0'): 3, (9, 'enzyme3', 'enzyme1'): 2, (9, 'enzyme3', 'enzyme2'): 4, (9, 'enzyme3', 'enzyme3'): 0, (9, 'enzyme3', 'enzyme4'): 2, (9, 'enzyme3', 'enzyme5'): 3, (9, 'enzyme4', 'enzyme0'): 3, (9, 'enzyme4', 'enzyme1'): 4, (9, 'enzyme4', 'enzyme2'): 4, (9, 'enzyme4', 'enzyme3'): 4, (9, 'enzyme4', 'enzyme4'): 0, (9, 'enzyme4', 'enzyme5'): 3, (9, 'enzyme5', 'enzyme0'): 4, (9, 'enzyme5', 'enzyme1'): 4, (9, 'enzyme5', 'enzyme2'): 1, (9, 'enzyme5', 'enzyme3'): 1, (9, 'enzyme5', 'enzyme4'): 3, (9, 'enzyme5', 'enzyme5'): 0}
