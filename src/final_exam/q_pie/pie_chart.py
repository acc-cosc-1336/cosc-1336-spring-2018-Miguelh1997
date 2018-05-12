from pie_arc import PieArc
class PieChart:
    
    def __init__(self, pie_arcs):
        self.pie_arcs = pie_arcs
    
    def draw(self):       
        for arc in pie_arcs:
            arc.draw()
