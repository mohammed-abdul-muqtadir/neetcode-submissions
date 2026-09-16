class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        plot = []

        for i in range(len(position)):
            plot.append([position[i],speed[i],(target-position[i])/speed[i]])
        
        plot.sort(key=lambda x:x[0])
        

        sta = []

        for time in range(len(plot)):
            while sta and plot[time][2] >= sta[-1]:
                sta.pop()
            sta.append(plot[time][2])

        return len(sta)


