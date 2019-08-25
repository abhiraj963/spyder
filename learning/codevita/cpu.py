flag = 0
while flag:
    cores = int(input('cores in each cpu: '))
    mem = int(input('memory in gb: ')) * 1024
    no_of_apps = int(input('no of apps: '))
    if (cores>=0 and cores<=10) or (mem>=0 and mem <= 10*1024) or (no_of_apps>=0 and no_of_apps<=100):
        flag = 0
    app_dict = {}
    for i in range(0,no_of_apps):
        lst = []
        lst.append(input(f'cpu utiliztn {i}: '))
        lst.append(input(f'mem utiliztn in mb {i}: '))
        app_dict[f'app {i}'] = lst
    res_cpu = input('reserved cpu: ')
    res_mem = input('reserved memory in mb: ')
    
def cost(cpu_util, mem_util):
    constant_initial_cost = 100
    cost_per_hour = constant_initial_cost + (1.5/10000)*(cpu_util**3) + 0.5*(mem_util)
    return cost_per_hour

cost1 = cost(8.03+26.77+26.66,451/1024+192/1024+184/1024)
cost2 = cost(8.03+25.8+26.81,184/1024+207/1024+294/1024)
print(cost2+cost1)

        
        

